from typing import Optional, Any, Type

import os
import grpc  # type: ignore
from concurrent import futures
import subprocess

from . import edgir, edgrpc
from .Core import builder
from .HierarchyBlock import Block
from .HdlInterfaceServer import HdlInterface, CachedLibrary


class ScalaCompilerInstance:
  RELATIVE_PATH = "compiler/target/scala-2.13/edg-compiler-assembly-0.1-SNAPSHOT.jar"

  def __init__(self):
    self.server: Optional[Any] = None

    self.process: Optional[Any] = None
    self.channel: Optional[Any] = None
    self.stub: Optional[Any] = None

    self.library = CachedLibrary()  # TODO should this be instance-specific?

  def check_started(self) -> None:
    if self.server is None:
      self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
      edgrpc.add_HdlInterfaceServicer_to_server(HdlInterface(self.library), self.server)  # type: ignore
      self.server.add_insecure_port('[::]:50051')
      self.server.start()

    if self.stub is None:
      if os.path.exists(self.RELATIVE_PATH):
        jar_path = self.RELATIVE_PATH
        print("Using development JAR")
      else:
        raise ValueError("No EDG Compiler JAR found")
      self.process = subprocess.Popen(
        ['java', '-jar', jar_path],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

      self.channel = grpc.insecure_channel('localhost:50052')
      self.stub = edgrpc.CompilerStub(self.channel)


  def compile(self, block: Type[Block]) -> edgrpc.CompilerResult:
    self.check_started()
    assert self.stub is not None

    result: edgrpc.CompilerResult = self.stub.Compile(edgrpc.CompilerRequest(
      modules=[block.__module__],
      design=edgir.Design(
        contents=builder.elaborate_toplevel(block(), f"in elaborating top design block {block}"))
    ))
    assert not result.error, f"error during compilation: \n{result.error}"
    return result

  def close(self):
    assert self.server is not None
    self.server.stop()
    self.server.wait_for_termination()  # is this needed?
    self.server = None


ScalaCompiler = ScalaCompilerInstance()