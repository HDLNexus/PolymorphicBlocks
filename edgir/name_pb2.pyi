"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import edgir.common_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

#*
#A namespace allows us to define a more useful organizational structure
#over items in the library. It lets us group elements in categories that
#are orthogonal to the usual Block, Port, Link, ontology.
class Namespace(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BASIC_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    #* Basic namespaces are a way to organize library elements into a
    #useful hirearchy (e.g. 'Core.*' for the most primitive definitions
    #that we define, or 'NXP.*' for NXP made components.)
    #
    #Basic namespaces should have the following properties:
    #
    #- First char is a capital letter
    #- All other chars must be letters, numbers, '-', '<', '>'
    #- CamelCase is preffered, don't use any symbols in the name
    #if possible.
    basic: typing.Text = ...
    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        basic : typing.Text = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"basic",b"basic",u"meta",b"meta",u"namespace",b"namespace"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"basic",b"basic",u"meta",b"meta",u"namespace",b"namespace"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"namespace",b"namespace"]) -> typing.Optional[typing_extensions.Literal["basic"]]: ...
global___Namespace = Namespace

#* A library name is a way to identify a specific library from a
#set of parent libraries.
#
#This can be the initial element in a path or reference.
class LibraryName(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    #* Since libraries allow for inheritance, we will often want to say
    #this element, defined in *this* particular library.
    #
    #In those cases we want to be able to specify the relevant library
    #by its identifier.
    #
    #Otherwise we assume it's somehow implicit which library we're
    #talking about.
    name: typing.Text = ...
    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"meta",b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"name",b"name"]) -> None: ...
global___LibraryName = LibraryName
