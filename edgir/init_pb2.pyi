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

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ValInit(google.protobuf.message.Message):
    """* This is the general way we initialize values in the local context.

    I think the frontend should have more type specific wrappers around
    this since the data required for each type can be different.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FLOATING_FIELD_NUMBER: builtins.int
    INTEGER_FIELD_NUMBER: builtins.int
    BOOLEAN_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    SET_FIELD_NUMBER: builtins.int
    STRUCT_FIELD_NUMBER: builtins.int
    RANGE_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def floating(self) -> edgir.common_pb2.Empty: ...
    @property
    def integer(self) -> edgir.common_pb2.Empty: ...
    @property
    def boolean(self) -> edgir.common_pb2.Empty: ...
    @property
    def text(self) -> edgir.common_pb2.Empty: ...
    @property
    def set(self) -> edgir.common_pb2.Empty: ...
    @property
    def struct(self) -> edgir.common_pb2.Empty: ...
    @property
    def range(self) -> edgir.common_pb2.Empty: ...
    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        floating: typing.Optional[edgir.common_pb2.Empty] = ...,
        integer: typing.Optional[edgir.common_pb2.Empty] = ...,
        boolean: typing.Optional[edgir.common_pb2.Empty] = ...,
        text: typing.Optional[edgir.common_pb2.Empty] = ...,
        set: typing.Optional[edgir.common_pb2.Empty] = ...,
        struct: typing.Optional[edgir.common_pb2.Empty] = ...,
        range: typing.Optional[edgir.common_pb2.Empty] = ...,
        meta: typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["boolean",b"boolean","floating",b"floating","integer",b"integer","meta",b"meta","range",b"range","set",b"set","struct",b"struct","text",b"text","val",b"val"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["boolean",b"boolean","floating",b"floating","integer",b"integer","meta",b"meta","range",b"range","set",b"set","struct",b"struct","text",b"text","val",b"val"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["val",b"val"]) -> typing.Optional[typing_extensions.Literal["floating","integer","boolean","text","set","struct","range"]]: ...
global___ValInit = ValInit
