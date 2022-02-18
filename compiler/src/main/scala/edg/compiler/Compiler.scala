package edg.compiler

import scala.collection.{SeqMap, mutable}
import edgir.schema.schema
import edgir.expr.expr
import edgir.ref.ref
import edgir.ref.ref.{LibraryPath, LocalPath}
import edg.wir.{DesignPath, IndirectDesignPath, IndirectStep, PathSuffix, PortLike, Refinements}
import edg.{EdgirUtils, ExprBuilder, wir}
import edg.util.{DependencyGraph, Errorable}
import EdgirUtils._


class IllegalConstraintException(msg: String) extends Exception(msg)


sealed trait ElaborateRecord
object ElaborateRecord {
  sealed trait ElaborateTask extends ElaborateRecord  // an elaboration task that can be run
  sealed trait ElaborateDependency extends ElaborateRecord  // an elaboration dependency

  case class Block(blockPath: DesignPath) extends ElaborateTask  // even when done, still may only be a generator
  case class Link(linkPath: DesignPath) extends ElaborateTask
  // Connection to be elaborated, to set port parameter, IS_CONNECTED, and CONNECTED_LINK equivalences.
  case class Connect(toLinkPortPath: DesignPath, fromLinkPortPath: DesignPath) extends ElaborateTask

  case class Generator(blockPath: DesignPath, blockClass: LibraryPath, fnName: String,
                       unrefinedClass: Option[LibraryPath],
                       requiredParams: Seq[ref.LocalPath], requiredPorts: Seq[ref.LocalPath]
                      ) extends ElaborateTask {
    override def toString: String = s"Generator(${blockClass.toSimpleString}.$fnName @ $blockPath)"
  }

  case class ParamValue(paramPath: IndirectDesignPath) extends ElaborateDependency  // when solved

  // Set when the connection from the link's port to portPath have been elaborated
  // (or in the link port case, when the link has been elaborated).
  // If the port is not connected, this is set when the port has been elaborated.
  // When this is complete, the port's IS_CONNECTED, CONNECTED_LINK (if applicable) will have their final values.
  case class ConnectedLink(portPath: DesignPath) extends ElaborateDependency
}


sealed trait CompilerError
object CompilerError {
  case class Unelaborated(elaborateRecord: ElaborateRecord, missing: Set[ElaborateRecord]) extends CompilerError {
    // These errors may be redundant with below, but provides dependency data
    override def toString: String = s"Unelaborated missing dependencies $elaborateRecord:\n" +
        s"${missing.map(x => s"- $x").mkString("\n")}"
  }
  case class LibraryElement(path: DesignPath, target: ref.LibraryPath) extends CompilerError {
    override def toString: String = s"Unelaborated library element ${target.toSimpleString} @ $path"
  }

  case class LibraryError(path: DesignPath, target: ref.LibraryPath, err: String) extends CompilerError {
    override def toString: String = s"Library error ${target.toSimpleString} @ $path: $err"
  }
  case class GeneratorError(path: DesignPath, target: ref.LibraryPath, fn: String, err: String) extends CompilerError {
    override def toString: String = s"Generator error ${target.toSimpleString}.$fn @ $path: $err"
  }
  case class RefinementSubclassError(path: DesignPath, refinedLibrary: ref.LibraryPath, designLibrary: ref.LibraryPath)
      extends CompilerError {
    override def toString: String =
      s"Invalid refinement ${refinedLibrary.toSimpleString} <- ${designLibrary.toSimpleString} @ $path"
  }

  case class OverAssign(target: IndirectDesignPath,
                        causes: Seq[OverAssignCause]) extends CompilerError {
    override def toString: String = s"Overassign to $target:\n" +
        s"${causes.map(x => s"- $x").mkString("\n")}"
  }

  case class AbstractBlock(path: DesignPath, blockType: ref.LibraryPath) extends CompilerError {
    override def toString: String = s"Abstract block: $path (of type ${blockType.toSimpleString})"
  }

  case class FailedAssertion(root: DesignPath, constrName: String,
                             value: expr.ValueExpr, result: ExprValue) extends CompilerError {
    override def toString: String =
      s"Failed assertion: $root.$constrName, ${ExprToString.apply(value)} => $result"
  }
  case class MissingAssertion(root: DesignPath, constrName: String,
                              value: expr.ValueExpr, missing: Set[ExprRef]) extends CompilerError {
    override def toString: String =
      s"Unevaluated assertion: $root.$constrName (${ExprToString.apply(value)}), missing ${missing.mkString(", ")}"
  }

  // TODO should this be an error? Currently a debugging tool
  case class EmptyRange(param: IndirectDesignPath, root: DesignPath, constrName: String,
                        value: expr.ValueExpr) extends CompilerError

  sealed trait OverAssignCause
  object OverAssignCause {
    case class Assign(target: IndirectDesignPath, root: DesignPath, constrName: String, value: expr.ValueExpr)
        extends OverAssignCause {
      override def toString = s"Assign $target <- ${ExprToString(value)} @ $root.$constrName"
    }
    case class Equal(target: IndirectDesignPath, source: IndirectDesignPath)  // TODO constraint info once we track that?
        extends OverAssignCause {
      override def toString = s"Equals $target = $source"
    }
  }
}


/** Compiler for a particular design, with an associated library to elaborate references from.
  * TODO also needs a Python interface for generators, somewhere.
  *
  * During the compilation process, internal data structures are mutated.
  *
  * Port parameters are propagated by expanding connect and export statements between connected ports
  * into equalities between all contained parameters.
  * This expansion triggers when both ports are fully elaborated, and checks the structures of both ends
  * for equivalence.
  *
  * CONNECTED_LINK parameters are propagated by expanding from the link's top-level port outward.
  * Expansion triggers at the link-side top-level port (by ref matching), or when the towards-innermost-link
  * (or towards-outermost-block) port is expanded.
  * A list of link params is kept in a hashmap indexed by ports, as they are expanded.
  *
  * Alternative: fetch links from library (using the port type) to get params to expand.
  * Problem: a bit more restrictive than what can be expressed in a block - but should be a common interface.
  *
  * It is intentional to allow a link-side port to access the CONNECTED_LINK, as a mechanism to access inner links.
  */
class Compiler(inputDesignPb: schema.Design, library: edg.wir.Library,
               refinements: Refinements=Refinements()) {
  // TODO better debug toggle
//  protected def debug(msg: => String): Unit = println(msg)
  protected def debug(msg: => String): Unit = { }

  def readableLibraryPath(path: ref.LibraryPath): String = {  // TODO refactor to shared utils?
    path.getTarget.getName
  }

  // Working design tree data structure
  private var root = new wir.Block(inputDesignPb.getContents, None)  // TODO refactor to unify root / non-root cases
  def resolve(path: DesignPath): wir.Pathable = root.resolve(path.steps)
  def resolveBlock(path: DesignPath): wir.BlockLike = root.resolve(path.steps).asInstanceOf[wir.BlockLike]
  def resolveLink(path: DesignPath): wir.LinkLike = root.resolve(path.steps).asInstanceOf[wir.LinkLike]
  def resolvePort(path: DesignPath): wir.PortLike = root.resolve(path.steps).asInstanceOf[wir.PortLike]

  // Main data structure that tracks the next unit to elaborate
  private val elaboratePending = DependencyGraph[ElaborateRecord, None.type]()

  // Design parameters solving (constraint evaluation) and assertions
  private val constProp = new ConstProp() {
    override def onParamSolved(param: IndirectDesignPath, value: ExprValue): Unit = {
      elaboratePending.setValue(ElaborateRecord.ParamValue(param), null)
    }
  }
  private[edg] def getValue(path: IndirectDesignPath): Option[ExprValue] = constProp.getValue(path)  // TODO clean up this API?
  for ((path, value) <- refinements.instanceValues) {  // seed const prop with path assertions
    constProp.setForcedValue(path.asIndirect, value, "path refinement")
  }

  private val assertions = mutable.Buffer[(DesignPath, String, expr.ValueExpr, SourceLocator)]()  // containing block, name, expr

  // Supplemental elaboration data structures
  private val linkParams = mutable.HashMap[DesignPath, Seq[IndirectStep]]()  // link path -> list of params
  private val connectedLink = mutable.HashMap[DesignPath, DesignPath]()  // port -> connected link path
  private val portDirectlyConnected = mutable.HashMap[DesignPath, Boolean]()  // if port directly connected in enclosing block

  private val errors = mutable.ListBuffer[CompilerError]()

  // Returns all errors, by scanning the design tree for errors and adding errors accumulated through the compile
  // process
  def getErrors(): Seq[CompilerError] = {
    val assertionErrors = assertions.flatMap { case (root, constrName, value, sourceLocator) =>
      new ExprEvaluatePartial(constProp, root).map(value) match {
        case ExprResult.Result(BooleanValue(true)) => None
        case ExprResult.Result(result) =>
          Some(CompilerError.FailedAssertion(root, constrName, value, result))
        case ExprResult.Missing(missing) =>
          Some(CompilerError.MissingAssertion(root, constrName, value, missing))
      }
    }.toSeq

    val pendingErrors = elaboratePending.getMissing.map { missingNode =>
      CompilerError.Unelaborated(missingNode, elaboratePending.nodeMissing(missingNode))
    }.toSeq

    errors.toSeq ++ constProp.getErrors ++ pendingErrors ++ assertionErrors
  }

  // Hook method to be overridden, eg for status
  //
  def onElaborate(record: ElaborateRecord): Unit = { }

  // Actual compilation methods
  //

  // Elaborate a connection (either a connect or export), by generating bidirectional equality constraints
  // including link parameters (through CONNECTED_LINK) and IS_CONNECTED.
  // Neither port can be an array (container) port (array connects should be expanded into individual element connects),
  // but ports may be bundle or inner ports (in bundles or arrays).
  // Only the link side port needs to have been elaborated.
  protected def elaborateConnect(toLinkPortPath: DesignPath, toBlockPortPath: DesignPath): Unit = {
    // Generate port-port parameter propagation
    // All connected ports should have params
    val toLinkPort = resolvePort(toLinkPortPath).asInstanceOf[wir.HasParams]
    val connectedSteps = toLinkPort.getParams.keys.map(IndirectStep.Element(_)) ++ Seq(IndirectStep.IsConnected)
    for (connectedStep <- connectedSteps) {
      constProp.addEquality(
        toLinkPortPath.asIndirect + connectedStep,
        toBlockPortPath.asIndirect + connectedStep
      )
    }

    connectedLink.get(toLinkPortPath) match {
      case Some(linkPath) =>  // Generate the CONNECTED_LINK equalities, if there is a connected link
        connectedLink.put(toBlockPortPath, linkPath)  // propagate CONNECTED_LINK params
        for (linkParam <- linkParams(linkPath)) {
          constProp.addEquality(
            toBlockPortPath.asIndirect + IndirectStep.ConnectedLink + linkParam,
            linkPath.asIndirect + linkParam,
          )
        }
      case None =>
    }

    // Add sub-ports to the elaboration dependency graph, as appropriate
    toLinkPort match {
      case toLinkPort: wir.Bundle =>
        for (portName <- toLinkPort.getElaboratedPorts.keys) {
          elaboratePending.addNode(
            ElaborateRecord.Connect(toLinkPortPath + portName, toBlockPortPath + portName),
            Seq(ElaborateRecord.ConnectedLink(toLinkPortPath + portName))
          )
        }
      case toLinkPort => // everything else ignored
    }

    // Register port as finished
    elaboratePending.setValue(ElaborateRecord.ConnectedLink(toBlockPortPath), None)
  }

  // Called for each param declaration, currently just registers the declaration and type signature.
  protected def processParamDeclarations(path: DesignPath, hasParams: wir.HasParams): Unit = {
    for ((paramName, param) <- hasParams.getParams) {
      constProp.addDeclaration(path + paramName, param)
    }
  }

  // Elaborates the port, mutating it in-place. Recursive.
  protected def elaboratePort(path: DesignPath, container: wir.HasMutablePorts, port: wir.PortLike): Unit = {
    // Instantiate as needed
    val instantiated = port match {
      case port: wir.PortLibrary =>
        val libraryPath = port.target
        debug(s"Elaborate port @ $path")

        val portPb = library.getPort(libraryPath) match {
          case Errorable.Success(portPb) => portPb
          case Errorable.Error(err) =>
            import edgir.elem.elem, edg.IrPort
            errors += CompilerError.LibraryError(path, libraryPath, err)
            IrPort.Port(elem.Port())
        }
        val newPort = wir.PortLike.fromIrPort(portPb)
        container.elaborate(path.lastString, newPort)
        newPort
      case port: wir.PortArray => port  // no instantiation needed
      case port => throw new NotImplementedError(s"unknown unelaborated port $port")
    }

    // Process and recurse as needed
    instantiated match {
      case port: wir.Port =>
        constProp.setValue(path.asIndirect + IndirectStep.Name, TextValue(path.toString))
        processParamDeclarations(path, port)
      case port: wir.Bundle =>
        constProp.setValue(path.asIndirect + IndirectStep.Name, TextValue(path.toString))
        processParamDeclarations(path, port)
        for ((childPortName, childPort) <- port.getUnelaboratedPorts) {
          elaboratePort(path + childPortName, port, childPort)
        }
      case port: wir.PortArray =>
        // arrays have no params (including name), but we need to instantiate the array
        val childPortNames = constProp.getArrayElts(path) match {
          case Some(elts) => elts
          case None =>  // TODO can the empty case be set with everything else?
            constProp.setArrayElts(path, Seq())
            constProp.setValue(path.asIndirect + IndirectStep.Length, IntValue(0))
            Seq()
        }
        val childPortLibraries = (childPortNames map { childPortName =>
          childPortName -> wir.PortLibrary.apply(port.getType)
        }).toMap
        port.setPorts(childPortLibraries)
        for ((childPortName, childPort) <- port.getUnelaboratedPorts) {
          elaboratePort(path + childPortName, port, childPort)
        }
      case port => throw new NotImplementedError(s"unknown instantiated port $port")
    }
  }

  // Additional processing for ports that sets not-connected if they haven't been connected (in the enclosing block)
  protected def setPortNotConnected(portPath: DesignPath, port: wir.PortLike): Unit = {
    val topIsConnected = port match {  // If not connected, set unconnected
      case _ @ (_: wir.Port | _: wir.Bundle) =>
        if (!portDirectlyConnected.contains(portPath)) {
          portDirectlyConnected.put(portPath, false)
          constProp.setValue(portPath.asIndirect + IndirectStep.IsConnected, BooleanValue(false))
          elaboratePending.setValue(ElaborateRecord.ConnectedLink(portPath), None)
          false
        } else {
          require(portDirectlyConnected(portPath))  // it should not have been assigned false from anywhere else
          true
        }
      case _: wir.PortArray => false  // arrays should not have connection status
      case port => throw new NotImplementedError(s"unknown instantiated port $port")
    }

    port match {
      case port: wir.Bundle =>
        for ((childPortName, childPort) <- port.getElaboratedPorts) {
          if (topIsConnected) {  // only propagate connectivity status
            require(!portDirectlyConnected.contains(portPath + childPortName))
            portDirectlyConnected.put(portPath + childPortName, true)
          }  // in the false case, it would be set during the recursive call
          setPortNotConnected(portPath + childPortName, childPort)
        }
      case port: wir.PortArray =>
        // don't propagate connectivity status, since connectivity should be directly set for array elts
        for ((childPortName, childPort) <- port.getElaboratedPorts) {
          setPortNotConnected(portPath + childPortName, childPort)
        }
      case _: wir.Port =>  // no recursion case for leaf types
      case port => throw new NotImplementedError(s"unknown instantiated port $port")
    }
  }

  // Sets the ConnectedLink for all the top-level ports (recursing into arrays, but not bundles)
  protected def setPortConnectedLink(portPath: DesignPath, port: wir.PortLike, linkPath: DesignPath): Unit = {
    port match {
      case _: wir.Port | _: wir.Bundle =>
        // false case set in setPortNotConnected - TODO this needs serious cleaning
        if (portDirectlyConnected.contains(portPath)) {
          connectedLink.put(portPath, linkPath)
          constProp.setValue(portPath.asIndirect + IndirectStep.IsConnected, BooleanValue(true))
          elaboratePending.setValue(ElaborateRecord.ConnectedLink(portPath), None)
        }
      case port: wir.PortArray => port.getElaboratedPorts.foreach { case (childName, childPort) =>
        // Array contents are treated as top-level ports
        setPortConnectedLink(portPath + childName, childPort, linkPath)
      }
      case port => throw new NotImplementedError(s"unknown port $port")
    }
  }

  // TODO clean this up... by a lot
  def processBlocklikeConstraint: PartialFunction[(DesignPath, String, expr.ValueExpr, expr.ValueExpr.Expr), Unit] = {
    case (path, constrName, constr, expr.ValueExpr.Expr.Assign(assign)) =>
      constProp.addAssignment(
        path.asIndirect ++ assign.dst.get,
        path, assign.src.get,
        constrName) // TODO add sourcelocators
    case (path, constrName, constr,
        expr.ValueExpr.Expr.Binary(_) | expr.ValueExpr.Expr.BinarySet(_) |
        expr.ValueExpr.Expr.Unary(_) | expr.ValueExpr.Expr.UnarySet(_) |
        expr.ValueExpr.Expr.IfThenElse(_)) =>
      assertions += ((path, constrName, constr, SourceLocator.empty))  // TODO add source locators
    case (path, constrName, constr, expr.ValueExpr.Expr.Ref(target))
      if target.steps.last.step.isReservedParam
          && target.steps.last.getReservedParam == ref.Reserved.IS_CONNECTED =>
      assertions += ((path, constrName, constr, SourceLocator.empty))  // TODO add source locators
  }

  protected def processBlock(path: DesignPath, block: wir.Block): Unit = {
    import edg.ExprBuilder.{Ref, ValueExpr}
    import edgir.ref.ref
    constProp.setValue(path.asIndirect + IndirectStep.Name, TextValue(path.toString))

    // Elaborate ports, generating equivalence constraints as needed
    processParamDeclarations(path, block)
    for ((portName, port) <- block.getUnelaboratedPorts) {
      elaboratePort(path + portName, block, port)
    }
    for ((portName, port) <- block.getElaboratedPorts) {
      setPortNotConnected(path + portName, port)
    }

    // Find allocate ports and lower them before processing all constraints
    // link-side port array -> list of (constraint name, block port)
    val linkPortAllocates = mutable.HashMap[Seq[String], mutable.ListBuffer[(String, Seq[String])]]()
    block.getConstraints.foreach { case (constrName, constr) => constr.expr match {
      case expr.ValueExpr.Expr.Connected(connected) =>
        (connected.getBlockPort, connected.getLinkPort) match {
          case (ValueExpr.Ref(blockPort), ValueExpr.RefAllocate(linkPortArray)) =>
            linkPortAllocates.getOrElseUpdate(linkPortArray, mutable.ListBuffer()) += ((constrName, blockPort))
          case _ =>
        }
      case _ =>
    }}

    // For fully resolved arrays, allocate port numbers and set array elements
    linkPortAllocates.foreach { case (linkPortArray, blockConstrPorts) =>
      val linkPortArrayElts = blockConstrPorts.zipWithIndex.map { case ((constrName, blockPort), index) =>
        block.mapConstraint(constrName) { constr =>
          val steps = constr.getConnected.getLinkPort.getRef.steps
          require(steps.last == Ref.AllocateStep)
          val indexStep = ref.LocalStep(step=ref.LocalStep.Step.Name(index.toString))
          constr.update(
            _.connected.linkPort.ref.steps := steps.slice(0, steps.length - 1) :+ indexStep
          )
        }
        index.toString
      }.toSeq
      debug(s"Array defined: ${path ++ linkPortArray} = $linkPortArrayElts")
      constProp.setArrayElts(path ++ linkPortArray, linkPortArrayElts)
      constProp.setValue(path.asIndirect ++ linkPortArray + IndirectStep.Length,
        IntValue(linkPortArrayElts.length))
    }

    // Process constraints:
    // - for connected constraints, add into the connectivity map
    // - for assignment constraints, add into const prop
    // - for other constraints, add into asserts list
    // TODO ensure constraint processing order?
    // All ports that need to be allocated, with the list of connected ports,
    // as (port array path -> list(constraint name, block port))
    block.getConstraints.foreach { case (constrName, constr) => constr.expr match {
      case expr if processBlocklikeConstraint.isDefinedAt(path, constrName, constr, expr) =>
        processBlocklikeConstraint(path, constrName, constr, expr)
      case expr.ValueExpr.Expr.Connected(connected) =>
        (connected.getBlockPort, connected.getLinkPort) match {
          case (ValueExpr.Ref(blockPort), ValueExpr.Ref(linkPort)) =>
            elaboratePending.addNode(
              ElaborateRecord.Connect(path ++ linkPort, path ++ blockPort),
              Seq(ElaborateRecord.ConnectedLink(path ++ linkPort))
            )
            require(!portDirectlyConnected.contains(path ++ blockPort))
            portDirectlyConnected.put(path ++ blockPort, true)
            require(!portDirectlyConnected.contains(path ++ linkPort))
            portDirectlyConnected.put(path ++ linkPort, true)
          case (ValueExpr.Ref(blockPort), ValueExpr.RefAllocate(linkPortArray)) =>
            throw new Exception("This constraint should have been lowered")
          case (ValueExpr.RefAllocate(blockPortArray), ValueExpr.RefAllocate(linkPortArray)) =>
            throw new NotImplementedError(s"TODO: block port array <-> link port array: ${constr.expr}")
          case (ValueExpr.RefAllocate(blockPortArray), ValueExpr.Ref(linkPort)) =>
            throw new NotImplementedError(s"TODO: block port array <-> link port: ${constr.expr}")
          case _ => throw new IllegalConstraintException(s"unknown connect in block $path: $constrName = $connected")
        }
      case expr.ValueExpr.Expr.Exported(exported) =>
        (exported.getExteriorPort, exported.getInternalBlockPort) match {
          case (ValueExpr.Ref(extPort), ValueExpr.Ref(intPort)) =>
            elaboratePending.addNode(
              ElaborateRecord.Connect(path ++ extPort, path ++ intPort),
              Seq(ElaborateRecord.ConnectedLink(path ++ extPort))
            )
            // TODO: this allows exporting into exterior ports' inner ports. Is this clean?
            require(!portDirectlyConnected.contains(path ++ intPort))
            portDirectlyConnected.put(path ++ intPort, true)
          case (ValueExpr.RefAllocate(extPortArray), ValueExpr.RefAllocate(intPortArray)) =>
            throw new NotImplementedError(s"TODO: export port array <-> port array: ${constr.expr}")
          case (ValueExpr.RefAllocate(extPortArray), ValueExpr.Ref(intPort)) =>
            throw new NotImplementedError(s"TODO: export port array <-> port: ${constr.expr}")
          case (ValueExpr.Ref(extPort), ValueExpr.RefAllocate(intPortArray)) =>
            throw new NotImplementedError(s"TODO: export port <-> port array: ${constr.expr}")
          case _ => throw new IllegalConstraintException(s"unknown export in block $path: $constrName = $exported")
        }
      case _ => throw new IllegalConstraintException(s"unknown constraint in block $path: $constrName = $constr")
    }}

    // Queue up sub-trees that need elaboration - needs to be post-generate for generators
    // subtree ports can't know connected state until own connected state known
    for (blockName <- block.getUnelaboratedBlocks.keys) {
      debug(s"Push block to pending: ${path + blockName}")
      elaboratePending.addNode(ElaborateRecord.Block(path + blockName), Seq())
    }
    for (linkName <- block.getUnelaboratedLinks.keys) {
      debug(s"Push link to pending: ${path + linkName}")
      elaboratePending.addNode(ElaborateRecord.Link(path + linkName), Seq())
    }
  }

  /** Elaborate the unelaborated block at path (but where the parent has been elaborated and is reachable from root),
    * and adds it to the parent and replaces the lib_elem proto entry with a placeholder unknown.
    * Adds children to the pending queue, and adds constraints to constProp.
    * Expands connects in the parent, as needed.
    */
  protected def elaborateBlock(path: DesignPath): Unit = {
    // Instantiate block from library element to wir.Block
    val libraryPath = resolveBlock(path).asInstanceOf[wir.BlockLibrary].target

    val (refinedLibrary, unrefinedType) = refinements.instanceRefinements.get(path) match {
      case Some(refinement) => (refinement, Some(libraryPath))
      case None => refinements.classRefinements.get(libraryPath) match {
        case Some(refinement) => (refinement, Some(libraryPath))
        case None => (libraryPath, None)
      }
    }

    val blockPb = library.getBlock(refinedLibrary) match {
      case Errorable.Success(blockPb) =>
        if (unrefinedType.isDefined) {  // check refinement validity and add default params
          if (!library.isSubclassOf(refinedLibrary, libraryPath)) {
            errors += CompilerError.RefinementSubclassError(path, refinedLibrary, libraryPath)
          }
          library.getBlock(libraryPath) match {
            case Errorable.Success(unrefinedPb) =>
              val refinedNewParams = blockPb.params.keys.toSet -- unrefinedPb.params.keys
              refinedNewParams.foreach { refinedNewParam =>
                blockPb.paramDefaults.get(refinedNewParam) match {
                  case Some(refinedDefault) =>
                    constProp.addAssignment(path.asIndirect + refinedNewParam, path, refinedDefault,
                        s"(default)${refinedLibrary.toSimpleString}.$refinedNewParam")
                  case None =>  // ignored
                }
              }
            case Errorable.Error(err) =>  // TODO cleaner error handling
              import edgir.elem.elem
              errors += CompilerError.LibraryError(path, libraryPath, err)
              elem.HierarchyBlock()
          }
          blockPb
        } else {  // no default params
          blockPb
        }
      case Errorable.Error(err) =>
        import edgir.elem.elem
        errors += CompilerError.LibraryError(path, refinedLibrary, err)
        elem.HierarchyBlock()
    }

    // Populate class-based value refinements
    refinements.classValues.get(refinedLibrary) match {
      case Some(classValueRefinements) => for ((subpath, value) <- classValueRefinements) {
        constProp.setForcedValue(
          path.asIndirect ++ subpath, value,
          s"${refinedLibrary.getTarget.getName} class refinement")
      }
      case None =>
    }

    if (blockPb.generators.isEmpty) {  // non-generators: directly instantiate the block
      val block = new wir.Block(blockPb, unrefinedType)
      processBlock(path, block)
      if (path.steps.nonEmpty) {
        val (parentPath, name) = path.split
        val parent = resolveBlock(parentPath).asInstanceOf[wir.Block]
        parent.elaborate(name, block)  // link block in parent
      } else {
        root = block
      }
    } else {  // Generators: add to queue without changing the block
      require(blockPb.generators.size == 1)  // TODO proper single generator structure
      val (generatorFnName, generator) = blockPb.generators.head
      elaboratePending.addNode(ElaborateRecord.Generator(path, refinedLibrary, generatorFnName,
          unrefinedType, generator.requiredParams, generator.requiredPorts),
        generator.requiredParams.map { depPath =>
          ElaborateRecord.ParamValue(path.asIndirect ++ depPath)
        } ++ generator.requiredPorts.flatMap { depPort =>
            if (portDirectlyConnected.contains(path ++ depPort)) {
              Some(ElaborateRecord.ConnectedLink(path ++ depPort))
            } else {  // don't block on non-connected ports
              // TODO the disconnected logic is very spread around, this needs to be centralized
              None
            }
        }
      )
    }
  }

  // Elaborates the generator, replacing the block stub with the generated implementation.
  //
  protected def elaborateGenerator(generator: ElaborateRecord.Generator): Unit = {
    // Get required values for the generator
    val reqParamValues = generator.requiredParams.map { reqParam =>
      reqParam -> constProp.getValue(generator.blockPath.asIndirect ++ reqParam).get
    }.toMap

    val reqPortValues = generator.requiredPorts.flatMap { reqPort =>
      val isConnectedSuffix = PathSuffix() ++ reqPort + IndirectStep.IsConnected
      // TODO centralize not-connected logic
      if (portDirectlyConnected.contains(generator.blockPath ++ reqPort)) {
        val connectedNameSuffix = PathSuffix() ++ reqPort + IndirectStep.ConnectedLink + IndirectStep.Name
        Map(
          isConnectedSuffix -> BooleanValue(true),
          connectedNameSuffix -> constProp.getValue(generator.blockPath.asIndirect ++ connectedNameSuffix).get,
        )
      } else {
        Map(isConnectedSuffix -> BooleanValue(false))
      }
    }.map { case (param, value) =>
      param.asLocalPath() -> value
    }

    // Run generator and plug in
    val generatedPb = library.runGenerator(generator.blockClass, generator.fnName,
      reqParamValues ++ reqPortValues
    ) match {
      case Errorable.Success(generatedPb) =>
        if (generatedPb.getSelfClass != generator.blockClass) {
          errors += CompilerError.GeneratorError(generator.blockPath, generator.blockClass, generator.fnName,
            s"Generated class ${generatedPb.getSelfClass.toSimpleString} not equal to " +
                s"generator class ${generator.blockClass.toSimpleString}")
        }
        if (generatedPb.generators.nonEmpty) {
          errors += CompilerError.GeneratorError(generator.blockPath, generator.blockClass, generator.fnName,
            s"Generated ${generatedPb.getSelfClass.toSimpleString} still contains generators")
        }
        generatedPb
      case Errorable.Error(err) =>
        import edgir.elem.elem
        errors += CompilerError.GeneratorError(generator.blockPath, generator.blockClass, generator.fnName, err)
        elem.HierarchyBlock()
    }
    val block = new wir.Block(generatedPb, generator.unrefinedClass)
    processBlock(generator.blockPath, block)

    // Link block in parent
    if (generator.blockPath.steps.nonEmpty) {
      val (parentPath, name) = generator.blockPath.split
      val parent = resolveBlock(parentPath).asInstanceOf[wir.Block]
      parent.elaborate(name, block)
    } else {
      root = block
    }
  }

  protected def processLink(path: DesignPath, link: wir.Link): Unit = {
    import edg.ExprBuilder.{Ref, ValueExpr}

    // Set my parameters in the global data structure
    constProp.setValue(path.asIndirect + IndirectStep.Name, TextValue(path.toString))
    val allParams = link.getParams.keys.toSeq.map(IndirectStep.Element(_)) :+ IndirectStep.Name
    linkParams.put(path, allParams)

    // Elaborate ports, generating equivalence constraints as needed
    processParamDeclarations(path, link)
    for ((portName, port) <- link.getUnelaboratedPorts) {
      elaboratePort(path + portName, link, port)
    }
    for ((portName, port) <- link.getElaboratedPorts) {
      setPortConnectedLink(path + portName, port, path)
      setPortNotConnected(path + portName, port)
    }

    // Find allocate ports and lower them before processing all constraints
    // path to inner link port array -> list of array elements
    val intPortArrayEltss = mutable.HashMap[Seq[String], mutable.ListBuffer[String]]()
    link.getConstraints.view.mapValues(_.expr).collect {  // extract exported constraints only
      case (constrName, expr.ValueExpr.Expr.Exported(exported)) =>
        (constrName, exported.getExteriorPort, exported.getInternalBlockPort)
    }.collect {  // extract array ones that need lowering, into (name, external ports, internal array)
      case (constrName, ValueExpr.MapExtract(ValueExpr.Ref(extPortArray), Ref(extPortInner)),
      ValueExpr.RefAllocate(intPortArray)) =>  // array-array connect
        val extPorts = constProp.getArrayElts(path ++ extPortArray).get.map { extArrayElt =>
          (extPortArray :+ extArrayElt) ++ extPortInner }
        (constrName, extPorts, intPortArray)
      case (constrName, ValueExpr.Ref(extPort), ValueExpr.RefAllocate(intPortArray)) =>  // element-array connect
        val extPorts = Seq(extPort)
        (constrName, extPorts, intPortArray)
    }.foreach { case (constrName, extPorts, intPortArray) =>  // expand the connections
      link.mapMultiConstraint(constrName) { constr =>
        val intPortArrayElts = intPortArrayEltss.getOrElseUpdate(intPortArray, mutable.ListBuffer())
        val startIndex = intPortArrayElts.length
        extPorts.zipWithIndex.map { case (extPort, extPortIndex) =>
          val intPortIndex = (startIndex + extPortIndex).toString
          intPortArrayElts.append(intPortIndex)

          val newConstrName = extPorts.length match {
            case 1 => constrName // constraint doesn't expand
            case _ => constrName + "." + extPortIndex // expands into multiple constraints, each needs a unique name
          }
          val newConstr = constr.update(
            _.exported.exteriorPort.ref.steps := extPort.map { pathElt =>
              ref.LocalStep(ref.LocalStep.Step.Name(pathElt))
            },
            _.exported.internalBlockPort.ref.steps := (intPortArray :+ intPortIndex).map { pathElt =>
              ref.LocalStep(ref.LocalStep.Step.Name(pathElt))
            },
          )

          newConstrName -> newConstr
        }
      }
    }

    // Actually define arrays
    intPortArrayEltss.foreach { case (intPortArray, intPortArrayElts) =>
      debug(s"Array defined: ${path ++ intPortArray} = $intPortArrayElts")
      constProp.setArrayElts(path ++ intPortArray, intPortArrayElts.toSeq)
      constProp.setValue(path.asIndirect ++ intPortArray + IndirectStep.Length, IntValue(intPortArrayElts.length))
    }

    // Process constraints, as in the block case
    link.getConstraints.foreach { case (constrName, constr) => constr.expr match {
      case expr if processBlocklikeConstraint.isDefinedAt(path, constrName, constr, expr) =>
        processBlocklikeConstraint(path, constrName, constr, expr)
      case expr.ValueExpr.Expr.Exported(exported) =>
        (exported.getExteriorPort, exported.getInternalBlockPort) match {
          case (ValueExpr.Ref(extPort), ValueExpr.Ref(intPort)) =>
            elaboratePending.addNode(
              ElaborateRecord.Connect(path ++ intPort, path ++ extPort),
              Seq(ElaborateRecord.ConnectedLink(path ++ intPort))
            )
            require(!portDirectlyConnected.contains(path ++ intPort))
            if (portDirectlyConnected(path ++ extPort)) {  // unlike Blocks, inner links inherit connectedness
              portDirectlyConnected.put(path ++ intPort, true)
            }
          case _ => throw new IllegalConstraintException(s"unknown export in link $path: $constrName = $exported")
        }
      case _ => throw new IllegalConstraintException(s"unknown constraint in link $path: $constrName = $constr")
    }}

    // Queue up sub-trees that need elaboration - needs to be post-generate for generators
    for (linkName <- link.getUnelaboratedLinks.keys) {
      debug(s"Push link to pending: ${path + linkName}")
      elaboratePending.addNode(ElaborateRecord.Link(path + linkName), Seq())
    }
  }

  /** Elaborate the unelaborated link at path (but where the parent has been elaborated and is reachable from root),
    * and adds it to the parent and replaces the lib_elem proto entry with a placeholder unknown.
    * Adds children to the pending queue, and adds constraints to constProp.
    * Expands connects in the parent, as needed.
    */
  protected def elaborateLink(path: DesignPath): Unit = {
    val (parentPath, name) = path.split

    // Instantiate block from library element to wir.Block
    val parent = resolve(parentPath).asInstanceOf[wir.HasMutableLinks]
    val libraryPath = parent.getUnelaboratedLinks(name).asInstanceOf[wir.LinkLibrary].target

    val linkPb = library.getLink(libraryPath) match {
      case Errorable.Success(linkPb) => linkPb
      case Errorable.Error(err) =>
        import edgir.elem.elem
        errors += CompilerError.LibraryError(path, libraryPath, err)
        elem.Link()
    }
    val link = new wir.Link(linkPb)

    // Process block
    processLink(path, link)

    // Link block in parent
    parent.elaborate(name, link)
  }


  /** Performs full compilation and returns the resulting design. Might take a while.
    */
  def compile(): schema.Design = {
    import edg.ElemBuilder

    // We don't use the usual elaboration flow for the root block because it has no parent and breaks the flow
    // TODO unify with BlockLike in Design
    val rootPb = root.toPb.getHierarchy
    require(rootPb.generators.isEmpty, "root generators not supported")
    processBlock(DesignPath(), root)

    // Ports at top break IS_CONNECTED implies CONNECTED_LINK has valid params
    require(root.getElaboratedPorts.isEmpty, "design top may not have ports")

    while (elaboratePending.getReady.nonEmpty) {
      elaboratePending.getReady.foreach { elaborateRecord =>
        onElaborate(elaborateRecord)
        elaborateRecord match {
          case elaborateRecord@ElaborateRecord.Block(blockPath) =>
            debug(s"Elaborate block @ $blockPath")
            elaborateBlock(blockPath)
            elaboratePending.setValue(elaborateRecord, None)
          case elaborateRecord@ElaborateRecord.Link(linkPath) =>
            debug(s"Elaborate link @ $linkPath")
            elaborateLink(linkPath)
            elaboratePending.setValue(elaborateRecord, None)
          case elaborateRecord@ElaborateRecord.Connect(toLinkPortPath, fromLinkPortPath) =>
            debug(s"Elaborate connect $toLinkPortPath <-> $fromLinkPortPath")
            elaborateConnect(toLinkPortPath, fromLinkPortPath)
            elaboratePending.setValue(elaborateRecord, None)
          case generator: ElaborateRecord.Generator =>
            debug(s"Elaborate generator '${generator.fnName}' @ ${generator.blockPath}")
            elaborateGenerator(generator)
            elaboratePending.setValue(generator, None)
          case _: ElaborateRecord.ElaborateDependency =>
            throw new IllegalArgumentException(s"can't elaborate dependency-only record $elaborateRecord")
        }
      }
    }

    ElemBuilder.Design(root.toPb)
  }

  def evaluateExpr(root: DesignPath, value: expr.ValueExpr): ExprResult = {
    new ExprEvaluatePartial(constProp, root).map(value)
  }

  def getParamValue(param: IndirectDesignPath): Option[ExprValue] = constProp.getValue(param)
  def getAllSolved: Map[IndirectDesignPath, ExprValue] = constProp.getAllSolved
  def getConnectedLink(port: DesignPath): Option[DesignPath] = connectedLink.get(port)
}
