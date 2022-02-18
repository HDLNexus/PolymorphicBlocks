"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import edgir.elem_pb2
import edgir.lit_pb2
import edgir.ref_pb2
import edgir.schema_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ModuleName(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___ModuleName = ModuleName

class LibraryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENT_FIELD_NUMBER: builtins.int
    @property
    def element(self) -> edgir.ref_pb2.LibraryPath:
        """library element asked for"""
        pass
    def __init__(self,
        *,
        element: typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["element",b"element"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["element",b"element"]) -> None: ...
global___LibraryRequest = LibraryRequest

class GeneratorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Value(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PATH_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        @property
        def path(self) -> edgir.ref_pb2.LocalPath: ...
        @property
        def value(self) -> edgir.lit_pb2.ValueLit: ...
        def __init__(self,
            *,
            path: typing.Optional[edgir.ref_pb2.LocalPath] = ...,
            value: typing.Optional[edgir.lit_pb2.ValueLit] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["path",b"path","value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["path",b"path","value",b"value"]) -> None: ...

    ELEMENT_FIELD_NUMBER: builtins.int
    FN_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def element(self) -> edgir.ref_pb2.LibraryPath:
        """path of library element containing the generator"""
        pass
    fn: typing.Text
    """name of generator function"""

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GeneratorRequest.Value]: ...
    def __init__(self,
        *,
        element: typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        fn: typing.Text = ...,
        values: typing.Optional[typing.Iterable[global___GeneratorRequest.Value]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["element",b"element"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["element",b"element","fn",b"fn","values",b"values"]) -> None: ...
global___GeneratorRequest = GeneratorRequest

class Refinements(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Subclass(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PATH_FIELD_NUMBER: builtins.int
        CLS_FIELD_NUMBER: builtins.int
        REPLACEMENT_FIELD_NUMBER: builtins.int
        @property
        def path(self) -> edgir.ref_pb2.LocalPath: ...
        @property
        def cls(self) -> edgir.ref_pb2.LibraryPath: ...
        @property
        def replacement(self) -> edgir.ref_pb2.LibraryPath: ...
        def __init__(self,
            *,
            path: typing.Optional[edgir.ref_pb2.LocalPath] = ...,
            cls: typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
            replacement: typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["cls",b"cls","path",b"path","replacement",b"replacement","source",b"source"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["cls",b"cls","path",b"path","replacement",b"replacement","source",b"source"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["source",b"source"]) -> typing.Optional[typing_extensions.Literal["path","cls"]]: ...

    class Value(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ClassParamPath(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            CLS_FIELD_NUMBER: builtins.int
            PARAM_PATH_FIELD_NUMBER: builtins.int
            @property
            def cls(self) -> edgir.ref_pb2.LibraryPath: ...
            @property
            def param_path(self) -> edgir.ref_pb2.LocalPath: ...
            def __init__(self,
                *,
                cls: typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
                param_path: typing.Optional[edgir.ref_pb2.LocalPath] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["cls",b"cls","param_path",b"param_path"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["cls",b"cls","param_path",b"param_path"]) -> None: ...

        PATH_FIELD_NUMBER: builtins.int
        CLS_PARAM_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        @property
        def path(self) -> edgir.ref_pb2.LocalPath: ...
        @property
        def cls_param(self) -> global___Refinements.Value.ClassParamPath: ...
        @property
        def value(self) -> edgir.lit_pb2.ValueLit: ...
        def __init__(self,
            *,
            path: typing.Optional[edgir.ref_pb2.LocalPath] = ...,
            cls_param: typing.Optional[global___Refinements.Value.ClassParamPath] = ...,
            value: typing.Optional[edgir.lit_pb2.ValueLit] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["cls_param",b"cls_param","path",b"path","source",b"source","value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["cls_param",b"cls_param","path",b"path","source",b"source","value",b"value"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["source",b"source"]) -> typing.Optional[typing_extensions.Literal["path","cls_param"]]: ...

    SUBCLASSES_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def subclasses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Refinements.Subclass]: ...
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Refinements.Value]: ...
    def __init__(self,
        *,
        subclasses: typing.Optional[typing.Iterable[global___Refinements.Subclass]] = ...,
        values: typing.Optional[typing.Iterable[global___Refinements.Value]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subclasses",b"subclasses","values",b"values"]) -> None: ...
global___Refinements = Refinements

class IndexResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEXED_FIELD_NUMBER: builtins.int
    @property
    def indexed(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LibraryPath]: ...
    def __init__(self,
        *,
        indexed: typing.Optional[typing.Iterable[edgir.ref_pb2.LibraryPath]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["indexed",b"indexed"]) -> None: ...
global___IndexResponse = IndexResponse

class LibraryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENT_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    REFINEMENTS_FIELD_NUMBER: builtins.int
    @property
    def element(self) -> edgir.schema_pb2.Library.NS.Val: ...
    error: typing.Text
    """TODO source locators"""

    @property
    def refinements(self) -> global___Refinements:
        """only valid if element is a top-level block, and not error"""
        pass
    def __init__(self,
        *,
        element: typing.Optional[edgir.schema_pb2.Library.NS.Val] = ...,
        error: typing.Text = ...,
        refinements: typing.Optional[global___Refinements] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["element",b"element","error",b"error","refinements",b"refinements","result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["element",b"element","error",b"error","refinements",b"refinements","result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["result",b"result"]) -> typing.Optional[typing_extensions.Literal["element","error"]]: ...
global___LibraryResponse = LibraryResponse

class GeneratorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GENERATED_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def generated(self) -> edgir.elem_pb2.HierarchyBlock: ...
    error: typing.Text
    """TODO source locators"""

    def __init__(self,
        *,
        generated: typing.Optional[edgir.elem_pb2.HierarchyBlock] = ...,
        error: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","generated",b"generated","result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","generated",b"generated","result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["result",b"result"]) -> typing.Optional[typing_extensions.Literal["generated","error"]]: ...
global___GeneratorResponse = GeneratorResponse

class HdlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_MODULE_FIELD_NUMBER: builtins.int
    GET_LIBRARY_ELEMENT_FIELD_NUMBER: builtins.int
    ELABORATE_GENERATOR_FIELD_NUMBER: builtins.int
    @property
    def index_module(self) -> global___ModuleName:
        """returns an index of IR elements in a Python module"""
        pass
    @property
    def get_library_element(self) -> global___LibraryRequest:
        """returns the IR for a library element"""
        pass
    @property
    def elaborate_generator(self) -> global___GeneratorRequest:
        """returns the elaborated IR"""
        pass
    def __init__(self,
        *,
        index_module: typing.Optional[global___ModuleName] = ...,
        get_library_element: typing.Optional[global___LibraryRequest] = ...,
        elaborate_generator: typing.Optional[global___GeneratorRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elaborate_generator",b"elaborate_generator","get_library_element",b"get_library_element","index_module",b"index_module","request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["elaborate_generator",b"elaborate_generator","get_library_element",b"get_library_element","index_module",b"index_module","request",b"request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["request",b"request"]) -> typing.Optional[typing_extensions.Literal["index_module","get_library_element","elaborate_generator"]]: ...
global___HdlRequest = HdlRequest

class HdlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INDEX_MODULE_FIELD_NUMBER: builtins.int
    GET_LIBRARY_ELEMENT_FIELD_NUMBER: builtins.int
    ELABORATE_GENERATOR_FIELD_NUMBER: builtins.int
    @property
    def index_module(self) -> global___IndexResponse:
        """list of contained library elements"""
        pass
    @property
    def get_library_element(self) -> global___LibraryResponse: ...
    @property
    def elaborate_generator(self) -> global___GeneratorResponse: ...
    def __init__(self,
        *,
        index_module: typing.Optional[global___IndexResponse] = ...,
        get_library_element: typing.Optional[global___LibraryResponse] = ...,
        elaborate_generator: typing.Optional[global___GeneratorResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elaborate_generator",b"elaborate_generator","get_library_element",b"get_library_element","index_module",b"index_module","response",b"response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["elaborate_generator",b"elaborate_generator","get_library_element",b"get_library_element","index_module",b"index_module","response",b"response"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["index_module","get_library_element","elaborate_generator"]]: ...
global___HdlResponse = HdlResponse
