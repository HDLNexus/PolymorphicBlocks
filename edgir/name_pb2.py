# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edgir/name.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgir import common_pb2 as edgir_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x65\x64gir/name.proto\x12\nedgir.name\x1a\x12\x65\x64gir/common.proto\"O\n\tNamespace\x12\x0f\n\x05\x62\x61sic\x18\x01 \x01(\tH\x00\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.MetadataB\x0b\n\tnamespace\"A\n\x0bLibraryName\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadatab\x06proto3')



_NAMESPACE = DESCRIPTOR.message_types_by_name['Namespace']
_LIBRARYNAME = DESCRIPTOR.message_types_by_name['LibraryName']
Namespace = _reflection.GeneratedProtocolMessageType('Namespace', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACE,
  '__module__' : 'edgir.name_pb2'
  # @@protoc_insertion_point(class_scope:edgir.name.Namespace)
  })
_sym_db.RegisterMessage(Namespace)

LibraryName = _reflection.GeneratedProtocolMessageType('LibraryName', (_message.Message,), {
  'DESCRIPTOR' : _LIBRARYNAME,
  '__module__' : 'edgir.name_pb2'
  # @@protoc_insertion_point(class_scope:edgir.name.LibraryName)
  })
_sym_db.RegisterMessage(LibraryName)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NAMESPACE._serialized_start=52
  _NAMESPACE._serialized_end=131
  _LIBRARYNAME._serialized_start=133
  _LIBRARYNAME._serialized_end=198
# @@protoc_insertion_point(module_scope)
