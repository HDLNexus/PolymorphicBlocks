# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edgir/elem.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgir import common_pb2 as edgir_dot_common__pb2
from edgir import init_pb2 as edgir_dot_init__pb2
from edgir import expr_pb2 as edgir_dot_expr__pb2
from edgir import ref_pb2 as edgir_dot_ref__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x65\x64gir/elem.proto\x12\nedgir.elem\x1a\x12\x65\x64gir/common.proto\x1a\x10\x65\x64gir/init.proto\x1a\x10\x65\x64gir/expr.proto\x1a\x0f\x65\x64gir/ref.proto\"\xfb\x02\n\x04Port\x12,\n\x06params\x18\n \x03(\x0b\x32\x1c.edgir.elem.Port.ParamsEntry\x12\x36\n\x0b\x63onstraints\x18\x0b \x03(\x0b\x32!.edgir.elem.Port.ConstraintsEntry\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x15 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\"\xf3\x03\n\x06\x42undle\x12.\n\x06params\x18\n \x03(\x0b\x32\x1e.edgir.elem.Bundle.ParamsEntry\x12,\n\x05ports\x18\x0b \x03(\x0b\x32\x1d.edgir.elem.Bundle.PortsEntry\x12\x38\n\x0b\x63onstraints\x18\x0c \x03(\x0b\x32#.edgir.elem.Bundle.ConstraintsEntry\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x15 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\"\x9c\x02\n\tPortArray\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x05ports\x18\x0e \x01(\x0b\x32\x1b.edgir.elem.PortArray.PortsH\x00\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x82\x01\n\x05Ports\x12\x35\n\x05ports\x18\n \x03(\x0b\x32&.edgir.elem.PortArray.Ports.PortsEntry\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x42\n\n\x08\x63ontains\"\xd6\x01\n\x08PortLike\x12(\n\tundefined\x18\x01 \x01(\x0b\x32\x13.edgir.common.EmptyH\x00\x12*\n\x08lib_elem\x18\x02 \x01(\x0b\x32\x16.edgir.ref.LibraryPathH\x00\x12 \n\x04port\x18\x03 \x01(\x0b\x32\x10.edgir.elem.PortH\x00\x12&\n\x05\x61rray\x18\x04 \x01(\x0b\x32\x15.edgir.elem.PortArrayH\x00\x12$\n\x06\x62undle\x18\x06 \x01(\x0b\x32\x12.edgir.elem.BundleH\x00\x42\x04\n\x02is\"\x8f\x08\n\x0eHierarchyBlock\x12\x36\n\x06params\x18\n \x03(\x0b\x32&.edgir.elem.HierarchyBlock.ParamsEntry\x12\x45\n\x0eparam_defaults\x18\x0f \x03(\x0b\x32-.edgir.elem.HierarchyBlock.ParamDefaultsEntry\x12\x34\n\x05ports\x18\x0b \x03(\x0b\x32%.edgir.elem.HierarchyBlock.PortsEntry\x12\x36\n\x06\x62locks\x18\x0c \x03(\x0b\x32&.edgir.elem.HierarchyBlock.BlocksEntry\x12\x34\n\x05links\x18\r \x03(\x0b\x32%.edgir.elem.HierarchyBlock.LinksEntry\x12@\n\x0b\x63onstraints\x18\x0e \x03(\x0b\x32+.edgir.elem.HierarchyBlock.ConstraintsEntry\x12*\n\nself_class\x18\x17 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x14 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12/\n\x0fprerefine_class\x18\x15 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12(\n\tgenerator\x18\x16 \x01(\x0b\x32\x15.edgir.elem.Generator\x12\x13\n\x0bis_abstract\x18\x1e \x01(\x08\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1aK\n\x12ParamDefaultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1a\x44\n\x0b\x42locksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.elem.BlockLike:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.LinkLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\":\n\tGenerator\x12-\n\x0frequired_params\x18\x02 \x03(\x0b\x32\x14.edgir.ref.LocalPath\"\x9a\x01\n\tBlockLike\x12(\n\tundefined\x18\x01 \x01(\x0b\x32\x13.edgir.common.EmptyH\x00\x12*\n\x08lib_elem\x18\x02 \x01(\x0b\x32\x16.edgir.ref.LibraryPathH\x00\x12/\n\thierarchy\x18\x04 \x01(\x0b\x32\x1a.edgir.elem.HierarchyBlockH\x00\x42\x06\n\x04type\"\xdb\x04\n\x04Link\x12,\n\x06params\x18\n \x03(\x0b\x32\x1c.edgir.elem.Link.ParamsEntry\x12*\n\x05ports\x18\x0b \x03(\x0b\x32\x1b.edgir.elem.Link.PortsEntry\x12*\n\x05links\x18\r \x03(\x0b\x32\x1b.edgir.elem.Link.LinksEntry\x12\x36\n\x0b\x63onstraints\x18\x0c \x03(\x0b\x32!.edgir.elem.Link.ConstraintsEntry\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12,\n\x0csuperclasses\x18\x15 \x03(\x0b\x32\x16.edgir.ref.LibraryPath\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.edgir.init.ValInit:\x02\x38\x01\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.LinkLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\"\xcf\x03\n\tLinkArray\x12*\n\nself_class\x18\x14 \x01(\x0b\x32\x16.edgir.ref.LibraryPath\x12/\n\x05ports\x18\x0b \x03(\x0b\x32 .edgir.elem.LinkArray.PortsEntry\x12;\n\x0b\x63onstraints\x18\x0c \x03(\x0b\x32&.edgir.elem.LinkArray.ConstraintsEntry\x12/\n\x05links\x18\r \x03(\x0b\x32 .edgir.elem.LinkArray.LinksEntry\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\x42\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.PortLike:\x02\x38\x01\x1aI\n\x10\x43onstraintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.edgir.expr.ValueExpr:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.edgir.elem.LinkLike:\x02\x38\x01\"\xb2\x01\n\x08LinkLike\x12(\n\tundefined\x18\x01 \x01(\x0b\x32\x13.edgir.common.EmptyH\x00\x12*\n\x08lib_elem\x18\x02 \x01(\x0b\x32\x16.edgir.ref.LibraryPathH\x00\x12 \n\x04link\x18\x03 \x01(\x0b\x32\x10.edgir.elem.LinkH\x00\x12&\n\x05\x61rray\x18\x04 \x01(\x0b\x32\x15.edgir.elem.LinkArrayH\x00\x42\x06\n\x04typeb\x06proto3')



_PORT = DESCRIPTOR.message_types_by_name['Port']
_PORT_PARAMSENTRY = _PORT.nested_types_by_name['ParamsEntry']
_PORT_CONSTRAINTSENTRY = _PORT.nested_types_by_name['ConstraintsEntry']
_BUNDLE = DESCRIPTOR.message_types_by_name['Bundle']
_BUNDLE_PARAMSENTRY = _BUNDLE.nested_types_by_name['ParamsEntry']
_BUNDLE_PORTSENTRY = _BUNDLE.nested_types_by_name['PortsEntry']
_BUNDLE_CONSTRAINTSENTRY = _BUNDLE.nested_types_by_name['ConstraintsEntry']
_PORTARRAY = DESCRIPTOR.message_types_by_name['PortArray']
_PORTARRAY_PORTS = _PORTARRAY.nested_types_by_name['Ports']
_PORTARRAY_PORTS_PORTSENTRY = _PORTARRAY_PORTS.nested_types_by_name['PortsEntry']
_PORTLIKE = DESCRIPTOR.message_types_by_name['PortLike']
_HIERARCHYBLOCK = DESCRIPTOR.message_types_by_name['HierarchyBlock']
_HIERARCHYBLOCK_PARAMSENTRY = _HIERARCHYBLOCK.nested_types_by_name['ParamsEntry']
_HIERARCHYBLOCK_PARAMDEFAULTSENTRY = _HIERARCHYBLOCK.nested_types_by_name['ParamDefaultsEntry']
_HIERARCHYBLOCK_PORTSENTRY = _HIERARCHYBLOCK.nested_types_by_name['PortsEntry']
_HIERARCHYBLOCK_BLOCKSENTRY = _HIERARCHYBLOCK.nested_types_by_name['BlocksEntry']
_HIERARCHYBLOCK_LINKSENTRY = _HIERARCHYBLOCK.nested_types_by_name['LinksEntry']
_HIERARCHYBLOCK_CONSTRAINTSENTRY = _HIERARCHYBLOCK.nested_types_by_name['ConstraintsEntry']
_GENERATOR = DESCRIPTOR.message_types_by_name['Generator']
_BLOCKLIKE = DESCRIPTOR.message_types_by_name['BlockLike']
_LINK = DESCRIPTOR.message_types_by_name['Link']
_LINK_PARAMSENTRY = _LINK.nested_types_by_name['ParamsEntry']
_LINK_PORTSENTRY = _LINK.nested_types_by_name['PortsEntry']
_LINK_LINKSENTRY = _LINK.nested_types_by_name['LinksEntry']
_LINK_CONSTRAINTSENTRY = _LINK.nested_types_by_name['ConstraintsEntry']
_LINKARRAY = DESCRIPTOR.message_types_by_name['LinkArray']
_LINKARRAY_PORTSENTRY = _LINKARRAY.nested_types_by_name['PortsEntry']
_LINKARRAY_CONSTRAINTSENTRY = _LINKARRAY.nested_types_by_name['ConstraintsEntry']
_LINKARRAY_LINKSENTRY = _LINKARRAY.nested_types_by_name['LinksEntry']
_LINKLIKE = DESCRIPTOR.message_types_by_name['LinkLike']
Port = _reflection.GeneratedProtocolMessageType('Port', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PORT_PARAMSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Port.ParamsEntry)
    })
  ,

  'ConstraintsEntry' : _reflection.GeneratedProtocolMessageType('ConstraintsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PORT_CONSTRAINTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Port.ConstraintsEntry)
    })
  ,
  'DESCRIPTOR' : _PORT,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.Port)
  })
_sym_db.RegisterMessage(Port)
_sym_db.RegisterMessage(Port.ParamsEntry)
_sym_db.RegisterMessage(Port.ConstraintsEntry)

Bundle = _reflection.GeneratedProtocolMessageType('Bundle', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BUNDLE_PARAMSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Bundle.ParamsEntry)
    })
  ,

  'PortsEntry' : _reflection.GeneratedProtocolMessageType('PortsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BUNDLE_PORTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Bundle.PortsEntry)
    })
  ,

  'ConstraintsEntry' : _reflection.GeneratedProtocolMessageType('ConstraintsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BUNDLE_CONSTRAINTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Bundle.ConstraintsEntry)
    })
  ,
  'DESCRIPTOR' : _BUNDLE,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.Bundle)
  })
_sym_db.RegisterMessage(Bundle)
_sym_db.RegisterMessage(Bundle.ParamsEntry)
_sym_db.RegisterMessage(Bundle.PortsEntry)
_sym_db.RegisterMessage(Bundle.ConstraintsEntry)

PortArray = _reflection.GeneratedProtocolMessageType('PortArray', (_message.Message,), {

  'Ports' : _reflection.GeneratedProtocolMessageType('Ports', (_message.Message,), {

    'PortsEntry' : _reflection.GeneratedProtocolMessageType('PortsEntry', (_message.Message,), {
      'DESCRIPTOR' : _PORTARRAY_PORTS_PORTSENTRY,
      '__module__' : 'edgir.elem_pb2'
      # @@protoc_insertion_point(class_scope:edgir.elem.PortArray.Ports.PortsEntry)
      })
    ,
    'DESCRIPTOR' : _PORTARRAY_PORTS,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.PortArray.Ports)
    })
  ,
  'DESCRIPTOR' : _PORTARRAY,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.PortArray)
  })
_sym_db.RegisterMessage(PortArray)
_sym_db.RegisterMessage(PortArray.Ports)
_sym_db.RegisterMessage(PortArray.Ports.PortsEntry)

PortLike = _reflection.GeneratedProtocolMessageType('PortLike', (_message.Message,), {
  'DESCRIPTOR' : _PORTLIKE,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.PortLike)
  })
_sym_db.RegisterMessage(PortLike)

HierarchyBlock = _reflection.GeneratedProtocolMessageType('HierarchyBlock', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HIERARCHYBLOCK_PARAMSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.HierarchyBlock.ParamsEntry)
    })
  ,

  'ParamDefaultsEntry' : _reflection.GeneratedProtocolMessageType('ParamDefaultsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HIERARCHYBLOCK_PARAMDEFAULTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.HierarchyBlock.ParamDefaultsEntry)
    })
  ,

  'PortsEntry' : _reflection.GeneratedProtocolMessageType('PortsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HIERARCHYBLOCK_PORTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.HierarchyBlock.PortsEntry)
    })
  ,

  'BlocksEntry' : _reflection.GeneratedProtocolMessageType('BlocksEntry', (_message.Message,), {
    'DESCRIPTOR' : _HIERARCHYBLOCK_BLOCKSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.HierarchyBlock.BlocksEntry)
    })
  ,

  'LinksEntry' : _reflection.GeneratedProtocolMessageType('LinksEntry', (_message.Message,), {
    'DESCRIPTOR' : _HIERARCHYBLOCK_LINKSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.HierarchyBlock.LinksEntry)
    })
  ,

  'ConstraintsEntry' : _reflection.GeneratedProtocolMessageType('ConstraintsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HIERARCHYBLOCK_CONSTRAINTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.HierarchyBlock.ConstraintsEntry)
    })
  ,
  'DESCRIPTOR' : _HIERARCHYBLOCK,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.HierarchyBlock)
  })
_sym_db.RegisterMessage(HierarchyBlock)
_sym_db.RegisterMessage(HierarchyBlock.ParamsEntry)
_sym_db.RegisterMessage(HierarchyBlock.ParamDefaultsEntry)
_sym_db.RegisterMessage(HierarchyBlock.PortsEntry)
_sym_db.RegisterMessage(HierarchyBlock.BlocksEntry)
_sym_db.RegisterMessage(HierarchyBlock.LinksEntry)
_sym_db.RegisterMessage(HierarchyBlock.ConstraintsEntry)

Generator = _reflection.GeneratedProtocolMessageType('Generator', (_message.Message,), {
  'DESCRIPTOR' : _GENERATOR,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.Generator)
  })
_sym_db.RegisterMessage(Generator)

BlockLike = _reflection.GeneratedProtocolMessageType('BlockLike', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKLIKE,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.BlockLike)
  })
_sym_db.RegisterMessage(BlockLike)

Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LINK_PARAMSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Link.ParamsEntry)
    })
  ,

  'PortsEntry' : _reflection.GeneratedProtocolMessageType('PortsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LINK_PORTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Link.PortsEntry)
    })
  ,

  'LinksEntry' : _reflection.GeneratedProtocolMessageType('LinksEntry', (_message.Message,), {
    'DESCRIPTOR' : _LINK_LINKSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Link.LinksEntry)
    })
  ,

  'ConstraintsEntry' : _reflection.GeneratedProtocolMessageType('ConstraintsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LINK_CONSTRAINTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.Link.ConstraintsEntry)
    })
  ,
  'DESCRIPTOR' : _LINK,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.Link)
  })
_sym_db.RegisterMessage(Link)
_sym_db.RegisterMessage(Link.ParamsEntry)
_sym_db.RegisterMessage(Link.PortsEntry)
_sym_db.RegisterMessage(Link.LinksEntry)
_sym_db.RegisterMessage(Link.ConstraintsEntry)

LinkArray = _reflection.GeneratedProtocolMessageType('LinkArray', (_message.Message,), {

  'PortsEntry' : _reflection.GeneratedProtocolMessageType('PortsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LINKARRAY_PORTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.LinkArray.PortsEntry)
    })
  ,

  'ConstraintsEntry' : _reflection.GeneratedProtocolMessageType('ConstraintsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LINKARRAY_CONSTRAINTSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.LinkArray.ConstraintsEntry)
    })
  ,

  'LinksEntry' : _reflection.GeneratedProtocolMessageType('LinksEntry', (_message.Message,), {
    'DESCRIPTOR' : _LINKARRAY_LINKSENTRY,
    '__module__' : 'edgir.elem_pb2'
    # @@protoc_insertion_point(class_scope:edgir.elem.LinkArray.LinksEntry)
    })
  ,
  'DESCRIPTOR' : _LINKARRAY,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.LinkArray)
  })
_sym_db.RegisterMessage(LinkArray)
_sym_db.RegisterMessage(LinkArray.PortsEntry)
_sym_db.RegisterMessage(LinkArray.ConstraintsEntry)
_sym_db.RegisterMessage(LinkArray.LinksEntry)

LinkLike = _reflection.GeneratedProtocolMessageType('LinkLike', (_message.Message,), {
  'DESCRIPTOR' : _LINKLIKE,
  '__module__' : 'edgir.elem_pb2'
  # @@protoc_insertion_point(class_scope:edgir.elem.LinkLike)
  })
_sym_db.RegisterMessage(LinkLike)

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
  _HIERARCHYBLOCK._serialized_start=1494
  _HIERARCHYBLOCK._serialized_end=2533
  _HIERARCHYBLOCK_PARAMSENTRY._serialized_start=344
  _HIERARCHYBLOCK_PARAMSENTRY._serialized_end=410
  _HIERARCHYBLOCK_PARAMDEFAULTSENTRY._serialized_start=2177
  _HIERARCHYBLOCK_PARAMDEFAULTSENTRY._serialized_end=2252
  _HIERARCHYBLOCK_PORTSENTRY._serialized_start=846
  _HIERARCHYBLOCK_PORTSENTRY._serialized_end=912
  _HIERARCHYBLOCK_BLOCKSENTRY._serialized_start=2322
  _HIERARCHYBLOCK_BLOCKSENTRY._serialized_end=2390
  _HIERARCHYBLOCK_LINKSENTRY._serialized_start=2392
  _HIERARCHYBLOCK_LINKSENTRY._serialized_end=2458
  _HIERARCHYBLOCK_CONSTRAINTSENTRY._serialized_start=412
  _HIERARCHYBLOCK_CONSTRAINTSENTRY._serialized_end=485
  _GENERATOR._serialized_start=2535
  _GENERATOR._serialized_end=2593
  _BLOCKLIKE._serialized_start=2596
  _BLOCKLIKE._serialized_end=2750
  _LINK._serialized_start=2753
  _LINK._serialized_end=3356
  _LINK_PARAMSENTRY._serialized_start=344
  _LINK_PARAMSENTRY._serialized_end=410
  _LINK_PORTSENTRY._serialized_start=846
  _LINK_PORTSENTRY._serialized_end=912
  _LINK_LINKSENTRY._serialized_start=2392
  _LINK_LINKSENTRY._serialized_end=2458
  _LINK_CONSTRAINTSENTRY._serialized_start=412
  _LINK_CONSTRAINTSENTRY._serialized_end=485
  _LINKARRAY._serialized_start=3359
  _LINKARRAY._serialized_end=3822
  _LINKARRAY_PORTSENTRY._serialized_start=846
  _LINKARRAY_PORTSENTRY._serialized_end=912
  _LINKARRAY_CONSTRAINTSENTRY._serialized_start=412
  _LINKARRAY_CONSTRAINTSENTRY._serialized_end=485
  _LINKARRAY_LINKSENTRY._serialized_start=2392
  _LINKARRAY_LINKSENTRY._serialized_end=2458
  _LINKLIKE._serialized_start=3825
  _LINKLIKE._serialized_end=4003
# @@protoc_insertion_point(module_scope)