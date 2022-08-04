# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edgir/elem.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgir import common_pb2 as edgir_dot_common__pb2
from edgir import init_pb2 as edgir_dot_init__pb2
from edgir import expr_pb2 as edgir_dot_expr__pb2
from edgir import ref_pb2 as edgir_dot_ref__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x65\x64gir/elem.proto\x12\nedgir.elem\x1a\x12\x65\x64gir/common.proto\x1a\x10\x65\x64gir/init.proto\x1a\x10\x65\x64gir/expr.proto\x1a\x0f\x65\x64gir/ref.proto\"\xfb\x02\n\x04Port\x12,\n\x06params\x18\n \x03(\x0b\x32\x1c.edgir.elem.Port.ParamsEntry\x12\x36\n\x0b\x63onstraints\x18\x0b \x03(\x0b\x32!.edgir.elem.Port.ConstraintsEntry\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x15 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\"\xf3\x03\n\x06\x42undle\x12.\n\x06params\x18\n \x03(\x0b\x32\x1e.edgir.elem.Bundle.ParamsEntry\x12,\n\x05ports\x18\x0b \x03(\x0b\x32\x1d.edgir.elem.Bundle.PortsEntry\x12\x38\n\x0b\x63onstraints\x18\x0c \x03(\x0b\x32#.edgir.elem.Bundle.ConstraintsEntry\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x15 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\"\x9c\x02\n\tPortArray\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x05ports\x18\x0e \x01(\x0b\x32\x1b.edgir.elem.PortArray.PortsH\x00\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x82\x01\n\x05Ports\x12\x35\n\x05ports\x18\n \x03(\x0b\x32&.edgir.elem.PortArray.Ports.PortsEntry\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x42\n\n\x08\x63ontains\"\xd6\x01\n\x08PortLike\x12(\n\tundefined\x18\x01 \x01(\x0b\x32\x13.edgir.common.EmptyH\x00\x12*\n\x08lib_elem\x18\x02 \x01(\x0b\x32\x16.edgir.ref.LibraryPathH\x00\x12 \n\x04port\x18\x03 \x01(\x0b\x32\x10.edgir.elem.PortH\x00\x12&\n\x05\x61rray\x18\x04 \x01(\x0b\x32\x15.edgir.elem.PortArrayH\x00\x12$\n\x06\x62undle\x18\x06 \x01(\x0b\x32\x12.edgir.elem.BundleH\x00\x42\x04\n\x02is\"=\n\tParameter\x12\"\n\x04path\x18\x01 \x01(\x0b\x32\x14.edgir.ref.LocalPath\x12\x0c\n\x04unit\x18\x02 \x01(\t\"a\n\x18StringDescriptionElement\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12&\n\x05param\x18\x02 \x01(\x0b\x32\x15.edgir.elem.ParameterH\x00\x42\r\n\x0b\x45lementType\"\xca\x08\n\x0eHierarchyBlock\x12\x36\n\x06params\x18\n \x03(\x0b\x32&.edgir.elem.HierarchyBlock.ParamsEntry\x12\x45\n\x0eparam_defaults\x18\x0f \x03(\x0b\x32-.edgir.elem.HierarchyBlock.ParamDefaultsEntry\x12\x34\n\x05ports\x18\x0b \x03(\x0b\x32%.edgir.elem.HierarchyBlock.PortsEntry\x12\x36\n\x06\x62locks\x18\x0c \x03(\x0b\x32&.edgir.elem.HierarchyBlock.BlocksEntry\x12\x34\n\x05links\x18\r \x03(\x0b\x32%.edgir.elem.HierarchyBlock.LinksEntry\x12@\n\x0b\x63onstraints\x18\x0e \x03(\x0b\x32+.edgir.elem.HierarchyBlock.ConstraintsEntry\x12*\n\nself_class\x18\x17 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x14 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12/\n\x0fprerefine_class\x18\x15 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12(\n\tgenerator\x18\x16 \x01(\x0b\x32\x15.edgir.elem.Generator\x12\x13\n\x0bis_abstract\x18\x1e \x01(\x08\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x12\x39\n\x0b\x64\x65scription\x18\x01 \x03(\x0b\x32$.edgir.elem.StringDescriptionElement\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1aK\n\x12ParamDefaultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1a\x44\n\x0b\x42locksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.elem.BlockLike:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.LinkLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\":\n\tGenerator\x12-\n\x0frequired_params\x18\x02 \x03(\x0b\x32\x14.edgir.ref.LocalPath\"\x9a\x01\n\tBlockLike\x12(\n\tundefined\x18\x01 \x01(\x0b\x32\x13.edgir.common.EmptyH\x00\x12*\n\x08lib_elem\x18\x02 \x01(\x0b\x32\x16.edgir.ref.LibraryPathH\x00\x12/\n\thierarchy\x18\x04 \x01(\x0b\x32\x1a.edgir.elem.HierarchyBlockH\x00\x42\x06\n\x04type\"\x96\x05\n\x04Link\x12,\n\x06params\x18\n \x03(\x0b\x32\x1c.edgir.elem.Link.ParamsEntry\x12*\n\x05ports\x18\x0b \x03(\x0b\x32\x1b.edgir.elem.Link.PortsEntry\x12*\n\x05links\x18\r \x03(\x0b\x32\x1b.edgir.elem.Link.LinksEntry\x12\x36\n\x0b\x63onstraints\x18\x0c \x03(\x0b\x32!.edgir.elem.Link.ConstraintsEntry\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x15 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x12\x39\n\x0b\x64\x65scription\x18\x01 \x03(\x0b\x32$.edgir.elem.StringDescriptionElement\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.LinkLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\"\xcf\x03\n\tLinkArray\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12/\n\x05ports\x18\x0b \x03(\x0b\x32 .edgir.elem.LinkArray.PortsEntry\x12;\n\x0b\x63onstraints\x18\x0c \x03(\x0b\x32&.edgir.elem.LinkArray.ConstraintsEntry\x12/\n\x05links\x18\r \x03(\x0b\x32 .edgir.elem.LinkArray.LinksEntry\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.LinkLike:\x02\x38\x01\"\xb2\x01\n\x08LinkLike\x12(\n\tundefined\x18\x01 \x01(\x0b\x32\x13.edgir.common.EmptyH\x00\x12*\n\x08lib_elem\x18\x02 \x01(\x0b\x32\x16.edgir.ref.LibraryPathH\x00\x12 \n\x04link\x18\x03 \x01(\x0b\x32\x10.edgir.elem.LinkH\x00\x12&\n\x05\x61rray\x18\x04 \x01(\x0b\x32\x15.edgir.elem.LinkArrayH\x00\x42\x06\n\x04typeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'edgir.elem_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PORT_PARAMSENTRY._options = None
  _PORT_PARAMSENTRY._serialized_options = b'8\001'
  _PORT_CONSTRAINTSENTRY._options = None
  _PORT_CONSTRAINTSENTRY._serialized_options = b'8\001'
  _BUNDLE_PARAMSENTRY._options = None
  _BUNDLE_PARAMSENTRY._serialized_options = b'8\001'
  _BUNDLE_PORTSENTRY._options = None
  _BUNDLE_PORTSENTRY._serialized_options = b'8\001'
  _BUNDLE_CONSTRAINTSENTRY._options = None
  _BUNDLE_CONSTRAINTSENTRY._serialized_options = b'8\001'
  _PORTARRAY_PORTS_PORTSENTRY._options = None
  _PORTARRAY_PORTS_PORTSENTRY._serialized_options = b'8\001'
  _HIERARCHYBLOCK_PARAMSENTRY._options = None
  _HIERARCHYBLOCK_PARAMSENTRY._serialized_options = b'8\001'
  _HIERARCHYBLOCK_PARAMDEFAULTSENTRY._options = None
  _HIERARCHYBLOCK_PARAMDEFAULTSENTRY._serialized_options = b'8\001'
  _HIERARCHYBLOCK_PORTSENTRY._options = None
  _HIERARCHYBLOCK_PORTSENTRY._serialized_options = b'8\001'
  _HIERARCHYBLOCK_BLOCKSENTRY._options = None
  _HIERARCHYBLOCK_BLOCKSENTRY._serialized_options = b'8\001'
  _HIERARCHYBLOCK_LINKSENTRY._options = None
  _HIERARCHYBLOCK_LINKSENTRY._serialized_options = b'8\001'
  _HIERARCHYBLOCK_CONSTRAINTSENTRY._options = None
  _HIERARCHYBLOCK_CONSTRAINTSENTRY._serialized_options = b'8\001'
  _LINK_PARAMSENTRY._options = None
  _LINK_PARAMSENTRY._serialized_options = b'8\001'
  _LINK_PORTSENTRY._options = None
  _LINK_PORTSENTRY._serialized_options = b'8\001'
  _LINK_LINKSENTRY._options = None
  _LINK_LINKSENTRY._serialized_options = b'8\001'
  _LINK_CONSTRAINTSENTRY._options = None
  _LINK_CONSTRAINTSENTRY._serialized_options = b'8\001'
  _LINKARRAY_PORTSENTRY._options = None
  _LINKARRAY_PORTSENTRY._serialized_options = b'8\001'
  _LINKARRAY_CONSTRAINTSENTRY._options = None
  _LINKARRAY_CONSTRAINTSENTRY._serialized_options = b'8\001'
  _LINKARRAY_LINKSENTRY._options = None
  _LINKARRAY_LINKSENTRY._serialized_options = b'8\001'
  _PORT._serialized_start=106
  _PORT._serialized_end=485
  _PORT_PARAMSENTRY._serialized_start=344
  _PORT_PARAMSENTRY._serialized_end=410
  _PORT_CONSTRAINTSENTRY._serialized_start=412
  _PORT_CONSTRAINTSENTRY._serialized_end=485
  _BUNDLE._serialized_start=488
  _BUNDLE._serialized_end=987
  _BUNDLE_PARAMSENTRY._serialized_start=344
  _BUNDLE_PARAMSENTRY._serialized_end=410
  _BUNDLE_PORTSENTRY._serialized_start=846
  _BUNDLE_PORTSENTRY._serialized_end=912
  _BUNDLE_CONSTRAINTSENTRY._serialized_start=412
  _BUNDLE_CONSTRAINTSENTRY._serialized_end=485
  _PORTARRAY._serialized_start=990
  _PORTARRAY._serialized_end=1274
  _PORTARRAY_PORTS._serialized_start=1132
  _PORTARRAY_PORTS._serialized_end=1262
  _PORTARRAY_PORTS_PORTSENTRY._serialized_start=846
  _PORTARRAY_PORTS_PORTSENTRY._serialized_end=912
  _PORTLIKE._serialized_start=1277
  _PORTLIKE._serialized_end=1491
  _PARAMETER._serialized_start=1493
  _PARAMETER._serialized_end=1554
  _STRINGDESCRIPTIONELEMENT._serialized_start=1556
  _STRINGDESCRIPTIONELEMENT._serialized_end=1653
  _HIERARCHYBLOCK._serialized_start=1656
  _HIERARCHYBLOCK._serialized_end=2754
  _HIERARCHYBLOCK_PARAMSENTRY._serialized_start=344
  _HIERARCHYBLOCK_PARAMSENTRY._serialized_end=410
  _HIERARCHYBLOCK_PARAMDEFAULTSENTRY._serialized_start=2398
  _HIERARCHYBLOCK_PARAMDEFAULTSENTRY._serialized_end=2473
  _HIERARCHYBLOCK_PORTSENTRY._serialized_start=846
  _HIERARCHYBLOCK_PORTSENTRY._serialized_end=912
  _HIERARCHYBLOCK_BLOCKSENTRY._serialized_start=2543
  _HIERARCHYBLOCK_BLOCKSENTRY._serialized_end=2611
  _HIERARCHYBLOCK_LINKSENTRY._serialized_start=2613
  _HIERARCHYBLOCK_LINKSENTRY._serialized_end=2679
  _HIERARCHYBLOCK_CONSTRAINTSENTRY._serialized_start=412
  _HIERARCHYBLOCK_CONSTRAINTSENTRY._serialized_end=485
  _GENERATOR._serialized_start=2756
  _GENERATOR._serialized_end=2814
  _BLOCKLIKE._serialized_start=2817
  _BLOCKLIKE._serialized_end=2971
  _LINK._serialized_start=2974
  _LINK._serialized_end=3636
  _LINK_PARAMSENTRY._serialized_start=344
  _LINK_PARAMSENTRY._serialized_end=410
  _LINK_PORTSENTRY._serialized_start=846
  _LINK_PORTSENTRY._serialized_end=912
  _LINK_LINKSENTRY._serialized_start=2613
  _LINK_LINKSENTRY._serialized_end=2679
  _LINK_CONSTRAINTSENTRY._serialized_start=412
  _LINK_CONSTRAINTSENTRY._serialized_end=485
  _LINKARRAY._serialized_start=3639
  _LINKARRAY._serialized_end=4102
  _LINKARRAY_PORTSENTRY._serialized_start=846
  _LINKARRAY_PORTSENTRY._serialized_end=912
  _LINKARRAY_CONSTRAINTSENTRY._serialized_start=412
  _LINKARRAY_CONSTRAINTSENTRY._serialized_end=485
  _LINKARRAY_LINKSENTRY._serialized_start=2613
  _LINKARRAY_LINKSENTRY._serialized_end=2679
  _LINKLIKE._serialized_start=4105
  _LINKLIKE._serialized_end=4283
# @@protoc_insertion_point(module_scope)
