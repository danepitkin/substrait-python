"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..proto import parameterized_types_pb2 as proto_dot_parameterized__types__pb2
from ..proto import type_pb2 as proto_dot_type__pb2
from ..proto import type_expressions_pb2 as proto_dot_type__expressions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14proto/function.proto\x12\x05proto\x1a\x1fproto/parameterized_types.proto\x1a\x10proto/type.proto\x1a\x1cproto/type_expressions.proto"\xe9\x18\n\x11FunctionSignature\x1a\xb8\x02\n\x10FinalArgVariadic\x12\x19\n\x08min_args\x18\x01 \x01(\x03R\x07minArgs\x12\x19\n\x08max_args\x18\x02 \x01(\x03R\x07maxArgs\x12`\n\x0bconsistency\x18\x03 \x01(\x0e2>.proto.FunctionSignature.FinalArgVariadic.ParameterConsistencyR\x0bconsistency"\x8b\x01\n\x14ParameterConsistency\x12%\n!PARAMETER_CONSISTENCY_UNSPECIFIED\x10\x00\x12$\n PARAMETER_CONSISTENCY_CONSISTENT\x10\x01\x12&\n"PARAMETER_CONSISTENCY_INCONSISTENT\x10\x02\x1a\x10\n\x0eFinalArgNormal\x1a\xb0\x04\n\x06Scalar\x12?\n\targuments\x18\x02 \x03(\x0b2!.proto.FunctionSignature.ArgumentR\targuments\x12\x12\n\x04name\x18\x03 \x03(\tR\x04name\x12F\n\x0bdescription\x18\x04 \x01(\x0b2$.proto.FunctionSignature.DescriptionR\x0bdescription\x12$\n\rdeterministic\x18\x07 \x01(\x08R\rdeterministic\x12+\n\x11session_dependent\x18\x08 \x01(\x08R\x10sessionDependent\x12<\n\x0boutput_type\x18\t \x01(\x0b2\x1b.proto.DerivationExpressionR\noutputType\x12G\n\x08variadic\x18\n \x01(\x0b2).proto.FunctionSignature.FinalArgVariadicH\x00R\x08variadic\x12A\n\x06normal\x18\x0b \x01(\x0b2\'.proto.FunctionSignature.FinalArgNormalH\x00R\x06normal\x12Q\n\x0fimplementations\x18\x0c \x03(\x0b2\'.proto.FunctionSignature.ImplementationR\x0fimplementationsB\x19\n\x17final_variable_behavior\x1a\xa0\x05\n\tAggregate\x12?\n\targuments\x18\x02 \x03(\x0b2!.proto.FunctionSignature.ArgumentR\targuments\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12F\n\x0bdescription\x18\x04 \x01(\x0b2$.proto.FunctionSignature.DescriptionR\x0bdescription\x12$\n\rdeterministic\x18\x07 \x01(\x08R\rdeterministic\x12+\n\x11session_dependent\x18\x08 \x01(\x08R\x10sessionDependent\x12<\n\x0boutput_type\x18\t \x01(\x0b2\x1b.proto.DerivationExpressionR\noutputType\x12G\n\x08variadic\x18\n \x01(\x0b2).proto.FunctionSignature.FinalArgVariadicH\x00R\x08variadic\x12A\n\x06normal\x18\x0b \x01(\x0b2\'.proto.FunctionSignature.FinalArgNormalH\x00R\x06normal\x12\x18\n\x07ordered\x18\x0e \x01(\x08R\x07ordered\x12\x17\n\x07max_set\x18\x0c \x01(\x04R\x06maxSet\x128\n\x11intermediate_type\x18\r \x01(\x0b2\x0b.proto.TypeR\x10intermediateType\x12Q\n\x0fimplementations\x18\x0f \x03(\x0b2\'.proto.FunctionSignature.ImplementationR\x0fimplementationsB\x19\n\x17final_variable_behavior\x1a\xdb\x06\n\x06Window\x12?\n\targuments\x18\x02 \x03(\x0b2!.proto.FunctionSignature.ArgumentR\targuments\x12\x12\n\x04name\x18\x03 \x03(\tR\x04name\x12F\n\x0bdescription\x18\x04 \x01(\x0b2$.proto.FunctionSignature.DescriptionR\x0bdescription\x12$\n\rdeterministic\x18\x07 \x01(\x08R\rdeterministic\x12+\n\x11session_dependent\x18\x08 \x01(\x08R\x10sessionDependent\x12H\n\x11intermediate_type\x18\t \x01(\x0b2\x1b.proto.DerivationExpressionR\x10intermediateType\x12<\n\x0boutput_type\x18\n \x01(\x0b2\x1b.proto.DerivationExpressionR\noutputType\x12G\n\x08variadic\x18\x10 \x01(\x0b2).proto.FunctionSignature.FinalArgVariadicH\x00R\x08variadic\x12A\n\x06normal\x18\x11 \x01(\x0b2\'.proto.FunctionSignature.FinalArgNormalH\x00R\x06normal\x12\x18\n\x07ordered\x18\x0b \x01(\x08R\x07ordered\x12\x17\n\x07max_set\x18\x0c \x01(\x04R\x06maxSet\x12K\n\x0bwindow_type\x18\x0e \x01(\x0e2*.proto.FunctionSignature.Window.WindowTypeR\nwindowType\x12Q\n\x0fimplementations\x18\x0f \x03(\x0b2\'.proto.FunctionSignature.ImplementationR\x0fimplementations"_\n\nWindowType\x12\x1b\n\x17WINDOW_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15WINDOW_TYPE_STREAMING\x10\x01\x12\x19\n\x15WINDOW_TYPE_PARTITION\x10\x02B\x19\n\x17final_variable_behavior\x1a=\n\x0bDescription\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12\x12\n\x04body\x18\x02 \x01(\tR\x04body\x1a\xad\x01\n\x0eImplementation\x12@\n\x04type\x18\x01 \x01(\x0e2,.proto.FunctionSignature.Implementation.TypeR\x04type\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri"G\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11TYPE_WEB_ASSEMBLY\x10\x01\x12\x12\n\x0eTYPE_TRINO_JAR\x10\x02\x1a\xe3\x03\n\x08Argument\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12G\n\x05value\x18\x02 \x01(\x0b2/.proto.FunctionSignature.Argument.ValueArgumentH\x00R\x05value\x12D\n\x04type\x18\x03 \x01(\x0b2..proto.FunctionSignature.Argument.TypeArgumentH\x00R\x04type\x12D\n\x04enum\x18\x04 \x01(\x0b2..proto.FunctionSignature.Argument.EnumArgumentH\x00R\x04enum\x1aY\n\rValueArgument\x12,\n\x04type\x18\x01 \x01(\x0b2\x18.proto.ParameterizedTypeR\x04type\x12\x1a\n\x08constant\x18\x02 \x01(\x08R\x08constant\x1a<\n\x0cTypeArgument\x12,\n\x04type\x18\x01 \x01(\x0b2\x18.proto.ParameterizedTypeR\x04type\x1aD\n\x0cEnumArgument\x12\x18\n\x07options\x18\x01 \x03(\tR\x07options\x12\x1a\n\x08optional\x18\x02 \x01(\x08R\x08optionalB\x0f\n\rargument_kindB#\n\x0eio.proto.protoP\x01\xaa\x02\x0eProto.Protobufb\x06proto3')
_FUNCTIONSIGNATURE = DESCRIPTOR.message_types_by_name['FunctionSignature']
_FUNCTIONSIGNATURE_FINALARGVARIADIC = _FUNCTIONSIGNATURE.nested_types_by_name['FinalArgVariadic']
_FUNCTIONSIGNATURE_FINALARGNORMAL = _FUNCTIONSIGNATURE.nested_types_by_name['FinalArgNormal']
_FUNCTIONSIGNATURE_SCALAR = _FUNCTIONSIGNATURE.nested_types_by_name['Scalar']
_FUNCTIONSIGNATURE_AGGREGATE = _FUNCTIONSIGNATURE.nested_types_by_name['Aggregate']
_FUNCTIONSIGNATURE_WINDOW = _FUNCTIONSIGNATURE.nested_types_by_name['Window']
_FUNCTIONSIGNATURE_DESCRIPTION = _FUNCTIONSIGNATURE.nested_types_by_name['Description']
_FUNCTIONSIGNATURE_IMPLEMENTATION = _FUNCTIONSIGNATURE.nested_types_by_name['Implementation']
_FUNCTIONSIGNATURE_ARGUMENT = _FUNCTIONSIGNATURE.nested_types_by_name['Argument']
_FUNCTIONSIGNATURE_ARGUMENT_VALUEARGUMENT = _FUNCTIONSIGNATURE_ARGUMENT.nested_types_by_name['ValueArgument']
_FUNCTIONSIGNATURE_ARGUMENT_TYPEARGUMENT = _FUNCTIONSIGNATURE_ARGUMENT.nested_types_by_name['TypeArgument']
_FUNCTIONSIGNATURE_ARGUMENT_ENUMARGUMENT = _FUNCTIONSIGNATURE_ARGUMENT.nested_types_by_name['EnumArgument']
_FUNCTIONSIGNATURE_FINALARGVARIADIC_PARAMETERCONSISTENCY = _FUNCTIONSIGNATURE_FINALARGVARIADIC.enum_types_by_name['ParameterConsistency']
_FUNCTIONSIGNATURE_WINDOW_WINDOWTYPE = _FUNCTIONSIGNATURE_WINDOW.enum_types_by_name['WindowType']
_FUNCTIONSIGNATURE_IMPLEMENTATION_TYPE = _FUNCTIONSIGNATURE_IMPLEMENTATION.enum_types_by_name['Type']
FunctionSignature = _reflection.GeneratedProtocolMessageType('FunctionSignature', (_message.Message,), {'FinalArgVariadic': _reflection.GeneratedProtocolMessageType('FinalArgVariadic', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_FINALARGVARIADIC, '__module__': 'proto.function_pb2'}), 'FinalArgNormal': _reflection.GeneratedProtocolMessageType('FinalArgNormal', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_FINALARGNORMAL, '__module__': 'proto.function_pb2'}), 'Scalar': _reflection.GeneratedProtocolMessageType('Scalar', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_SCALAR, '__module__': 'proto.function_pb2'}), 'Aggregate': _reflection.GeneratedProtocolMessageType('Aggregate', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_AGGREGATE, '__module__': 'proto.function_pb2'}), 'Window': _reflection.GeneratedProtocolMessageType('Window', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_WINDOW, '__module__': 'proto.function_pb2'}), 'Description': _reflection.GeneratedProtocolMessageType('Description', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_DESCRIPTION, '__module__': 'proto.function_pb2'}), 'Implementation': _reflection.GeneratedProtocolMessageType('Implementation', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_IMPLEMENTATION, '__module__': 'proto.function_pb2'}), 'Argument': _reflection.GeneratedProtocolMessageType('Argument', (_message.Message,), {'ValueArgument': _reflection.GeneratedProtocolMessageType('ValueArgument', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_ARGUMENT_VALUEARGUMENT, '__module__': 'proto.function_pb2'}), 'TypeArgument': _reflection.GeneratedProtocolMessageType('TypeArgument', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_ARGUMENT_TYPEARGUMENT, '__module__': 'proto.function_pb2'}), 'EnumArgument': _reflection.GeneratedProtocolMessageType('EnumArgument', (_message.Message,), {'DESCRIPTOR': _FUNCTIONSIGNATURE_ARGUMENT_ENUMARGUMENT, '__module__': 'proto.function_pb2'}), 'DESCRIPTOR': _FUNCTIONSIGNATURE_ARGUMENT, '__module__': 'proto.function_pb2'}), 'DESCRIPTOR': _FUNCTIONSIGNATURE, '__module__': 'proto.function_pb2'})
_sym_db.RegisterMessage(FunctionSignature)
_sym_db.RegisterMessage(FunctionSignature.FinalArgVariadic)
_sym_db.RegisterMessage(FunctionSignature.FinalArgNormal)
_sym_db.RegisterMessage(FunctionSignature.Scalar)
_sym_db.RegisterMessage(FunctionSignature.Aggregate)
_sym_db.RegisterMessage(FunctionSignature.Window)
_sym_db.RegisterMessage(FunctionSignature.Description)
_sym_db.RegisterMessage(FunctionSignature.Implementation)
_sym_db.RegisterMessage(FunctionSignature.Argument)
_sym_db.RegisterMessage(FunctionSignature.Argument.ValueArgument)
_sym_db.RegisterMessage(FunctionSignature.Argument.TypeArgument)
_sym_db.RegisterMessage(FunctionSignature.Argument.EnumArgument)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x0eio.proto.protoP\x01\xaa\x02\x0eProto.Protobuf'
    _FUNCTIONSIGNATURE._serialized_start = 113
    _FUNCTIONSIGNATURE._serialized_end = 3290
    _FUNCTIONSIGNATURE_FINALARGVARIADIC._serialized_start = 135
    _FUNCTIONSIGNATURE_FINALARGVARIADIC._serialized_end = 447
    _FUNCTIONSIGNATURE_FINALARGVARIADIC_PARAMETERCONSISTENCY._serialized_start = 308
    _FUNCTIONSIGNATURE_FINALARGVARIADIC_PARAMETERCONSISTENCY._serialized_end = 447
    _FUNCTIONSIGNATURE_FINALARGNORMAL._serialized_start = 449
    _FUNCTIONSIGNATURE_FINALARGNORMAL._serialized_end = 465
    _FUNCTIONSIGNATURE_SCALAR._serialized_start = 468
    _FUNCTIONSIGNATURE_SCALAR._serialized_end = 1028
    _FUNCTIONSIGNATURE_AGGREGATE._serialized_start = 1031
    _FUNCTIONSIGNATURE_AGGREGATE._serialized_end = 1703
    _FUNCTIONSIGNATURE_WINDOW._serialized_start = 1706
    _FUNCTIONSIGNATURE_WINDOW._serialized_end = 2565
    _FUNCTIONSIGNATURE_WINDOW_WINDOWTYPE._serialized_start = 2443
    _FUNCTIONSIGNATURE_WINDOW_WINDOWTYPE._serialized_end = 2538
    _FUNCTIONSIGNATURE_DESCRIPTION._serialized_start = 2567
    _FUNCTIONSIGNATURE_DESCRIPTION._serialized_end = 2628
    _FUNCTIONSIGNATURE_IMPLEMENTATION._serialized_start = 2631
    _FUNCTIONSIGNATURE_IMPLEMENTATION._serialized_end = 2804
    _FUNCTIONSIGNATURE_IMPLEMENTATION_TYPE._serialized_start = 2733
    _FUNCTIONSIGNATURE_IMPLEMENTATION_TYPE._serialized_end = 2804
    _FUNCTIONSIGNATURE_ARGUMENT._serialized_start = 2807
    _FUNCTIONSIGNATURE_ARGUMENT._serialized_end = 3290
    _FUNCTIONSIGNATURE_ARGUMENT_VALUEARGUMENT._serialized_start = 3052
    _FUNCTIONSIGNATURE_ARGUMENT_VALUEARGUMENT._serialized_end = 3141
    _FUNCTIONSIGNATURE_ARGUMENT_TYPEARGUMENT._serialized_start = 3143
    _FUNCTIONSIGNATURE_ARGUMENT_TYPEARGUMENT._serialized_end = 3203
    _FUNCTIONSIGNATURE_ARGUMENT_ENUMARGUMENT._serialized_start = 3205
    _FUNCTIONSIGNATURE_ARGUMENT_ENUMARGUMENT._serialized_end = 3273