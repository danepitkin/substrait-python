"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ..proto.extensions import extensions_pb2 as proto_dot_extensions_dot_extensions__pb2
from ..proto import type_pb2 as proto_dot_type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/algebra.proto\x12\x05proto\x1a\x19google/protobuf/any.proto\x1a!proto/extensions/extensions.proto\x1a\x10proto/type.proto"\x8e\x06\n\tRelCommon\x121\n\x06direct\x18\x01 \x01(\x0b2\x17.proto.RelCommon.DirectH\x00R\x06direct\x12+\n\x04emit\x18\x02 \x01(\x0b2\x15.proto.RelCommon.EmitH\x00R\x04emit\x12)\n\x04hint\x18\x03 \x01(\x0b2\x15.proto.RelCommon.HintR\x04hint\x12R\n\x12advanced_extension\x18\x04 \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x1a\x08\n\x06Direct\x1a-\n\x04Emit\x12%\n\x0eoutput_mapping\x18\x01 \x03(\x05R\routputMapping\x1a\xdb\x03\n\x04Hint\x121\n\x05stats\x18\x01 \x01(\x0b2\x1b.proto.RelCommon.Hint.StatsR\x05stats\x12G\n\nconstraint\x18\x02 \x01(\x0b2\'.proto.RelCommon.Hint.RuntimeConstraintR\nconstraint\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x1a\x99\x01\n\x05Stats\x12\x1b\n\trow_count\x18\x01 \x01(\x01R\x08rowCount\x12\x1f\n\x0brecord_size\x18\x02 \x01(\x01R\nrecordSize\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x1ag\n\x11RuntimeConstraint\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtensionB\x0b\n\temit_kind"\xf7\r\n\x07ReadRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x123\n\x0bbase_schema\x18\x02 \x01(\x0b2\x12.proto.NamedStructR\nbaseSchema\x12)\n\x06filter\x18\x03 \x01(\x0b2\x11.proto.ExpressionR\x06filter\x12?\n\x12best_effort_filter\x18\x0b \x01(\x0b2\x11.proto.ExpressionR\x10bestEffortFilter\x12@\n\nprojection\x18\x04 \x01(\x0b2 .proto.Expression.MaskExpressionR\nprojection\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x12B\n\rvirtual_table\x18\x05 \x01(\x0b2\x1b.proto.ReadRel.VirtualTableH\x00R\x0cvirtualTable\x12<\n\x0blocal_files\x18\x06 \x01(\x0b2\x19.proto.ReadRel.LocalFilesH\x00R\nlocalFiles\x12<\n\x0bnamed_table\x18\x07 \x01(\x0b2\x19.proto.ReadRel.NamedTableH\x00R\nnamedTable\x12H\n\x0fextension_table\x18\x08 \x01(\x0b2\x1d.proto.ReadRel.ExtensionTableH\x00R\x0eextensionTable\x1av\n\nNamedTable\x12\x14\n\x05names\x18\x01 \x03(\tR\x05names\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x1aH\n\x0cVirtualTable\x128\n\x06values\x18\x01 \x03(\x0b2 .proto.Expression.Literal.StructR\x06values\x1a>\n\x0eExtensionTable\x12,\n\x06detail\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyR\x06detail\x1a\xf1\x06\n\nLocalFiles\x12;\n\x05items\x18\x01 \x03(\x0b2%.proto.ReadRel.LocalFiles.FileOrFilesR\x05items\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x1a\xd1\x05\n\x0bFileOrFiles\x12\x1b\n\x08uri_path\x18\x01 \x01(\tH\x00R\x07uriPath\x12$\n\ruri_path_glob\x18\x02 \x01(\tH\x00R\x0buriPathGlob\x12\x1b\n\x08uri_file\x18\x03 \x01(\tH\x00R\x07uriFile\x12\x1f\n\nuri_folder\x18\x04 \x01(\tH\x00R\turiFolder\x12\'\n\x0fpartition_index\x18\x06 \x01(\x04R\x0epartitionIndex\x12\x14\n\x05start\x18\x07 \x01(\x04R\x05start\x12\x16\n\x06length\x18\x08 \x01(\x04R\x06length\x12T\n\x07parquet\x18\t \x01(\x0b28.proto.ReadRel.LocalFiles.FileOrFiles.ParquetReadOptionsH\x01R\x07parquet\x12N\n\x05arrow\x18\n \x01(\x0b26.proto.ReadRel.LocalFiles.FileOrFiles.ArrowReadOptionsH\x01R\x05arrow\x12H\n\x03orc\x18\x0b \x01(\x0b24.proto.ReadRel.LocalFiles.FileOrFiles.OrcReadOptionsH\x01R\x03orc\x124\n\textension\x18\x0c \x01(\x0b2\x14.google.protobuf.AnyH\x01R\textension\x12K\n\x04dwrf\x18\r \x01(\x0b25.proto.ReadRel.LocalFiles.FileOrFiles.DwrfReadOptionsH\x01R\x04dwrf\x1a\x14\n\x12ParquetReadOptions\x1a\x12\n\x10ArrowReadOptions\x1a\x10\n\x0eOrcReadOptions\x1a\x11\n\x0fDwrfReadOptionsB\x0b\n\tpath_typeB\r\n\x0bfile_formatJ\x04\x08\x05\x10\x06R\x06formatB\x0b\n\tread_type"\xe1\x01\n\nProjectRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12 \n\x05input\x18\x02 \x01(\x0b2\n.proto.RelR\x05input\x123\n\x0bexpressions\x18\x03 \x03(\x0b2\x11.proto.ExpressionR\x0bexpressions\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\x9f\x04\n\x07JoinRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12\x1e\n\x04left\x18\x02 \x01(\x0b2\n.proto.RelR\x04left\x12 \n\x05right\x18\x03 \x01(\x0b2\n.proto.RelR\x05right\x121\n\nexpression\x18\x04 \x01(\x0b2\x11.proto.ExpressionR\nexpression\x12;\n\x10post_join_filter\x18\x05 \x01(\x0b2\x11.proto.ExpressionR\x0epostJoinFilter\x12+\n\x04type\x18\x06 \x01(\x0e2\x17.proto.JoinRel.JoinTypeR\x04type\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\xb6\x01\n\x08JoinType\x12\x19\n\x15JOIN_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fJOIN_TYPE_INNER\x10\x01\x12\x13\n\x0fJOIN_TYPE_OUTER\x10\x02\x12\x12\n\x0eJOIN_TYPE_LEFT\x10\x03\x12\x13\n\x0fJOIN_TYPE_RIGHT\x10\x04\x12\x12\n\x0eJOIN_TYPE_SEMI\x10\x05\x12\x12\n\x0eJOIN_TYPE_ANTI\x10\x06\x12\x14\n\x10JOIN_TYPE_SINGLE\x10\x07"\xca\x01\n\x08CrossRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12\x1e\n\x04left\x18\x02 \x01(\x0b2\n.proto.RelR\x04left\x12 \n\x05right\x18\x03 \x01(\x0b2\n.proto.RelR\x05right\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\xd8\x01\n\x08FetchRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12 \n\x05input\x18\x02 \x01(\x0b2\n.proto.RelR\x05input\x12\x16\n\x06offset\x18\x03 \x01(\x03R\x06offset\x12\x14\n\x05count\x18\x04 \x01(\x03R\x05count\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\xdf\x03\n\x0cAggregateRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12 \n\x05input\x18\x02 \x01(\x0b2\n.proto.RelR\x05input\x12:\n\tgroupings\x18\x03 \x03(\x0b2\x1c.proto.AggregateRel.GroupingR\tgroupings\x127\n\x08measures\x18\x04 \x03(\x0b2\x1b.proto.AggregateRel.MeasureR\x08measures\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x1aP\n\x08Grouping\x12D\n\x14grouping_expressions\x18\x01 \x03(\x0b2\x11.proto.ExpressionR\x13groupingExpressions\x1ah\n\x07Measure\x122\n\x07measure\x18\x01 \x01(\x0b2\x18.proto.AggregateFunctionR\x07measure\x12)\n\x06filter\x18\x02 \x01(\x0b2\x11.proto.ExpressionR\x06filter"\xd1\x01\n\x07SortRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12 \n\x05input\x18\x02 \x01(\x0b2\n.proto.RelR\x05input\x12&\n\x05sorts\x18\x03 \x03(\x0b2\x10.proto.SortFieldR\x05sorts\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\xdc\x01\n\tFilterRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12 \n\x05input\x18\x02 \x01(\x0b2\n.proto.RelR\x05input\x12/\n\tcondition\x18\x03 \x01(\x0b2\x11.proto.ExpressionR\tcondition\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\x9a\x03\n\x06SetRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12"\n\x06inputs\x18\x02 \x03(\x0b2\n.proto.RelR\x06inputs\x12#\n\x02op\x18\x03 \x01(\x0e2\x13.proto.SetRel.SetOpR\x02op\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\xc8\x01\n\x05SetOp\x12\x16\n\x12SET_OP_UNSPECIFIED\x10\x00\x12\x18\n\x14SET_OP_MINUS_PRIMARY\x10\x01\x12\x19\n\x15SET_OP_MINUS_MULTISET\x10\x02\x12\x1f\n\x1bSET_OP_INTERSECTION_PRIMARY\x10\x03\x12 \n\x1cSET_OP_INTERSECTION_MULTISET\x10\x04\x12\x19\n\x15SET_OP_UNION_DISTINCT\x10\x05\x12\x14\n\x10SET_OP_UNION_ALL\x10\x06"\x8e\x01\n\x12ExtensionSingleRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12 \n\x05input\x18\x02 \x01(\x0b2\n.proto.RelR\x05input\x12,\n\x06detail\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyR\x06detail"j\n\x10ExtensionLeafRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12,\n\x06detail\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x06detail"\x8f\x01\n\x11ExtensionMultiRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12"\n\x06inputs\x18\x02 \x03(\x0b2\n.proto.RelR\x06inputs\x12,\n\x06detail\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyR\x06detail"\xe9\x08\n\x0bExchangeRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12 \n\x05input\x18\x02 \x01(\x0b2\n.proto.RelR\x05input\x12\'\n\x0fpartition_count\x18\x03 \x01(\x05R\x0epartitionCount\x12;\n\x07targets\x18\x04 \x03(\x0b2!.proto.ExchangeRel.ExchangeTargetR\x07targets\x12N\n\x11scatter_by_fields\x18\x05 \x01(\x0b2 .proto.ExchangeRel.ScatterFieldsH\x00R\x0fscatterByFields\x12P\n\rsingle_target\x18\x06 \x01(\x0b2).proto.ExchangeRel.SingleBucketExpressionH\x00R\x0csingleTarget\x12M\n\x0cmulti_target\x18\x07 \x01(\x0b2(.proto.ExchangeRel.MultiBucketExpressionH\x00R\x0bmultiTarget\x12@\n\x0bround_robin\x18\x08 \x01(\x0b2\x1d.proto.ExchangeRel.RoundRobinH\x00R\nroundRobin\x12<\n\tbroadcast\x18\t \x01(\x0b2\x1c.proto.ExchangeRel.BroadcastH\x00R\tbroadcast\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension\x1aI\n\rScatterFields\x128\n\x06fields\x18\x01 \x03(\x0b2 .proto.Expression.FieldReferenceR\x06fields\x1aK\n\x16SingleBucketExpression\x121\n\nexpression\x18\x01 \x01(\x0b2\x11.proto.ExpressionR\nexpression\x1a|\n\x15MultiBucketExpression\x121\n\nexpression\x18\x01 \x01(\x0b2\x11.proto.ExpressionR\nexpression\x120\n\x14constrained_to_count\x18\x02 \x01(\x08R\x12constrainedToCount\x1a\x0b\n\tBroadcast\x1a"\n\nRoundRobin\x12\x14\n\x05exact\x18\x01 \x01(\x08R\x05exact\x1a\x8a\x01\n\x0eExchangeTarget\x12!\n\x0cpartition_id\x18\x01 \x03(\x05R\x0bpartitionId\x12\x12\n\x03uri\x18\x02 \x01(\tH\x00R\x03uri\x122\n\x08extended\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyH\x00R\x08extendedB\r\n\x0btarget_typeB\x0f\n\rexchange_kind"A\n\x07RelRoot\x12 \n\x05input\x18\x01 \x01(\x0b2\n.proto.RelR\x05input\x12\x14\n\x05names\x18\x02 \x03(\tR\x05names"\xc0\x05\n\x03Rel\x12$\n\x04read\x18\x01 \x01(\x0b2\x0e.proto.ReadRelH\x00R\x04read\x12*\n\x06filter\x18\x02 \x01(\x0b2\x10.proto.FilterRelH\x00R\x06filter\x12\'\n\x05fetch\x18\x03 \x01(\x0b2\x0f.proto.FetchRelH\x00R\x05fetch\x123\n\taggregate\x18\x04 \x01(\x0b2\x13.proto.AggregateRelH\x00R\taggregate\x12$\n\x04sort\x18\x05 \x01(\x0b2\x0e.proto.SortRelH\x00R\x04sort\x12$\n\x04join\x18\x06 \x01(\x0b2\x0e.proto.JoinRelH\x00R\x04join\x12-\n\x07project\x18\x07 \x01(\x0b2\x11.proto.ProjectRelH\x00R\x07project\x12!\n\x03set\x18\x08 \x01(\x0b2\r.proto.SetRelH\x00R\x03set\x12F\n\x10extension_single\x18\t \x01(\x0b2\x19.proto.ExtensionSingleRelH\x00R\x0fextensionSingle\x12C\n\x0fextension_multi\x18\n \x01(\x0b2\x18.proto.ExtensionMultiRelH\x00R\x0eextensionMulti\x12@\n\x0eextension_leaf\x18\x0b \x01(\x0b2\x17.proto.ExtensionLeafRelH\x00R\rextensionLeaf\x12\'\n\x05cross\x18\x0c \x01(\x0b2\x0f.proto.CrossRelH\x00R\x05cross\x121\n\thash_join\x18\r \x01(\x0b2\x12.proto.HashJoinRelH\x00R\x08hashJoin\x124\n\nmerge_join\x18\x0e \x01(\x0b2\x13.proto.MergeJoinRelH\x00R\tmergeJoinB\n\n\x08rel_type"|\n\x10NamedObjectWrite\x12\x14\n\x05names\x18\x01 \x03(\tR\x05names\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"?\n\x0fExtensionObject\x12,\n\x06detail\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyR\x06detail"\x88\x05\n\x06DdlRel\x12<\n\x0cnamed_object\x18\x01 \x01(\x0b2\x17.proto.NamedObjectWriteH\x00R\x0bnamedObject\x12C\n\x10extension_object\x18\x02 \x01(\x0b2\x16.proto.ExtensionObjectH\x00R\x0fextensionObject\x125\n\x0ctable_schema\x18\x03 \x01(\x0b2\x12.proto.NamedStructR\x0btableSchema\x12G\n\x0etable_defaults\x18\x04 \x01(\x0b2 .proto.Expression.Literal.StructR\rtableDefaults\x12/\n\x06object\x18\x05 \x01(\x0e2\x17.proto.DdlRel.DdlObjectR\x06object\x12#\n\x02op\x18\x06 \x01(\x0e2\x13.proto.DdlRel.DdlOpR\x02op\x123\n\x0fview_definition\x18\x07 \x01(\x0b2\n.proto.RelR\x0eviewDefinition"R\n\tDdlObject\x12\x1a\n\x16DDL_OBJECT_UNSPECIFIED\x10\x00\x12\x14\n\x10DDL_OBJECT_TABLE\x10\x01\x12\x13\n\x0fDDL_OBJECT_VIEW\x10\x02"\x8d\x01\n\x05DdlOp\x12\x16\n\x12DDL_OP_UNSPECIFIED\x10\x00\x12\x11\n\rDDL_OP_CREATE\x10\x01\x12\x1c\n\x18DDL_OP_CREATE_OR_REPLACE\x10\x02\x12\x10\n\x0cDDL_OP_ALTER\x10\x03\x12\x0f\n\x0bDDL_OP_DROP\x10\x04\x12\x18\n\x14DDL_OP_DROP_IF_EXIST\x10\x05B\x0c\n\nwrite_type"\xab\x04\n\x08WriteRel\x12:\n\x0bnamed_table\x18\x01 \x01(\x0b2\x17.proto.NamedObjectWriteH\x00R\nnamedTable\x12A\n\x0fextension_table\x18\x02 \x01(\x0b2\x16.proto.ExtensionObjectH\x00R\x0eextensionTable\x125\n\x0ctable_schema\x18\x03 \x01(\x0b2\x12.proto.NamedStructR\x0btableSchema\x12\'\n\x02op\x18\x04 \x01(\x0e2\x17.proto.WriteRel.WriteOpR\x02op\x12 \n\x05input\x18\x05 \x01(\x0b2\n.proto.RelR\x05input\x122\n\x06output\x18\x06 \x01(\x0e2\x1a.proto.WriteRel.OutputModeR\x06output"u\n\x07WriteOp\x12\x18\n\x14WRITE_OP_UNSPECIFIED\x10\x00\x12\x13\n\x0fWRITE_OP_INSERT\x10\x01\x12\x13\n\x0fWRITE_OP_DELETE\x10\x02\x12\x13\n\x0fWRITE_OP_UPDATE\x10\x03\x12\x11\n\rWRITE_OP_CTAS\x10\x04"e\n\nOutputMode\x12\x1b\n\x17OUTPUT_MODE_UNSPECIFIED\x10\x00\x12\x19\n\x15OUTPUT_MODE_NO_OUTPUT\x10\x01\x12\x1f\n\x1bOUTPUT_MODE_MODIFIED_TUPLES\x10\x02B\x0c\n\nwrite_type"\x9c\x05\n\x0bHashJoinRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12\x1e\n\x04left\x18\x02 \x01(\x0b2\n.proto.RelR\x04left\x12 \n\x05right\x18\x03 \x01(\x0b2\n.proto.RelR\x05right\x12=\n\tleft_keys\x18\x04 \x03(\x0b2 .proto.Expression.FieldReferenceR\x08leftKeys\x12?\n\nright_keys\x18\x05 \x03(\x0b2 .proto.Expression.FieldReferenceR\trightKeys\x12;\n\x10post_join_filter\x18\x06 \x01(\x0b2\x11.proto.ExpressionR\x0epostJoinFilter\x12/\n\x04type\x18\x07 \x01(\x0e2\x1b.proto.HashJoinRel.JoinTypeR\x04type\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\xde\x01\n\x08JoinType\x12\x19\n\x15JOIN_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fJOIN_TYPE_INNER\x10\x01\x12\x13\n\x0fJOIN_TYPE_OUTER\x10\x02\x12\x12\n\x0eJOIN_TYPE_LEFT\x10\x03\x12\x13\n\x0fJOIN_TYPE_RIGHT\x10\x04\x12\x17\n\x13JOIN_TYPE_LEFT_SEMI\x10\x05\x12\x18\n\x14JOIN_TYPE_RIGHT_SEMI\x10\x06\x12\x17\n\x13JOIN_TYPE_LEFT_ANTI\x10\x07\x12\x18\n\x14JOIN_TYPE_RIGHT_ANTI\x10\x08"\x9e\x05\n\x0cMergeJoinRel\x12(\n\x06common\x18\x01 \x01(\x0b2\x10.proto.RelCommonR\x06common\x12\x1e\n\x04left\x18\x02 \x01(\x0b2\n.proto.RelR\x04left\x12 \n\x05right\x18\x03 \x01(\x0b2\n.proto.RelR\x05right\x12=\n\tleft_keys\x18\x04 \x03(\x0b2 .proto.Expression.FieldReferenceR\x08leftKeys\x12?\n\nright_keys\x18\x05 \x03(\x0b2 .proto.Expression.FieldReferenceR\trightKeys\x12;\n\x10post_join_filter\x18\x06 \x01(\x0b2\x11.proto.ExpressionR\x0epostJoinFilter\x120\n\x04type\x18\x07 \x01(\x0e2\x1c.proto.MergeJoinRel.JoinTypeR\x04type\x12R\n\x12advanced_extension\x18\n \x01(\x0b2#.proto.extensions.AdvancedExtensionR\x11advancedExtension"\xde\x01\n\x08JoinType\x12\x19\n\x15JOIN_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fJOIN_TYPE_INNER\x10\x01\x12\x13\n\x0fJOIN_TYPE_OUTER\x10\x02\x12\x12\n\x0eJOIN_TYPE_LEFT\x10\x03\x12\x13\n\x0fJOIN_TYPE_RIGHT\x10\x04\x12\x17\n\x13JOIN_TYPE_LEFT_SEMI\x10\x05\x12\x18\n\x14JOIN_TYPE_RIGHT_SEMI\x10\x06\x12\x17\n\x13JOIN_TYPE_LEFT_ANTI\x10\x07\x12\x18\n\x14JOIN_TYPE_RIGHT_ANTI\x10\x08"\x82\x01\n\x10FunctionArgument\x12\x14\n\x04enum\x18\x01 \x01(\tH\x00R\x04enum\x12!\n\x04type\x18\x02 \x01(\x0b2\x0b.proto.TypeH\x00R\x04type\x12)\n\x05value\x18\x03 \x01(\x0b2\x11.proto.ExpressionH\x00R\x05valueB\n\n\x08arg_type"D\n\x0eFunctionOption\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1e\n\npreference\x18\x02 \x03(\tR\npreference"\xebN\n\nExpression\x125\n\x07literal\x18\x01 \x01(\x0b2\x19.proto.Expression.LiteralH\x00R\x07literal\x12@\n\tselection\x18\x02 \x01(\x0b2 .proto.Expression.FieldReferenceH\x00R\tselection\x12K\n\x0fscalar_function\x18\x03 \x01(\x0b2 .proto.Expression.ScalarFunctionH\x00R\x0escalarFunction\x12K\n\x0fwindow_function\x18\x05 \x01(\x0b2 .proto.Expression.WindowFunctionH\x00R\x0ewindowFunction\x123\n\x07if_then\x18\x06 \x01(\x0b2\x18.proto.Expression.IfThenH\x00R\x06ifThen\x12Q\n\x11switch_expression\x18\x07 \x01(\x0b2".proto.Expression.SwitchExpressionH\x00R\x10switchExpression\x12L\n\x10singular_or_list\x18\x08 \x01(\x0b2 .proto.Expression.SingularOrListH\x00R\x0esingularOrList\x12C\n\rmulti_or_list\x18\t \x01(\x0b2\x1d.proto.Expression.MultiOrListH\x00R\x0bmultiOrList\x12,\n\x04cast\x18\x0b \x01(\x0b2\x16.proto.Expression.CastH\x00R\x04cast\x128\n\x08subquery\x18\x0c \x01(\x0b2\x1a.proto.Expression.SubqueryH\x00R\x08subquery\x122\n\x06nested\x18\r \x01(\x0b2\x18.proto.Expression.NestedH\x00R\x06nested\x120\n\x04enum\x18\n \x01(\x0b2\x16.proto.Expression.EnumB\x02\x18\x01H\x00R\x04enum\x1a\x86\x01\n\x04Enum\x12\x1e\n\tspecified\x18\x01 \x01(\tH\x00R\tspecified\x12@\n\x0bunspecified\x18\x02 \x01(\x0b2\x1c.proto.Expression.Enum.EmptyH\x00R\x0bunspecified\x1a\x0b\n\x05Empty:\x02\x18\x01:\x02\x18\x01B\x0b\n\tenum_kind\x1a\xd8\x0f\n\x07Literal\x12\x1a\n\x07boolean\x18\x01 \x01(\x08H\x00R\x07boolean\x12\x10\n\x02i8\x18\x02 \x01(\x05H\x00R\x02i8\x12\x12\n\x03i16\x18\x03 \x01(\x05H\x00R\x03i16\x12\x12\n\x03i32\x18\x05 \x01(\x05H\x00R\x03i32\x12\x12\n\x03i64\x18\x07 \x01(\x03H\x00R\x03i64\x12\x14\n\x04fp32\x18\n \x01(\x02H\x00R\x04fp32\x12\x14\n\x04fp64\x18\x0b \x01(\x01H\x00R\x04fp64\x12\x18\n\x06string\x18\x0c \x01(\tH\x00R\x06string\x12\x18\n\x06binary\x18\r \x01(\x0cH\x00R\x06binary\x12\x1e\n\ttimestamp\x18\x0e \x01(\x03H\x00R\ttimestamp\x12\x14\n\x04date\x18\x10 \x01(\x05H\x00R\x04date\x12\x14\n\x04time\x18\x11 \x01(\x03H\x00R\x04time\x12d\n\x16interval_year_to_month\x18\x13 \x01(\x0b2-.proto.Expression.Literal.IntervalYearToMonthH\x00R\x13intervalYearToMonth\x12d\n\x16interval_day_to_second\x18\x14 \x01(\x0b2-.proto.Expression.Literal.IntervalDayToSecondH\x00R\x13intervalDayToSecond\x12\x1f\n\nfixed_char\x18\x15 \x01(\tH\x00R\tfixedChar\x12>\n\x08var_char\x18\x16 \x01(\x0b2!.proto.Expression.Literal.VarCharH\x00R\x07varChar\x12#\n\x0cfixed_binary\x18\x17 \x01(\x0cH\x00R\x0bfixedBinary\x12=\n\x07decimal\x18\x18 \x01(\x0b2!.proto.Expression.Literal.DecimalH\x00R\x07decimal\x12:\n\x06struct\x18\x19 \x01(\x0b2 .proto.Expression.Literal.StructH\x00R\x06struct\x121\n\x03map\x18\x1a \x01(\x0b2\x1d.proto.Expression.Literal.MapH\x00R\x03map\x12#\n\x0ctimestamp_tz\x18\x1b \x01(\x03H\x00R\x0btimestampTz\x12\x14\n\x04uuid\x18\x1c \x01(\x0cH\x00R\x04uuid\x12!\n\x04null\x18\x1d \x01(\x0b2\x0b.proto.TypeH\x00R\x04null\x124\n\x04list\x18\x1e \x01(\x0b2\x1e.proto.Expression.Literal.ListH\x00R\x04list\x121\n\nempty_list\x18\x1f \x01(\x0b2\x10.proto.Type.ListH\x00R\temptyList\x12.\n\tempty_map\x18  \x01(\x0b2\x0f.proto.Type.MapH\x00R\x08emptyMap\x12J\n\x0cuser_defined\x18! \x01(\x0b2%.proto.Expression.Literal.UserDefinedH\x00R\x0buserDefined\x12\x1a\n\x08nullable\x182 \x01(\x08R\x08nullable\x128\n\x18type_variation_reference\x183 \x01(\rR\x16typeVariationReference\x1a7\n\x07VarChar\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x16\n\x06length\x18\x02 \x01(\rR\x06length\x1aS\n\x07Decimal\x12\x14\n\x05value\x18\x01 \x01(\x0cR\x05value\x12\x1c\n\tprecision\x18\x02 \x01(\x05R\tprecision\x12\x14\n\x05scale\x18\x03 \x01(\x05R\x05scale\x1a\xb6\x01\n\x03Map\x12E\n\nkey_values\x18\x01 \x03(\x0b2&.proto.Expression.Literal.Map.KeyValueR\tkeyValues\x1ah\n\x08KeyValue\x12+\n\x03key\x18\x01 \x01(\x0b2\x19.proto.Expression.LiteralR\x03key\x12/\n\x05value\x18\x02 \x01(\x0b2\x19.proto.Expression.LiteralR\x05value\x1aC\n\x13IntervalYearToMonth\x12\x14\n\x05years\x18\x01 \x01(\x05R\x05years\x12\x16\n\x06months\x18\x02 \x01(\x05R\x06months\x1ag\n\x13IntervalDayToSecond\x12\x12\n\x04days\x18\x01 \x01(\x05R\x04days\x12\x18\n\x07seconds\x18\x02 \x01(\x05R\x07seconds\x12"\n\x0cmicroseconds\x18\x03 \x01(\x05R\x0cmicroseconds\x1a;\n\x06Struct\x121\n\x06fields\x18\x01 \x03(\x0b2\x19.proto.Expression.LiteralR\x06fields\x1a9\n\x04List\x121\n\x06values\x18\x01 \x03(\x0b2\x19.proto.Expression.LiteralR\x06values\x1a\xa0\x01\n\x0bUserDefined\x12%\n\x0etype_reference\x18\x01 \x01(\rR\rtypeReference\x12>\n\x0ftype_parameters\x18\x03 \x03(\x0b2\x15.proto.Type.ParameterR\x0etypeParameters\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05valueB\x0e\n\x0cliteral_type\x1a\x9f\x04\n\x06Nested\x12\x1a\n\x08nullable\x18\x01 \x01(\x08R\x08nullable\x128\n\x18type_variation_reference\x18\x02 \x01(\rR\x16typeVariationReference\x129\n\x06struct\x18\x03 \x01(\x0b2\x1f.proto.Expression.Nested.StructH\x00R\x06struct\x123\n\x04list\x18\x04 \x01(\x0b2\x1d.proto.Expression.Nested.ListH\x00R\x04list\x120\n\x03map\x18\x05 \x01(\x0b2\x1c.proto.Expression.Nested.MapH\x00R\x03map\x1a\xa5\x01\n\x03Map\x12D\n\nkey_values\x18\x01 \x03(\x0b2%.proto.Expression.Nested.Map.KeyValueR\tkeyValues\x1aX\n\x08KeyValue\x12#\n\x03key\x18\x01 \x01(\x0b2\x11.proto.ExpressionR\x03key\x12\'\n\x05value\x18\x02 \x01(\x0b2\x11.proto.ExpressionR\x05value\x1a3\n\x06Struct\x12)\n\x06fields\x18\x01 \x03(\x0b2\x11.proto.ExpressionR\x06fields\x1a1\n\x04List\x12)\n\x06values\x18\x01 \x03(\x0b2\x11.proto.ExpressionR\x06valuesB\r\n\x0bnested_type\x1a\x80\x02\n\x0eScalarFunction\x12-\n\x12function_reference\x18\x01 \x01(\rR\x11functionReference\x125\n\targuments\x18\x04 \x03(\x0b2\x17.proto.FunctionArgumentR\targuments\x12/\n\x07options\x18\x05 \x03(\x0b2\x15.proto.FunctionOptionR\x07options\x12,\n\x0boutput_type\x18\x03 \x01(\x0b2\x0b.proto.TypeR\noutputType\x12)\n\x04args\x18\x02 \x03(\x0b2\x11.proto.ExpressionB\x02\x18\x01R\x04args\x1a\xaf\x08\n\x0eWindowFunction\x12-\n\x12function_reference\x18\x01 \x01(\rR\x11functionReference\x125\n\targuments\x18\t \x03(\x0b2\x17.proto.FunctionArgumentR\targuments\x12/\n\x07options\x18\x0b \x03(\x0b2\x15.proto.FunctionOptionR\x07options\x12,\n\x0boutput_type\x18\x07 \x01(\x0b2\x0b.proto.TypeR\noutputType\x12-\n\x05phase\x18\x06 \x01(\x0e2\x17.proto.AggregationPhaseR\x05phase\x12&\n\x05sorts\x18\x03 \x03(\x0b2\x10.proto.SortFieldR\x05sorts\x12N\n\ninvocation\x18\n \x01(\x0e2..proto.AggregateFunction.AggregationInvocationR\ninvocation\x121\n\npartitions\x18\x02 \x03(\x0b2\x11.proto.ExpressionR\npartitions\x12G\n\x0blower_bound\x18\x05 \x01(\x0b2&.proto.Expression.WindowFunction.BoundR\nlowerBound\x12G\n\x0bupper_bound\x18\x04 \x01(\x0b2&.proto.Expression.WindowFunction.BoundR\nupperBound\x12)\n\x04args\x18\x08 \x03(\x0b2\x11.proto.ExpressionB\x02\x18\x01R\x04args\x1a\xc0\x03\n\x05Bound\x12P\n\tpreceding\x18\x01 \x01(\x0b20.proto.Expression.WindowFunction.Bound.PrecedingH\x00R\tpreceding\x12P\n\tfollowing\x18\x02 \x01(\x0b20.proto.Expression.WindowFunction.Bound.FollowingH\x00R\tfollowing\x12T\n\x0bcurrent_row\x18\x03 \x01(\x0b21.proto.Expression.WindowFunction.Bound.CurrentRowH\x00R\ncurrentRow\x12P\n\tunbounded\x18\x04 \x01(\x0b20.proto.Expression.WindowFunction.Bound.UnboundedH\x00R\tunbounded\x1a#\n\tPreceding\x12\x16\n\x06offset\x18\x01 \x01(\x03R\x06offset\x1a#\n\tFollowing\x12\x16\n\x06offset\x18\x01 \x01(\x03R\x06offset\x1a\x0c\n\nCurrentRow\x1a\x0b\n\tUnboundedB\x06\n\x04kind\x1a\xba\x01\n\x06IfThen\x123\n\x03ifs\x18\x01 \x03(\x0b2!.proto.Expression.IfThen.IfClauseR\x03ifs\x12%\n\x04else\x18\x02 \x01(\x0b2\x11.proto.ExpressionR\x04else\x1aT\n\x08IfClause\x12!\n\x02if\x18\x01 \x01(\x0b2\x11.proto.ExpressionR\x02if\x12%\n\x04then\x18\x02 \x01(\x0b2\x11.proto.ExpressionR\x04then\x1a\xa0\x02\n\x04Cast\x12\x1f\n\x04type\x18\x01 \x01(\x0b2\x0b.proto.TypeR\x04type\x12\'\n\x05input\x18\x02 \x01(\x0b2\x11.proto.ExpressionR\x05input\x12Q\n\x10failure_behavior\x18\x03 \x01(\x0e2&.proto.Expression.Cast.FailureBehaviorR\x0ffailureBehavior"{\n\x0fFailureBehavior\x12 \n\x1cFAILURE_BEHAVIOR_UNSPECIFIED\x10\x00\x12 \n\x1cFAILURE_BEHAVIOR_RETURN_NULL\x10\x01\x12$\n FAILURE_BEHAVIOR_THROW_EXCEPTION\x10\x02\x1a\xfd\x01\n\x10SwitchExpression\x12\'\n\x05match\x18\x03 \x01(\x0b2\x11.proto.ExpressionR\x05match\x12<\n\x03ifs\x18\x01 \x03(\x0b2*.proto.Expression.SwitchExpression.IfValueR\x03ifs\x12%\n\x04else\x18\x02 \x01(\x0b2\x11.proto.ExpressionR\x04else\x1a[\n\x07IfValue\x12)\n\x02if\x18\x01 \x01(\x0b2\x19.proto.Expression.LiteralR\x02if\x12%\n\x04then\x18\x02 \x01(\x0b2\x11.proto.ExpressionR\x04then\x1af\n\x0eSingularOrList\x12\'\n\x05value\x18\x01 \x01(\x0b2\x11.proto.ExpressionR\x05value\x12+\n\x07options\x18\x02 \x03(\x0b2\x11.proto.ExpressionR\x07options\x1a\xab\x01\n\x0bMultiOrList\x12\'\n\x05value\x18\x01 \x03(\x0b2\x11.proto.ExpressionR\x05value\x12>\n\x07options\x18\x02 \x03(\x0b2$.proto.Expression.MultiOrList.RecordR\x07options\x1a3\n\x06Record\x12)\n\x06fields\x18\x01 \x03(\x0b2\x11.proto.ExpressionR\x06fields\x1a\x83\x04\n\x10EmbeddedFunction\x12/\n\targuments\x18\x01 \x03(\x0b2\x11.proto.ExpressionR\targuments\x12,\n\x0boutput_type\x18\x02 \x01(\x0b2\x0b.proto.TypeR\noutputType\x12o\n\x16python_pickle_function\x18\x03 \x01(\x0b27.proto.Expression.EmbeddedFunction.PythonPickleFunctionH\x00R\x14pythonPickleFunction\x12l\n\x15web_assembly_function\x18\x04 \x01(\x0b26.proto.Expression.EmbeddedFunction.WebAssemblyFunctionH\x00R\x13webAssemblyFunction\x1aV\n\x14PythonPickleFunction\x12\x1a\n\x08function\x18\x01 \x01(\x0cR\x08function\x12"\n\x0cprerequisite\x18\x02 \x03(\tR\x0cprerequisite\x1aQ\n\x13WebAssemblyFunction\x12\x16\n\x06script\x18\x01 \x01(\x0cR\x06script\x12"\n\x0cprerequisite\x18\x02 \x03(\tR\x0cprerequisiteB\x06\n\x04kind\x1a\xcc\x04\n\x10ReferenceSegment\x12D\n\x07map_key\x18\x01 \x01(\x0b2).proto.Expression.ReferenceSegment.MapKeyH\x00R\x06mapKey\x12S\n\x0cstruct_field\x18\x02 \x01(\x0b2..proto.Expression.ReferenceSegment.StructFieldH\x00R\x0bstructField\x12S\n\x0clist_element\x18\x03 \x01(\x0b2..proto.Expression.ReferenceSegment.ListElementH\x00R\x0blistElement\x1av\n\x06MapKey\x122\n\x07map_key\x18\x01 \x01(\x0b2\x19.proto.Expression.LiteralR\x06mapKey\x128\n\x05child\x18\x02 \x01(\x0b2".proto.Expression.ReferenceSegmentR\x05child\x1a]\n\x0bStructField\x12\x14\n\x05field\x18\x01 \x01(\x05R\x05field\x128\n\x05child\x18\x02 \x01(\x0b2".proto.Expression.ReferenceSegmentR\x05child\x1a_\n\x0bListElement\x12\x16\n\x06offset\x18\x01 \x01(\x05R\x06offset\x128\n\x05child\x18\x02 \x01(\x0b2".proto.Expression.ReferenceSegmentR\x05childB\x10\n\x0ereference_type\x1a\xee\n\n\x0eMaskExpression\x12E\n\x06select\x18\x01 \x01(\x0b2-.proto.Expression.MaskExpression.StructSelectR\x06select\x128\n\x18maintain_singular_struct\x18\x02 \x01(\x08R\x16maintainSingularStruct\x1a\xdc\x01\n\x06Select\x12G\n\x06struct\x18\x01 \x01(\x0b2-.proto.Expression.MaskExpression.StructSelectH\x00R\x06struct\x12A\n\x04list\x18\x02 \x01(\x0b2+.proto.Expression.MaskExpression.ListSelectH\x00R\x04list\x12>\n\x03map\x18\x03 \x01(\x0b2*.proto.Expression.MaskExpression.MapSelectH\x00R\x03mapB\x06\n\x04type\x1a^\n\x0cStructSelect\x12N\n\x0cstruct_items\x18\x01 \x03(\x0b2+.proto.Expression.MaskExpression.StructItemR\x0bstructItems\x1aa\n\nStructItem\x12\x14\n\x05field\x18\x01 \x01(\x05R\x05field\x12=\n\x05child\x18\x02 \x01(\x0b2\'.proto.Expression.MaskExpression.SelectR\x05child\x1a\xd6\x03\n\nListSelect\x12X\n\tselection\x18\x01 \x03(\x0b2:.proto.Expression.MaskExpression.ListSelect.ListSelectItemR\tselection\x12=\n\x05child\x18\x02 \x01(\x0b2\'.proto.Expression.MaskExpression.SelectR\x05child\x1a\xae\x02\n\x0eListSelectItem\x12\\\n\x04item\x18\x01 \x01(\x0b2F.proto.Expression.MaskExpression.ListSelect.ListSelectItem.ListElementH\x00R\x04item\x12\\\n\x05slice\x18\x02 \x01(\x0b2D.proto.Expression.MaskExpression.ListSelect.ListSelectItem.ListSliceH\x00R\x05slice\x1a#\n\x0bListElement\x12\x14\n\x05field\x18\x01 \x01(\x05R\x05field\x1a3\n\tListSlice\x12\x14\n\x05start\x18\x01 \x01(\x05R\x05start\x12\x10\n\x03end\x18\x02 \x01(\x05R\x03endB\x06\n\x04type\x1a\xdf\x02\n\tMapSelect\x12E\n\x03key\x18\x01 \x01(\x0b21.proto.Expression.MaskExpression.MapSelect.MapKeyH\x00R\x03key\x12]\n\nexpression\x18\x02 \x01(\x0b2;.proto.Expression.MaskExpression.MapSelect.MapKeyExpressionH\x00R\nexpression\x12=\n\x05child\x18\x03 \x01(\x0b2\'.proto.Expression.MaskExpression.SelectR\x05child\x1a!\n\x06MapKey\x12\x17\n\x07map_key\x18\x01 \x01(\tR\x06mapKey\x1a@\n\x10MapKeyExpression\x12,\n\x12map_key_expression\x18\x01 \x01(\tR\x10mapKeyExpressionB\x08\n\x06select\x1a\xf9\x03\n\x0eFieldReference\x12O\n\x10direct_reference\x18\x01 \x01(\x0b2".proto.Expression.ReferenceSegmentH\x00R\x0fdirectReference\x12M\n\x10masked_reference\x18\x02 \x01(\x0b2 .proto.Expression.MaskExpressionH\x00R\x0fmaskedReference\x123\n\nexpression\x18\x03 \x01(\x0b2\x11.proto.ExpressionH\x01R\nexpression\x12W\n\x0eroot_reference\x18\x04 \x01(\x0b2..proto.Expression.FieldReference.RootReferenceH\x01R\rrootReference\x12Z\n\x0fouter_reference\x18\x05 \x01(\x0b2/.proto.Expression.FieldReference.OuterReferenceH\x01R\x0eouterReference\x1a\x0f\n\rRootReference\x1a-\n\x0eOuterReference\x12\x1b\n\tsteps_out\x18\x01 \x01(\rR\x08stepsOutB\x10\n\x0ereference_typeB\x0b\n\troot_type\x1a\xe1\t\n\x08Subquery\x12;\n\x06scalar\x18\x01 \x01(\x0b2!.proto.Expression.Subquery.ScalarH\x00R\x06scalar\x12K\n\x0cin_predicate\x18\x02 \x01(\x0b2&.proto.Expression.Subquery.InPredicateH\x00R\x0binPredicate\x12N\n\rset_predicate\x18\x03 \x01(\x0b2\'.proto.Expression.Subquery.SetPredicateH\x00R\x0csetPredicate\x12Q\n\x0eset_comparison\x18\x04 \x01(\x0b2(.proto.Expression.Subquery.SetComparisonH\x00R\rsetComparison\x1a*\n\x06Scalar\x12 \n\x05input\x18\x01 \x01(\x0b2\n.proto.RelR\x05input\x1ab\n\x0bInPredicate\x12+\n\x07needles\x18\x01 \x03(\x0b2\x11.proto.ExpressionR\x07needles\x12&\n\x08haystack\x18\x02 \x01(\x0b2\n.proto.RelR\x08haystack\x1a\xe9\x01\n\x0cSetPredicate\x12V\n\x0cpredicate_op\x18\x01 \x01(\x0e23.proto.Expression.Subquery.SetPredicate.PredicateOpR\x0bpredicateOp\x12"\n\x06tuples\x18\x02 \x01(\x0b2\n.proto.RelR\x06tuples"]\n\x0bPredicateOp\x12\x1c\n\x18PREDICATE_OP_UNSPECIFIED\x10\x00\x12\x17\n\x13PREDICATE_OP_EXISTS\x10\x01\x12\x17\n\x13PREDICATE_OP_UNIQUE\x10\x02\x1a\x9a\x04\n\rSetComparison\x12W\n\x0creduction_op\x18\x01 \x01(\x0e24.proto.Expression.Subquery.SetComparison.ReductionOpR\x0breductionOp\x12Z\n\rcomparison_op\x18\x02 \x01(\x0e25.proto.Expression.Subquery.SetComparison.ComparisonOpR\x0ccomparisonOp\x12%\n\x04left\x18\x03 \x01(\x0b2\x11.proto.ExpressionR\x04left\x12 \n\x05right\x18\x04 \x01(\x0b2\n.proto.RelR\x05right"\xb1\x01\n\x0cComparisonOp\x12\x1d\n\x19COMPARISON_OP_UNSPECIFIED\x10\x00\x12\x14\n\x10COMPARISON_OP_EQ\x10\x01\x12\x14\n\x10COMPARISON_OP_NE\x10\x02\x12\x14\n\x10COMPARISON_OP_LT\x10\x03\x12\x14\n\x10COMPARISON_OP_GT\x10\x04\x12\x14\n\x10COMPARISON_OP_LE\x10\x05\x12\x14\n\x10COMPARISON_OP_GE\x10\x06"W\n\x0bReductionOp\x12\x1c\n\x18REDUCTION_OP_UNSPECIFIED\x10\x00\x12\x14\n\x10REDUCTION_OP_ANY\x10\x01\x12\x14\n\x10REDUCTION_OP_ALL\x10\x02B\x0f\n\rsubquery_typeB\n\n\x08rex_type"\xa5\x03\n\tSortField\x12%\n\x04expr\x18\x01 \x01(\x0b2\x11.proto.ExpressionR\x04expr\x12>\n\tdirection\x18\x02 \x01(\x0e2\x1e.proto.SortField.SortDirectionH\x00R\tdirection\x12D\n\x1dcomparison_function_reference\x18\x03 \x01(\rH\x00R\x1bcomparisonFunctionReference"\xdd\x01\n\rSortDirection\x12\x1e\n\x1aSORT_DIRECTION_UNSPECIFIED\x10\x00\x12"\n\x1eSORT_DIRECTION_ASC_NULLS_FIRST\x10\x01\x12!\n\x1dSORT_DIRECTION_ASC_NULLS_LAST\x10\x02\x12#\n\x1fSORT_DIRECTION_DESC_NULLS_FIRST\x10\x03\x12"\n\x1eSORT_DIRECTION_DESC_NULLS_LAST\x10\x04\x12\x1c\n\x18SORT_DIRECTION_CLUSTERED\x10\x05B\x0b\n\tsort_kind"\xea\x04\n\x11AggregateFunction\x12-\n\x12function_reference\x18\x01 \x01(\rR\x11functionReference\x125\n\targuments\x18\x07 \x03(\x0b2\x17.proto.FunctionArgumentR\targuments\x12/\n\x07options\x18\x08 \x03(\x0b2\x15.proto.FunctionOptionR\x07options\x12,\n\x0boutput_type\x18\x05 \x01(\x0b2\x0b.proto.TypeR\noutputType\x12-\n\x05phase\x18\x04 \x01(\x0e2\x17.proto.AggregationPhaseR\x05phase\x12&\n\x05sorts\x18\x03 \x03(\x0b2\x10.proto.SortFieldR\x05sorts\x12N\n\ninvocation\x18\x06 \x01(\x0e2..proto.AggregateFunction.AggregationInvocationR\ninvocation\x12)\n\x04args\x18\x02 \x03(\x0b2\x11.proto.ExpressionB\x02\x18\x01R\x04args\x1a7\n\x0cReferenceRel\x12\'\n\x0fsubtree_ordinal\x18\x01 \x01(\x05R\x0esubtreeOrdinal"\x84\x01\n\x15AggregationInvocation\x12&\n"AGGREGATION_INVOCATION_UNSPECIFIED\x10\x00\x12\x1e\n\x1aAGGREGATION_INVOCATION_ALL\x10\x01\x12#\n\x1fAGGREGATION_INVOCATION_DISTINCT\x10\x02*\xef\x01\n\x10AggregationPhase\x12!\n\x1dAGGREGATION_PHASE_UNSPECIFIED\x10\x00\x12-\n)AGGREGATION_PHASE_INITIAL_TO_INTERMEDIATE\x10\x01\x122\n.AGGREGATION_PHASE_INTERMEDIATE_TO_INTERMEDIATE\x10\x02\x12\'\n#AGGREGATION_PHASE_INITIAL_TO_RESULT\x10\x03\x12,\n(AGGREGATION_PHASE_INTERMEDIATE_TO_RESULT\x10\x04B#\n\x0eio.proto.protoP\x01\xaa\x02\x0eProto.Protobufb\x06proto3')
_AGGREGATIONPHASE = DESCRIPTOR.enum_types_by_name['AggregationPhase']
AggregationPhase = enum_type_wrapper.EnumTypeWrapper(_AGGREGATIONPHASE)
AGGREGATION_PHASE_UNSPECIFIED = 0
AGGREGATION_PHASE_INITIAL_TO_INTERMEDIATE = 1
AGGREGATION_PHASE_INTERMEDIATE_TO_INTERMEDIATE = 2
AGGREGATION_PHASE_INITIAL_TO_RESULT = 3
AGGREGATION_PHASE_INTERMEDIATE_TO_RESULT = 4
_RELCOMMON = DESCRIPTOR.message_types_by_name['RelCommon']
_RELCOMMON_DIRECT = _RELCOMMON.nested_types_by_name['Direct']
_RELCOMMON_EMIT = _RELCOMMON.nested_types_by_name['Emit']
_RELCOMMON_HINT = _RELCOMMON.nested_types_by_name['Hint']
_RELCOMMON_HINT_STATS = _RELCOMMON_HINT.nested_types_by_name['Stats']
_RELCOMMON_HINT_RUNTIMECONSTRAINT = _RELCOMMON_HINT.nested_types_by_name['RuntimeConstraint']
_READREL = DESCRIPTOR.message_types_by_name['ReadRel']
_READREL_NAMEDTABLE = _READREL.nested_types_by_name['NamedTable']
_READREL_VIRTUALTABLE = _READREL.nested_types_by_name['VirtualTable']
_READREL_EXTENSIONTABLE = _READREL.nested_types_by_name['ExtensionTable']
_READREL_LOCALFILES = _READREL.nested_types_by_name['LocalFiles']
_READREL_LOCALFILES_FILEORFILES = _READREL_LOCALFILES.nested_types_by_name['FileOrFiles']
_READREL_LOCALFILES_FILEORFILES_PARQUETREADOPTIONS = _READREL_LOCALFILES_FILEORFILES.nested_types_by_name['ParquetReadOptions']
_READREL_LOCALFILES_FILEORFILES_ARROWREADOPTIONS = _READREL_LOCALFILES_FILEORFILES.nested_types_by_name['ArrowReadOptions']
_READREL_LOCALFILES_FILEORFILES_ORCREADOPTIONS = _READREL_LOCALFILES_FILEORFILES.nested_types_by_name['OrcReadOptions']
_READREL_LOCALFILES_FILEORFILES_DWRFREADOPTIONS = _READREL_LOCALFILES_FILEORFILES.nested_types_by_name['DwrfReadOptions']
_PROJECTREL = DESCRIPTOR.message_types_by_name['ProjectRel']
_JOINREL = DESCRIPTOR.message_types_by_name['JoinRel']
_CROSSREL = DESCRIPTOR.message_types_by_name['CrossRel']
_FETCHREL = DESCRIPTOR.message_types_by_name['FetchRel']
_AGGREGATEREL = DESCRIPTOR.message_types_by_name['AggregateRel']
_AGGREGATEREL_GROUPING = _AGGREGATEREL.nested_types_by_name['Grouping']
_AGGREGATEREL_MEASURE = _AGGREGATEREL.nested_types_by_name['Measure']
_SORTREL = DESCRIPTOR.message_types_by_name['SortRel']
_FILTERREL = DESCRIPTOR.message_types_by_name['FilterRel']
_SETREL = DESCRIPTOR.message_types_by_name['SetRel']
_EXTENSIONSINGLEREL = DESCRIPTOR.message_types_by_name['ExtensionSingleRel']
_EXTENSIONLEAFREL = DESCRIPTOR.message_types_by_name['ExtensionLeafRel']
_EXTENSIONMULTIREL = DESCRIPTOR.message_types_by_name['ExtensionMultiRel']
_EXCHANGEREL = DESCRIPTOR.message_types_by_name['ExchangeRel']
_EXCHANGEREL_SCATTERFIELDS = _EXCHANGEREL.nested_types_by_name['ScatterFields']
_EXCHANGEREL_SINGLEBUCKETEXPRESSION = _EXCHANGEREL.nested_types_by_name['SingleBucketExpression']
_EXCHANGEREL_MULTIBUCKETEXPRESSION = _EXCHANGEREL.nested_types_by_name['MultiBucketExpression']
_EXCHANGEREL_BROADCAST = _EXCHANGEREL.nested_types_by_name['Broadcast']
_EXCHANGEREL_ROUNDROBIN = _EXCHANGEREL.nested_types_by_name['RoundRobin']
_EXCHANGEREL_EXCHANGETARGET = _EXCHANGEREL.nested_types_by_name['ExchangeTarget']
_RELROOT = DESCRIPTOR.message_types_by_name['RelRoot']
_REL = DESCRIPTOR.message_types_by_name['Rel']
_NAMEDOBJECTWRITE = DESCRIPTOR.message_types_by_name['NamedObjectWrite']
_EXTENSIONOBJECT = DESCRIPTOR.message_types_by_name['ExtensionObject']
_DDLREL = DESCRIPTOR.message_types_by_name['DdlRel']
_WRITEREL = DESCRIPTOR.message_types_by_name['WriteRel']
_HASHJOINREL = DESCRIPTOR.message_types_by_name['HashJoinRel']
_MERGEJOINREL = DESCRIPTOR.message_types_by_name['MergeJoinRel']
_FUNCTIONARGUMENT = DESCRIPTOR.message_types_by_name['FunctionArgument']
_FUNCTIONOPTION = DESCRIPTOR.message_types_by_name['FunctionOption']
_EXPRESSION = DESCRIPTOR.message_types_by_name['Expression']
_EXPRESSION_ENUM = _EXPRESSION.nested_types_by_name['Enum']
_EXPRESSION_ENUM_EMPTY = _EXPRESSION_ENUM.nested_types_by_name['Empty']
_EXPRESSION_LITERAL = _EXPRESSION.nested_types_by_name['Literal']
_EXPRESSION_LITERAL_VARCHAR = _EXPRESSION_LITERAL.nested_types_by_name['VarChar']
_EXPRESSION_LITERAL_DECIMAL = _EXPRESSION_LITERAL.nested_types_by_name['Decimal']
_EXPRESSION_LITERAL_MAP = _EXPRESSION_LITERAL.nested_types_by_name['Map']
_EXPRESSION_LITERAL_MAP_KEYVALUE = _EXPRESSION_LITERAL_MAP.nested_types_by_name['KeyValue']
_EXPRESSION_LITERAL_INTERVALYEARTOMONTH = _EXPRESSION_LITERAL.nested_types_by_name['IntervalYearToMonth']
_EXPRESSION_LITERAL_INTERVALDAYTOSECOND = _EXPRESSION_LITERAL.nested_types_by_name['IntervalDayToSecond']
_EXPRESSION_LITERAL_STRUCT = _EXPRESSION_LITERAL.nested_types_by_name['Struct']
_EXPRESSION_LITERAL_LIST = _EXPRESSION_LITERAL.nested_types_by_name['List']
_EXPRESSION_LITERAL_USERDEFINED = _EXPRESSION_LITERAL.nested_types_by_name['UserDefined']
_EXPRESSION_NESTED = _EXPRESSION.nested_types_by_name['Nested']
_EXPRESSION_NESTED_MAP = _EXPRESSION_NESTED.nested_types_by_name['Map']
_EXPRESSION_NESTED_MAP_KEYVALUE = _EXPRESSION_NESTED_MAP.nested_types_by_name['KeyValue']
_EXPRESSION_NESTED_STRUCT = _EXPRESSION_NESTED.nested_types_by_name['Struct']
_EXPRESSION_NESTED_LIST = _EXPRESSION_NESTED.nested_types_by_name['List']
_EXPRESSION_SCALARFUNCTION = _EXPRESSION.nested_types_by_name['ScalarFunction']
_EXPRESSION_WINDOWFUNCTION = _EXPRESSION.nested_types_by_name['WindowFunction']
_EXPRESSION_WINDOWFUNCTION_BOUND = _EXPRESSION_WINDOWFUNCTION.nested_types_by_name['Bound']
_EXPRESSION_WINDOWFUNCTION_BOUND_PRECEDING = _EXPRESSION_WINDOWFUNCTION_BOUND.nested_types_by_name['Preceding']
_EXPRESSION_WINDOWFUNCTION_BOUND_FOLLOWING = _EXPRESSION_WINDOWFUNCTION_BOUND.nested_types_by_name['Following']
_EXPRESSION_WINDOWFUNCTION_BOUND_CURRENTROW = _EXPRESSION_WINDOWFUNCTION_BOUND.nested_types_by_name['CurrentRow']
_EXPRESSION_WINDOWFUNCTION_BOUND_UNBOUNDED = _EXPRESSION_WINDOWFUNCTION_BOUND.nested_types_by_name['Unbounded']
_EXPRESSION_IFTHEN = _EXPRESSION.nested_types_by_name['IfThen']
_EXPRESSION_IFTHEN_IFCLAUSE = _EXPRESSION_IFTHEN.nested_types_by_name['IfClause']
_EXPRESSION_CAST = _EXPRESSION.nested_types_by_name['Cast']
_EXPRESSION_SWITCHEXPRESSION = _EXPRESSION.nested_types_by_name['SwitchExpression']
_EXPRESSION_SWITCHEXPRESSION_IFVALUE = _EXPRESSION_SWITCHEXPRESSION.nested_types_by_name['IfValue']
_EXPRESSION_SINGULARORLIST = _EXPRESSION.nested_types_by_name['SingularOrList']
_EXPRESSION_MULTIORLIST = _EXPRESSION.nested_types_by_name['MultiOrList']
_EXPRESSION_MULTIORLIST_RECORD = _EXPRESSION_MULTIORLIST.nested_types_by_name['Record']
_EXPRESSION_EMBEDDEDFUNCTION = _EXPRESSION.nested_types_by_name['EmbeddedFunction']
_EXPRESSION_EMBEDDEDFUNCTION_PYTHONPICKLEFUNCTION = _EXPRESSION_EMBEDDEDFUNCTION.nested_types_by_name['PythonPickleFunction']
_EXPRESSION_EMBEDDEDFUNCTION_WEBASSEMBLYFUNCTION = _EXPRESSION_EMBEDDEDFUNCTION.nested_types_by_name['WebAssemblyFunction']
_EXPRESSION_REFERENCESEGMENT = _EXPRESSION.nested_types_by_name['ReferenceSegment']
_EXPRESSION_REFERENCESEGMENT_MAPKEY = _EXPRESSION_REFERENCESEGMENT.nested_types_by_name['MapKey']
_EXPRESSION_REFERENCESEGMENT_STRUCTFIELD = _EXPRESSION_REFERENCESEGMENT.nested_types_by_name['StructField']
_EXPRESSION_REFERENCESEGMENT_LISTELEMENT = _EXPRESSION_REFERENCESEGMENT.nested_types_by_name['ListElement']
_EXPRESSION_MASKEXPRESSION = _EXPRESSION.nested_types_by_name['MaskExpression']
_EXPRESSION_MASKEXPRESSION_SELECT = _EXPRESSION_MASKEXPRESSION.nested_types_by_name['Select']
_EXPRESSION_MASKEXPRESSION_STRUCTSELECT = _EXPRESSION_MASKEXPRESSION.nested_types_by_name['StructSelect']
_EXPRESSION_MASKEXPRESSION_STRUCTITEM = _EXPRESSION_MASKEXPRESSION.nested_types_by_name['StructItem']
_EXPRESSION_MASKEXPRESSION_LISTSELECT = _EXPRESSION_MASKEXPRESSION.nested_types_by_name['ListSelect']
_EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM = _EXPRESSION_MASKEXPRESSION_LISTSELECT.nested_types_by_name['ListSelectItem']
_EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTELEMENT = _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM.nested_types_by_name['ListElement']
_EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTSLICE = _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM.nested_types_by_name['ListSlice']
_EXPRESSION_MASKEXPRESSION_MAPSELECT = _EXPRESSION_MASKEXPRESSION.nested_types_by_name['MapSelect']
_EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEY = _EXPRESSION_MASKEXPRESSION_MAPSELECT.nested_types_by_name['MapKey']
_EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEYEXPRESSION = _EXPRESSION_MASKEXPRESSION_MAPSELECT.nested_types_by_name['MapKeyExpression']
_EXPRESSION_FIELDREFERENCE = _EXPRESSION.nested_types_by_name['FieldReference']
_EXPRESSION_FIELDREFERENCE_ROOTREFERENCE = _EXPRESSION_FIELDREFERENCE.nested_types_by_name['RootReference']
_EXPRESSION_FIELDREFERENCE_OUTERREFERENCE = _EXPRESSION_FIELDREFERENCE.nested_types_by_name['OuterReference']
_EXPRESSION_SUBQUERY = _EXPRESSION.nested_types_by_name['Subquery']
_EXPRESSION_SUBQUERY_SCALAR = _EXPRESSION_SUBQUERY.nested_types_by_name['Scalar']
_EXPRESSION_SUBQUERY_INPREDICATE = _EXPRESSION_SUBQUERY.nested_types_by_name['InPredicate']
_EXPRESSION_SUBQUERY_SETPREDICATE = _EXPRESSION_SUBQUERY.nested_types_by_name['SetPredicate']
_EXPRESSION_SUBQUERY_SETCOMPARISON = _EXPRESSION_SUBQUERY.nested_types_by_name['SetComparison']
_SORTFIELD = DESCRIPTOR.message_types_by_name['SortField']
_AGGREGATEFUNCTION = DESCRIPTOR.message_types_by_name['AggregateFunction']
_AGGREGATEFUNCTION_REFERENCEREL = _AGGREGATEFUNCTION.nested_types_by_name['ReferenceRel']
_JOINREL_JOINTYPE = _JOINREL.enum_types_by_name['JoinType']
_SETREL_SETOP = _SETREL.enum_types_by_name['SetOp']
_DDLREL_DDLOBJECT = _DDLREL.enum_types_by_name['DdlObject']
_DDLREL_DDLOP = _DDLREL.enum_types_by_name['DdlOp']
_WRITEREL_WRITEOP = _WRITEREL.enum_types_by_name['WriteOp']
_WRITEREL_OUTPUTMODE = _WRITEREL.enum_types_by_name['OutputMode']
_HASHJOINREL_JOINTYPE = _HASHJOINREL.enum_types_by_name['JoinType']
_MERGEJOINREL_JOINTYPE = _MERGEJOINREL.enum_types_by_name['JoinType']
_EXPRESSION_CAST_FAILUREBEHAVIOR = _EXPRESSION_CAST.enum_types_by_name['FailureBehavior']
_EXPRESSION_SUBQUERY_SETPREDICATE_PREDICATEOP = _EXPRESSION_SUBQUERY_SETPREDICATE.enum_types_by_name['PredicateOp']
_EXPRESSION_SUBQUERY_SETCOMPARISON_COMPARISONOP = _EXPRESSION_SUBQUERY_SETCOMPARISON.enum_types_by_name['ComparisonOp']
_EXPRESSION_SUBQUERY_SETCOMPARISON_REDUCTIONOP = _EXPRESSION_SUBQUERY_SETCOMPARISON.enum_types_by_name['ReductionOp']
_SORTFIELD_SORTDIRECTION = _SORTFIELD.enum_types_by_name['SortDirection']
_AGGREGATEFUNCTION_AGGREGATIONINVOCATION = _AGGREGATEFUNCTION.enum_types_by_name['AggregationInvocation']
RelCommon = _reflection.GeneratedProtocolMessageType('RelCommon', (_message.Message,), {'Direct': _reflection.GeneratedProtocolMessageType('Direct', (_message.Message,), {'DESCRIPTOR': _RELCOMMON_DIRECT, '__module__': 'proto.algebra_pb2'}), 'Emit': _reflection.GeneratedProtocolMessageType('Emit', (_message.Message,), {'DESCRIPTOR': _RELCOMMON_EMIT, '__module__': 'proto.algebra_pb2'}), 'Hint': _reflection.GeneratedProtocolMessageType('Hint', (_message.Message,), {'Stats': _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), {'DESCRIPTOR': _RELCOMMON_HINT_STATS, '__module__': 'proto.algebra_pb2'}), 'RuntimeConstraint': _reflection.GeneratedProtocolMessageType('RuntimeConstraint', (_message.Message,), {'DESCRIPTOR': _RELCOMMON_HINT_RUNTIMECONSTRAINT, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _RELCOMMON_HINT, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _RELCOMMON, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(RelCommon)
_sym_db.RegisterMessage(RelCommon.Direct)
_sym_db.RegisterMessage(RelCommon.Emit)
_sym_db.RegisterMessage(RelCommon.Hint)
_sym_db.RegisterMessage(RelCommon.Hint.Stats)
_sym_db.RegisterMessage(RelCommon.Hint.RuntimeConstraint)
ReadRel = _reflection.GeneratedProtocolMessageType('ReadRel', (_message.Message,), {'NamedTable': _reflection.GeneratedProtocolMessageType('NamedTable', (_message.Message,), {'DESCRIPTOR': _READREL_NAMEDTABLE, '__module__': 'proto.algebra_pb2'}), 'VirtualTable': _reflection.GeneratedProtocolMessageType('VirtualTable', (_message.Message,), {'DESCRIPTOR': _READREL_VIRTUALTABLE, '__module__': 'proto.algebra_pb2'}), 'ExtensionTable': _reflection.GeneratedProtocolMessageType('ExtensionTable', (_message.Message,), {'DESCRIPTOR': _READREL_EXTENSIONTABLE, '__module__': 'proto.algebra_pb2'}), 'LocalFiles': _reflection.GeneratedProtocolMessageType('LocalFiles', (_message.Message,), {'FileOrFiles': _reflection.GeneratedProtocolMessageType('FileOrFiles', (_message.Message,), {'ParquetReadOptions': _reflection.GeneratedProtocolMessageType('ParquetReadOptions', (_message.Message,), {'DESCRIPTOR': _READREL_LOCALFILES_FILEORFILES_PARQUETREADOPTIONS, '__module__': 'proto.algebra_pb2'}), 'ArrowReadOptions': _reflection.GeneratedProtocolMessageType('ArrowReadOptions', (_message.Message,), {'DESCRIPTOR': _READREL_LOCALFILES_FILEORFILES_ARROWREADOPTIONS, '__module__': 'proto.algebra_pb2'}), 'OrcReadOptions': _reflection.GeneratedProtocolMessageType('OrcReadOptions', (_message.Message,), {'DESCRIPTOR': _READREL_LOCALFILES_FILEORFILES_ORCREADOPTIONS, '__module__': 'proto.algebra_pb2'}), 'DwrfReadOptions': _reflection.GeneratedProtocolMessageType('DwrfReadOptions', (_message.Message,), {'DESCRIPTOR': _READREL_LOCALFILES_FILEORFILES_DWRFREADOPTIONS, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _READREL_LOCALFILES_FILEORFILES, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _READREL_LOCALFILES, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _READREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(ReadRel)
_sym_db.RegisterMessage(ReadRel.NamedTable)
_sym_db.RegisterMessage(ReadRel.VirtualTable)
_sym_db.RegisterMessage(ReadRel.ExtensionTable)
_sym_db.RegisterMessage(ReadRel.LocalFiles)
_sym_db.RegisterMessage(ReadRel.LocalFiles.FileOrFiles)
_sym_db.RegisterMessage(ReadRel.LocalFiles.FileOrFiles.ParquetReadOptions)
_sym_db.RegisterMessage(ReadRel.LocalFiles.FileOrFiles.ArrowReadOptions)
_sym_db.RegisterMessage(ReadRel.LocalFiles.FileOrFiles.OrcReadOptions)
_sym_db.RegisterMessage(ReadRel.LocalFiles.FileOrFiles.DwrfReadOptions)
ProjectRel = _reflection.GeneratedProtocolMessageType('ProjectRel', (_message.Message,), {'DESCRIPTOR': _PROJECTREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(ProjectRel)
JoinRel = _reflection.GeneratedProtocolMessageType('JoinRel', (_message.Message,), {'DESCRIPTOR': _JOINREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(JoinRel)
CrossRel = _reflection.GeneratedProtocolMessageType('CrossRel', (_message.Message,), {'DESCRIPTOR': _CROSSREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(CrossRel)
FetchRel = _reflection.GeneratedProtocolMessageType('FetchRel', (_message.Message,), {'DESCRIPTOR': _FETCHREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(FetchRel)
AggregateRel = _reflection.GeneratedProtocolMessageType('AggregateRel', (_message.Message,), {'Grouping': _reflection.GeneratedProtocolMessageType('Grouping', (_message.Message,), {'DESCRIPTOR': _AGGREGATEREL_GROUPING, '__module__': 'proto.algebra_pb2'}), 'Measure': _reflection.GeneratedProtocolMessageType('Measure', (_message.Message,), {'DESCRIPTOR': _AGGREGATEREL_MEASURE, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _AGGREGATEREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(AggregateRel)
_sym_db.RegisterMessage(AggregateRel.Grouping)
_sym_db.RegisterMessage(AggregateRel.Measure)
SortRel = _reflection.GeneratedProtocolMessageType('SortRel', (_message.Message,), {'DESCRIPTOR': _SORTREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(SortRel)
FilterRel = _reflection.GeneratedProtocolMessageType('FilterRel', (_message.Message,), {'DESCRIPTOR': _FILTERREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(FilterRel)
SetRel = _reflection.GeneratedProtocolMessageType('SetRel', (_message.Message,), {'DESCRIPTOR': _SETREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(SetRel)
ExtensionSingleRel = _reflection.GeneratedProtocolMessageType('ExtensionSingleRel', (_message.Message,), {'DESCRIPTOR': _EXTENSIONSINGLEREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(ExtensionSingleRel)
ExtensionLeafRel = _reflection.GeneratedProtocolMessageType('ExtensionLeafRel', (_message.Message,), {'DESCRIPTOR': _EXTENSIONLEAFREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(ExtensionLeafRel)
ExtensionMultiRel = _reflection.GeneratedProtocolMessageType('ExtensionMultiRel', (_message.Message,), {'DESCRIPTOR': _EXTENSIONMULTIREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(ExtensionMultiRel)
ExchangeRel = _reflection.GeneratedProtocolMessageType('ExchangeRel', (_message.Message,), {'ScatterFields': _reflection.GeneratedProtocolMessageType('ScatterFields', (_message.Message,), {'DESCRIPTOR': _EXCHANGEREL_SCATTERFIELDS, '__module__': 'proto.algebra_pb2'}), 'SingleBucketExpression': _reflection.GeneratedProtocolMessageType('SingleBucketExpression', (_message.Message,), {'DESCRIPTOR': _EXCHANGEREL_SINGLEBUCKETEXPRESSION, '__module__': 'proto.algebra_pb2'}), 'MultiBucketExpression': _reflection.GeneratedProtocolMessageType('MultiBucketExpression', (_message.Message,), {'DESCRIPTOR': _EXCHANGEREL_MULTIBUCKETEXPRESSION, '__module__': 'proto.algebra_pb2'}), 'Broadcast': _reflection.GeneratedProtocolMessageType('Broadcast', (_message.Message,), {'DESCRIPTOR': _EXCHANGEREL_BROADCAST, '__module__': 'proto.algebra_pb2'}), 'RoundRobin': _reflection.GeneratedProtocolMessageType('RoundRobin', (_message.Message,), {'DESCRIPTOR': _EXCHANGEREL_ROUNDROBIN, '__module__': 'proto.algebra_pb2'}), 'ExchangeTarget': _reflection.GeneratedProtocolMessageType('ExchangeTarget', (_message.Message,), {'DESCRIPTOR': _EXCHANGEREL_EXCHANGETARGET, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXCHANGEREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(ExchangeRel)
_sym_db.RegisterMessage(ExchangeRel.ScatterFields)
_sym_db.RegisterMessage(ExchangeRel.SingleBucketExpression)
_sym_db.RegisterMessage(ExchangeRel.MultiBucketExpression)
_sym_db.RegisterMessage(ExchangeRel.Broadcast)
_sym_db.RegisterMessage(ExchangeRel.RoundRobin)
_sym_db.RegisterMessage(ExchangeRel.ExchangeTarget)
RelRoot = _reflection.GeneratedProtocolMessageType('RelRoot', (_message.Message,), {'DESCRIPTOR': _RELROOT, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(RelRoot)
Rel = _reflection.GeneratedProtocolMessageType('Rel', (_message.Message,), {'DESCRIPTOR': _REL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(Rel)
NamedObjectWrite = _reflection.GeneratedProtocolMessageType('NamedObjectWrite', (_message.Message,), {'DESCRIPTOR': _NAMEDOBJECTWRITE, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(NamedObjectWrite)
ExtensionObject = _reflection.GeneratedProtocolMessageType('ExtensionObject', (_message.Message,), {'DESCRIPTOR': _EXTENSIONOBJECT, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(ExtensionObject)
DdlRel = _reflection.GeneratedProtocolMessageType('DdlRel', (_message.Message,), {'DESCRIPTOR': _DDLREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(DdlRel)
WriteRel = _reflection.GeneratedProtocolMessageType('WriteRel', (_message.Message,), {'DESCRIPTOR': _WRITEREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(WriteRel)
HashJoinRel = _reflection.GeneratedProtocolMessageType('HashJoinRel', (_message.Message,), {'DESCRIPTOR': _HASHJOINREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(HashJoinRel)
MergeJoinRel = _reflection.GeneratedProtocolMessageType('MergeJoinRel', (_message.Message,), {'DESCRIPTOR': _MERGEJOINREL, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(MergeJoinRel)
FunctionArgument = _reflection.GeneratedProtocolMessageType('FunctionArgument', (_message.Message,), {'DESCRIPTOR': _FUNCTIONARGUMENT, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(FunctionArgument)
FunctionOption = _reflection.GeneratedProtocolMessageType('FunctionOption', (_message.Message,), {'DESCRIPTOR': _FUNCTIONOPTION, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(FunctionOption)
Expression = _reflection.GeneratedProtocolMessageType('Expression', (_message.Message,), {'Enum': _reflection.GeneratedProtocolMessageType('Enum', (_message.Message,), {'Empty': _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_ENUM_EMPTY, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_ENUM, '__module__': 'proto.algebra_pb2'}), 'Literal': _reflection.GeneratedProtocolMessageType('Literal', (_message.Message,), {'VarChar': _reflection.GeneratedProtocolMessageType('VarChar', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_VARCHAR, '__module__': 'proto.algebra_pb2'}), 'Decimal': _reflection.GeneratedProtocolMessageType('Decimal', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_DECIMAL, '__module__': 'proto.algebra_pb2'}), 'Map': _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {'KeyValue': _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_MAP_KEYVALUE, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_LITERAL_MAP, '__module__': 'proto.algebra_pb2'}), 'IntervalYearToMonth': _reflection.GeneratedProtocolMessageType('IntervalYearToMonth', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_INTERVALYEARTOMONTH, '__module__': 'proto.algebra_pb2'}), 'IntervalDayToSecond': _reflection.GeneratedProtocolMessageType('IntervalDayToSecond', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_INTERVALDAYTOSECOND, '__module__': 'proto.algebra_pb2'}), 'Struct': _reflection.GeneratedProtocolMessageType('Struct', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_STRUCT, '__module__': 'proto.algebra_pb2'}), 'List': _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_LIST, '__module__': 'proto.algebra_pb2'}), 'UserDefined': _reflection.GeneratedProtocolMessageType('UserDefined', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_LITERAL_USERDEFINED, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_LITERAL, '__module__': 'proto.algebra_pb2'}), 'Nested': _reflection.GeneratedProtocolMessageType('Nested', (_message.Message,), {'Map': _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {'KeyValue': _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_NESTED_MAP_KEYVALUE, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_NESTED_MAP, '__module__': 'proto.algebra_pb2'}), 'Struct': _reflection.GeneratedProtocolMessageType('Struct', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_NESTED_STRUCT, '__module__': 'proto.algebra_pb2'}), 'List': _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_NESTED_LIST, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_NESTED, '__module__': 'proto.algebra_pb2'}), 'ScalarFunction': _reflection.GeneratedProtocolMessageType('ScalarFunction', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_SCALARFUNCTION, '__module__': 'proto.algebra_pb2'}), 'WindowFunction': _reflection.GeneratedProtocolMessageType('WindowFunction', (_message.Message,), {'Bound': _reflection.GeneratedProtocolMessageType('Bound', (_message.Message,), {'Preceding': _reflection.GeneratedProtocolMessageType('Preceding', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_WINDOWFUNCTION_BOUND_PRECEDING, '__module__': 'proto.algebra_pb2'}), 'Following': _reflection.GeneratedProtocolMessageType('Following', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_WINDOWFUNCTION_BOUND_FOLLOWING, '__module__': 'proto.algebra_pb2'}), 'CurrentRow': _reflection.GeneratedProtocolMessageType('CurrentRow', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_WINDOWFUNCTION_BOUND_CURRENTROW, '__module__': 'proto.algebra_pb2'}), 'Unbounded': _reflection.GeneratedProtocolMessageType('Unbounded', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_WINDOWFUNCTION_BOUND_UNBOUNDED, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_WINDOWFUNCTION_BOUND, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_WINDOWFUNCTION, '__module__': 'proto.algebra_pb2'}), 'IfThen': _reflection.GeneratedProtocolMessageType('IfThen', (_message.Message,), {'IfClause': _reflection.GeneratedProtocolMessageType('IfClause', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_IFTHEN_IFCLAUSE, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_IFTHEN, '__module__': 'proto.algebra_pb2'}), 'Cast': _reflection.GeneratedProtocolMessageType('Cast', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_CAST, '__module__': 'proto.algebra_pb2'}), 'SwitchExpression': _reflection.GeneratedProtocolMessageType('SwitchExpression', (_message.Message,), {'IfValue': _reflection.GeneratedProtocolMessageType('IfValue', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_SWITCHEXPRESSION_IFVALUE, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_SWITCHEXPRESSION, '__module__': 'proto.algebra_pb2'}), 'SingularOrList': _reflection.GeneratedProtocolMessageType('SingularOrList', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_SINGULARORLIST, '__module__': 'proto.algebra_pb2'}), 'MultiOrList': _reflection.GeneratedProtocolMessageType('MultiOrList', (_message.Message,), {'Record': _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MULTIORLIST_RECORD, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_MULTIORLIST, '__module__': 'proto.algebra_pb2'}), 'EmbeddedFunction': _reflection.GeneratedProtocolMessageType('EmbeddedFunction', (_message.Message,), {'PythonPickleFunction': _reflection.GeneratedProtocolMessageType('PythonPickleFunction', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_EMBEDDEDFUNCTION_PYTHONPICKLEFUNCTION, '__module__': 'proto.algebra_pb2'}), 'WebAssemblyFunction': _reflection.GeneratedProtocolMessageType('WebAssemblyFunction', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_EMBEDDEDFUNCTION_WEBASSEMBLYFUNCTION, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_EMBEDDEDFUNCTION, '__module__': 'proto.algebra_pb2'}), 'ReferenceSegment': _reflection.GeneratedProtocolMessageType('ReferenceSegment', (_message.Message,), {'MapKey': _reflection.GeneratedProtocolMessageType('MapKey', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_REFERENCESEGMENT_MAPKEY, '__module__': 'proto.algebra_pb2'}), 'StructField': _reflection.GeneratedProtocolMessageType('StructField', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_REFERENCESEGMENT_STRUCTFIELD, '__module__': 'proto.algebra_pb2'}), 'ListElement': _reflection.GeneratedProtocolMessageType('ListElement', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_REFERENCESEGMENT_LISTELEMENT, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_REFERENCESEGMENT, '__module__': 'proto.algebra_pb2'}), 'MaskExpression': _reflection.GeneratedProtocolMessageType('MaskExpression', (_message.Message,), {'Select': _reflection.GeneratedProtocolMessageType('Select', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_SELECT, '__module__': 'proto.algebra_pb2'}), 'StructSelect': _reflection.GeneratedProtocolMessageType('StructSelect', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_STRUCTSELECT, '__module__': 'proto.algebra_pb2'}), 'StructItem': _reflection.GeneratedProtocolMessageType('StructItem', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_STRUCTITEM, '__module__': 'proto.algebra_pb2'}), 'ListSelect': _reflection.GeneratedProtocolMessageType('ListSelect', (_message.Message,), {'ListSelectItem': _reflection.GeneratedProtocolMessageType('ListSelectItem', (_message.Message,), {'ListElement': _reflection.GeneratedProtocolMessageType('ListElement', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTELEMENT, '__module__': 'proto.algebra_pb2'}), 'ListSlice': _reflection.GeneratedProtocolMessageType('ListSlice', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTSLICE, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_LISTSELECT, '__module__': 'proto.algebra_pb2'}), 'MapSelect': _reflection.GeneratedProtocolMessageType('MapSelect', (_message.Message,), {'MapKey': _reflection.GeneratedProtocolMessageType('MapKey', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEY, '__module__': 'proto.algebra_pb2'}), 'MapKeyExpression': _reflection.GeneratedProtocolMessageType('MapKeyExpression', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEYEXPRESSION, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION_MAPSELECT, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_MASKEXPRESSION, '__module__': 'proto.algebra_pb2'}), 'FieldReference': _reflection.GeneratedProtocolMessageType('FieldReference', (_message.Message,), {'RootReference': _reflection.GeneratedProtocolMessageType('RootReference', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_FIELDREFERENCE_ROOTREFERENCE, '__module__': 'proto.algebra_pb2'}), 'OuterReference': _reflection.GeneratedProtocolMessageType('OuterReference', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_FIELDREFERENCE_OUTERREFERENCE, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_FIELDREFERENCE, '__module__': 'proto.algebra_pb2'}), 'Subquery': _reflection.GeneratedProtocolMessageType('Subquery', (_message.Message,), {'Scalar': _reflection.GeneratedProtocolMessageType('Scalar', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_SUBQUERY_SCALAR, '__module__': 'proto.algebra_pb2'}), 'InPredicate': _reflection.GeneratedProtocolMessageType('InPredicate', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_SUBQUERY_INPREDICATE, '__module__': 'proto.algebra_pb2'}), 'SetPredicate': _reflection.GeneratedProtocolMessageType('SetPredicate', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_SUBQUERY_SETPREDICATE, '__module__': 'proto.algebra_pb2'}), 'SetComparison': _reflection.GeneratedProtocolMessageType('SetComparison', (_message.Message,), {'DESCRIPTOR': _EXPRESSION_SUBQUERY_SETCOMPARISON, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION_SUBQUERY, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _EXPRESSION, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(Expression)
_sym_db.RegisterMessage(Expression.Enum)
_sym_db.RegisterMessage(Expression.Enum.Empty)
_sym_db.RegisterMessage(Expression.Literal)
_sym_db.RegisterMessage(Expression.Literal.VarChar)
_sym_db.RegisterMessage(Expression.Literal.Decimal)
_sym_db.RegisterMessage(Expression.Literal.Map)
_sym_db.RegisterMessage(Expression.Literal.Map.KeyValue)
_sym_db.RegisterMessage(Expression.Literal.IntervalYearToMonth)
_sym_db.RegisterMessage(Expression.Literal.IntervalDayToSecond)
_sym_db.RegisterMessage(Expression.Literal.Struct)
_sym_db.RegisterMessage(Expression.Literal.List)
_sym_db.RegisterMessage(Expression.Literal.UserDefined)
_sym_db.RegisterMessage(Expression.Nested)
_sym_db.RegisterMessage(Expression.Nested.Map)
_sym_db.RegisterMessage(Expression.Nested.Map.KeyValue)
_sym_db.RegisterMessage(Expression.Nested.Struct)
_sym_db.RegisterMessage(Expression.Nested.List)
_sym_db.RegisterMessage(Expression.ScalarFunction)
_sym_db.RegisterMessage(Expression.WindowFunction)
_sym_db.RegisterMessage(Expression.WindowFunction.Bound)
_sym_db.RegisterMessage(Expression.WindowFunction.Bound.Preceding)
_sym_db.RegisterMessage(Expression.WindowFunction.Bound.Following)
_sym_db.RegisterMessage(Expression.WindowFunction.Bound.CurrentRow)
_sym_db.RegisterMessage(Expression.WindowFunction.Bound.Unbounded)
_sym_db.RegisterMessage(Expression.IfThen)
_sym_db.RegisterMessage(Expression.IfThen.IfClause)
_sym_db.RegisterMessage(Expression.Cast)
_sym_db.RegisterMessage(Expression.SwitchExpression)
_sym_db.RegisterMessage(Expression.SwitchExpression.IfValue)
_sym_db.RegisterMessage(Expression.SingularOrList)
_sym_db.RegisterMessage(Expression.MultiOrList)
_sym_db.RegisterMessage(Expression.MultiOrList.Record)
_sym_db.RegisterMessage(Expression.EmbeddedFunction)
_sym_db.RegisterMessage(Expression.EmbeddedFunction.PythonPickleFunction)
_sym_db.RegisterMessage(Expression.EmbeddedFunction.WebAssemblyFunction)
_sym_db.RegisterMessage(Expression.ReferenceSegment)
_sym_db.RegisterMessage(Expression.ReferenceSegment.MapKey)
_sym_db.RegisterMessage(Expression.ReferenceSegment.StructField)
_sym_db.RegisterMessage(Expression.ReferenceSegment.ListElement)
_sym_db.RegisterMessage(Expression.MaskExpression)
_sym_db.RegisterMessage(Expression.MaskExpression.Select)
_sym_db.RegisterMessage(Expression.MaskExpression.StructSelect)
_sym_db.RegisterMessage(Expression.MaskExpression.StructItem)
_sym_db.RegisterMessage(Expression.MaskExpression.ListSelect)
_sym_db.RegisterMessage(Expression.MaskExpression.ListSelect.ListSelectItem)
_sym_db.RegisterMessage(Expression.MaskExpression.ListSelect.ListSelectItem.ListElement)
_sym_db.RegisterMessage(Expression.MaskExpression.ListSelect.ListSelectItem.ListSlice)
_sym_db.RegisterMessage(Expression.MaskExpression.MapSelect)
_sym_db.RegisterMessage(Expression.MaskExpression.MapSelect.MapKey)
_sym_db.RegisterMessage(Expression.MaskExpression.MapSelect.MapKeyExpression)
_sym_db.RegisterMessage(Expression.FieldReference)
_sym_db.RegisterMessage(Expression.FieldReference.RootReference)
_sym_db.RegisterMessage(Expression.FieldReference.OuterReference)
_sym_db.RegisterMessage(Expression.Subquery)
_sym_db.RegisterMessage(Expression.Subquery.Scalar)
_sym_db.RegisterMessage(Expression.Subquery.InPredicate)
_sym_db.RegisterMessage(Expression.Subquery.SetPredicate)
_sym_db.RegisterMessage(Expression.Subquery.SetComparison)
SortField = _reflection.GeneratedProtocolMessageType('SortField', (_message.Message,), {'DESCRIPTOR': _SORTFIELD, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(SortField)
AggregateFunction = _reflection.GeneratedProtocolMessageType('AggregateFunction', (_message.Message,), {'ReferenceRel': _reflection.GeneratedProtocolMessageType('ReferenceRel', (_message.Message,), {'DESCRIPTOR': _AGGREGATEFUNCTION_REFERENCEREL, '__module__': 'proto.algebra_pb2'}), 'DESCRIPTOR': _AGGREGATEFUNCTION, '__module__': 'proto.algebra_pb2'})
_sym_db.RegisterMessage(AggregateFunction)
_sym_db.RegisterMessage(AggregateFunction.ReferenceRel)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x0eio.proto.protoP\x01\xaa\x02\x0eProto.Protobuf'
    _EXPRESSION_ENUM_EMPTY._options = None
    _EXPRESSION_ENUM_EMPTY._serialized_options = b'\x18\x01'
    _EXPRESSION_ENUM._options = None
    _EXPRESSION_ENUM._serialized_options = b'\x18\x01'
    _EXPRESSION_SCALARFUNCTION.fields_by_name['args']._options = None
    _EXPRESSION_SCALARFUNCTION.fields_by_name['args']._serialized_options = b'\x18\x01'
    _EXPRESSION_WINDOWFUNCTION.fields_by_name['args']._options = None
    _EXPRESSION_WINDOWFUNCTION.fields_by_name['args']._serialized_options = b'\x18\x01'
    _EXPRESSION.fields_by_name['enum']._options = None
    _EXPRESSION.fields_by_name['enum']._serialized_options = b'\x18\x01'
    _AGGREGATEFUNCTION.fields_by_name['args']._options = None
    _AGGREGATEFUNCTION.fields_by_name['args']._serialized_options = b'\x18\x01'
    _AGGREGATIONPHASE._serialized_start = 21601
    _AGGREGATIONPHASE._serialized_end = 21840
    _RELCOMMON._serialized_start = 111
    _RELCOMMON._serialized_end = 893
    _RELCOMMON_DIRECT._serialized_start = 347
    _RELCOMMON_DIRECT._serialized_end = 355
    _RELCOMMON_EMIT._serialized_start = 357
    _RELCOMMON_EMIT._serialized_end = 402
    _RELCOMMON_HINT._serialized_start = 405
    _RELCOMMON_HINT._serialized_end = 880
    _RELCOMMON_HINT_STATS._serialized_start = 622
    _RELCOMMON_HINT_STATS._serialized_end = 775
    _RELCOMMON_HINT_RUNTIMECONSTRAINT._serialized_start = 777
    _RELCOMMON_HINT_RUNTIMECONSTRAINT._serialized_end = 880
    _READREL._serialized_start = 896
    _READREL._serialized_end = 2679
    _READREL_NAMEDTABLE._serialized_start = 1526
    _READREL_NAMEDTABLE._serialized_end = 1644
    _READREL_VIRTUALTABLE._serialized_start = 1646
    _READREL_VIRTUALTABLE._serialized_end = 1718
    _READREL_EXTENSIONTABLE._serialized_start = 1720
    _READREL_EXTENSIONTABLE._serialized_end = 1782
    _READREL_LOCALFILES._serialized_start = 1785
    _READREL_LOCALFILES._serialized_end = 2666
    _READREL_LOCALFILES_FILEORFILES._serialized_start = 1945
    _READREL_LOCALFILES_FILEORFILES._serialized_end = 2666
    _READREL_LOCALFILES_FILEORFILES_PARQUETREADOPTIONS._serialized_start = 2547
    _READREL_LOCALFILES_FILEORFILES_PARQUETREADOPTIONS._serialized_end = 2567
    _READREL_LOCALFILES_FILEORFILES_ARROWREADOPTIONS._serialized_start = 2569
    _READREL_LOCALFILES_FILEORFILES_ARROWREADOPTIONS._serialized_end = 2587
    _READREL_LOCALFILES_FILEORFILES_ORCREADOPTIONS._serialized_start = 2589
    _READREL_LOCALFILES_FILEORFILES_ORCREADOPTIONS._serialized_end = 2605
    _READREL_LOCALFILES_FILEORFILES_DWRFREADOPTIONS._serialized_start = 2607
    _READREL_LOCALFILES_FILEORFILES_DWRFREADOPTIONS._serialized_end = 2624
    _PROJECTREL._serialized_start = 2682
    _PROJECTREL._serialized_end = 2907
    _JOINREL._serialized_start = 2910
    _JOINREL._serialized_end = 3453
    _JOINREL_JOINTYPE._serialized_start = 3271
    _JOINREL_JOINTYPE._serialized_end = 3453
    _CROSSREL._serialized_start = 3456
    _CROSSREL._serialized_end = 3658
    _FETCHREL._serialized_start = 3661
    _FETCHREL._serialized_end = 3877
    _AGGREGATEREL._serialized_start = 3880
    _AGGREGATEREL._serialized_end = 4359
    _AGGREGATEREL_GROUPING._serialized_start = 4173
    _AGGREGATEREL_GROUPING._serialized_end = 4253
    _AGGREGATEREL_MEASURE._serialized_start = 4255
    _AGGREGATEREL_MEASURE._serialized_end = 4359
    _SORTREL._serialized_start = 4362
    _SORTREL._serialized_end = 4571
    _FILTERREL._serialized_start = 4574
    _FILTERREL._serialized_end = 4794
    _SETREL._serialized_start = 4797
    _SETREL._serialized_end = 5207
    _SETREL_SETOP._serialized_start = 5007
    _SETREL_SETOP._serialized_end = 5207
    _EXTENSIONSINGLEREL._serialized_start = 5210
    _EXTENSIONSINGLEREL._serialized_end = 5352
    _EXTENSIONLEAFREL._serialized_start = 5354
    _EXTENSIONLEAFREL._serialized_end = 5460
    _EXTENSIONMULTIREL._serialized_start = 5463
    _EXTENSIONMULTIREL._serialized_end = 5606
    _EXCHANGEREL._serialized_start = 5609
    _EXCHANGEREL._serialized_end = 6738
    _EXCHANGEREL_SCATTERFIELDS._serialized_start = 6255
    _EXCHANGEREL_SCATTERFIELDS._serialized_end = 6328
    _EXCHANGEREL_SINGLEBUCKETEXPRESSION._serialized_start = 6330
    _EXCHANGEREL_SINGLEBUCKETEXPRESSION._serialized_end = 6405
    _EXCHANGEREL_MULTIBUCKETEXPRESSION._serialized_start = 6407
    _EXCHANGEREL_MULTIBUCKETEXPRESSION._serialized_end = 6531
    _EXCHANGEREL_BROADCAST._serialized_start = 6533
    _EXCHANGEREL_BROADCAST._serialized_end = 6544
    _EXCHANGEREL_ROUNDROBIN._serialized_start = 6546
    _EXCHANGEREL_ROUNDROBIN._serialized_end = 6580
    _EXCHANGEREL_EXCHANGETARGET._serialized_start = 6583
    _EXCHANGEREL_EXCHANGETARGET._serialized_end = 6721
    _RELROOT._serialized_start = 6740
    _RELROOT._serialized_end = 6805
    _REL._serialized_start = 6808
    _REL._serialized_end = 7512
    _NAMEDOBJECTWRITE._serialized_start = 7514
    _NAMEDOBJECTWRITE._serialized_end = 7638
    _EXTENSIONOBJECT._serialized_start = 7640
    _EXTENSIONOBJECT._serialized_end = 7703
    _DDLREL._serialized_start = 7706
    _DDLREL._serialized_end = 8354
    _DDLREL_DDLOBJECT._serialized_start = 8114
    _DDLREL_DDLOBJECT._serialized_end = 8196
    _DDLREL_DDLOP._serialized_start = 8199
    _DDLREL_DDLOP._serialized_end = 8340
    _WRITEREL._serialized_start = 8357
    _WRITEREL._serialized_end = 8912
    _WRITEREL_WRITEOP._serialized_start = 8678
    _WRITEREL_WRITEOP._serialized_end = 8795
    _WRITEREL_OUTPUTMODE._serialized_start = 8797
    _WRITEREL_OUTPUTMODE._serialized_end = 8898
    _HASHJOINREL._serialized_start = 8915
    _HASHJOINREL._serialized_end = 9583
    _HASHJOINREL_JOINTYPE._serialized_start = 9361
    _HASHJOINREL_JOINTYPE._serialized_end = 9583
    _MERGEJOINREL._serialized_start = 9586
    _MERGEJOINREL._serialized_end = 10256
    _MERGEJOINREL_JOINTYPE._serialized_start = 9361
    _MERGEJOINREL_JOINTYPE._serialized_end = 9583
    _FUNCTIONARGUMENT._serialized_start = 10259
    _FUNCTIONARGUMENT._serialized_end = 10389
    _FUNCTIONOPTION._serialized_start = 10391
    _FUNCTIONOPTION._serialized_end = 10459
    _EXPRESSION._serialized_start = 10462
    _EXPRESSION._serialized_end = 20553
    _EXPRESSION_ENUM._serialized_start = 11241
    _EXPRESSION_ENUM._serialized_end = 11375
    _EXPRESSION_ENUM_EMPTY._serialized_start = 11347
    _EXPRESSION_ENUM_EMPTY._serialized_end = 11358
    _EXPRESSION_LITERAL._serialized_start = 11378
    _EXPRESSION_LITERAL._serialized_end = 13386
    _EXPRESSION_LITERAL_VARCHAR._serialized_start = 12588
    _EXPRESSION_LITERAL_VARCHAR._serialized_end = 12643
    _EXPRESSION_LITERAL_DECIMAL._serialized_start = 12645
    _EXPRESSION_LITERAL_DECIMAL._serialized_end = 12728
    _EXPRESSION_LITERAL_MAP._serialized_start = 12731
    _EXPRESSION_LITERAL_MAP._serialized_end = 12913
    _EXPRESSION_LITERAL_MAP_KEYVALUE._serialized_start = 12809
    _EXPRESSION_LITERAL_MAP_KEYVALUE._serialized_end = 12913
    _EXPRESSION_LITERAL_INTERVALYEARTOMONTH._serialized_start = 12915
    _EXPRESSION_LITERAL_INTERVALYEARTOMONTH._serialized_end = 12982
    _EXPRESSION_LITERAL_INTERVALDAYTOSECOND._serialized_start = 12984
    _EXPRESSION_LITERAL_INTERVALDAYTOSECOND._serialized_end = 13087
    _EXPRESSION_LITERAL_STRUCT._serialized_start = 13089
    _EXPRESSION_LITERAL_STRUCT._serialized_end = 13148
    _EXPRESSION_LITERAL_LIST._serialized_start = 13150
    _EXPRESSION_LITERAL_LIST._serialized_end = 13207
    _EXPRESSION_LITERAL_USERDEFINED._serialized_start = 13210
    _EXPRESSION_LITERAL_USERDEFINED._serialized_end = 13370
    _EXPRESSION_NESTED._serialized_start = 13389
    _EXPRESSION_NESTED._serialized_end = 13932
    _EXPRESSION_NESTED_MAP._serialized_start = 13648
    _EXPRESSION_NESTED_MAP._serialized_end = 13813
    _EXPRESSION_NESTED_MAP_KEYVALUE._serialized_start = 13725
    _EXPRESSION_NESTED_MAP_KEYVALUE._serialized_end = 13813
    _EXPRESSION_NESTED_STRUCT._serialized_start = 13815
    _EXPRESSION_NESTED_STRUCT._serialized_end = 13866
    _EXPRESSION_NESTED_LIST._serialized_start = 13868
    _EXPRESSION_NESTED_LIST._serialized_end = 13917
    _EXPRESSION_SCALARFUNCTION._serialized_start = 13935
    _EXPRESSION_SCALARFUNCTION._serialized_end = 14191
    _EXPRESSION_WINDOWFUNCTION._serialized_start = 14194
    _EXPRESSION_WINDOWFUNCTION._serialized_end = 15265
    _EXPRESSION_WINDOWFUNCTION_BOUND._serialized_start = 14817
    _EXPRESSION_WINDOWFUNCTION_BOUND._serialized_end = 15265
    _EXPRESSION_WINDOWFUNCTION_BOUND_PRECEDING._serialized_start = 15158
    _EXPRESSION_WINDOWFUNCTION_BOUND_PRECEDING._serialized_end = 15193
    _EXPRESSION_WINDOWFUNCTION_BOUND_FOLLOWING._serialized_start = 15195
    _EXPRESSION_WINDOWFUNCTION_BOUND_FOLLOWING._serialized_end = 15230
    _EXPRESSION_WINDOWFUNCTION_BOUND_CURRENTROW._serialized_start = 15232
    _EXPRESSION_WINDOWFUNCTION_BOUND_CURRENTROW._serialized_end = 15244
    _EXPRESSION_WINDOWFUNCTION_BOUND_UNBOUNDED._serialized_start = 15246
    _EXPRESSION_WINDOWFUNCTION_BOUND_UNBOUNDED._serialized_end = 15257
    _EXPRESSION_IFTHEN._serialized_start = 15268
    _EXPRESSION_IFTHEN._serialized_end = 15454
    _EXPRESSION_IFTHEN_IFCLAUSE._serialized_start = 15370
    _EXPRESSION_IFTHEN_IFCLAUSE._serialized_end = 15454
    _EXPRESSION_CAST._serialized_start = 15457
    _EXPRESSION_CAST._serialized_end = 15745
    _EXPRESSION_CAST_FAILUREBEHAVIOR._serialized_start = 15622
    _EXPRESSION_CAST_FAILUREBEHAVIOR._serialized_end = 15745
    _EXPRESSION_SWITCHEXPRESSION._serialized_start = 15748
    _EXPRESSION_SWITCHEXPRESSION._serialized_end = 16001
    _EXPRESSION_SWITCHEXPRESSION_IFVALUE._serialized_start = 15910
    _EXPRESSION_SWITCHEXPRESSION_IFVALUE._serialized_end = 16001
    _EXPRESSION_SINGULARORLIST._serialized_start = 16003
    _EXPRESSION_SINGULARORLIST._serialized_end = 16105
    _EXPRESSION_MULTIORLIST._serialized_start = 16108
    _EXPRESSION_MULTIORLIST._serialized_end = 16279
    _EXPRESSION_MULTIORLIST_RECORD._serialized_start = 16228
    _EXPRESSION_MULTIORLIST_RECORD._serialized_end = 16279
    _EXPRESSION_EMBEDDEDFUNCTION._serialized_start = 16282
    _EXPRESSION_EMBEDDEDFUNCTION._serialized_end = 16797
    _EXPRESSION_EMBEDDEDFUNCTION_PYTHONPICKLEFUNCTION._serialized_start = 16620
    _EXPRESSION_EMBEDDEDFUNCTION_PYTHONPICKLEFUNCTION._serialized_end = 16706
    _EXPRESSION_EMBEDDEDFUNCTION_WEBASSEMBLYFUNCTION._serialized_start = 16708
    _EXPRESSION_EMBEDDEDFUNCTION_WEBASSEMBLYFUNCTION._serialized_end = 16789
    _EXPRESSION_REFERENCESEGMENT._serialized_start = 16800
    _EXPRESSION_REFERENCESEGMENT._serialized_end = 17388
    _EXPRESSION_REFERENCESEGMENT_MAPKEY._serialized_start = 17060
    _EXPRESSION_REFERENCESEGMENT_MAPKEY._serialized_end = 17178
    _EXPRESSION_REFERENCESEGMENT_STRUCTFIELD._serialized_start = 17180
    _EXPRESSION_REFERENCESEGMENT_STRUCTFIELD._serialized_end = 17273
    _EXPRESSION_REFERENCESEGMENT_LISTELEMENT._serialized_start = 17275
    _EXPRESSION_REFERENCESEGMENT_LISTELEMENT._serialized_end = 17370
    _EXPRESSION_MASKEXPRESSION._serialized_start = 17391
    _EXPRESSION_MASKEXPRESSION._serialized_end = 18781
    _EXPRESSION_MASKEXPRESSION_SELECT._serialized_start = 17539
    _EXPRESSION_MASKEXPRESSION_SELECT._serialized_end = 17759
    _EXPRESSION_MASKEXPRESSION_STRUCTSELECT._serialized_start = 17761
    _EXPRESSION_MASKEXPRESSION_STRUCTSELECT._serialized_end = 17855
    _EXPRESSION_MASKEXPRESSION_STRUCTITEM._serialized_start = 17857
    _EXPRESSION_MASKEXPRESSION_STRUCTITEM._serialized_end = 17954
    _EXPRESSION_MASKEXPRESSION_LISTSELECT._serialized_start = 17957
    _EXPRESSION_MASKEXPRESSION_LISTSELECT._serialized_end = 18427
    _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM._serialized_start = 18125
    _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM._serialized_end = 18427
    _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTELEMENT._serialized_start = 18331
    _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTELEMENT._serialized_end = 18366
    _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTSLICE._serialized_start = 18368
    _EXPRESSION_MASKEXPRESSION_LISTSELECT_LISTSELECTITEM_LISTSLICE._serialized_end = 18419
    _EXPRESSION_MASKEXPRESSION_MAPSELECT._serialized_start = 18430
    _EXPRESSION_MASKEXPRESSION_MAPSELECT._serialized_end = 18781
    _EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEY._serialized_start = 18672
    _EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEY._serialized_end = 18705
    _EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEYEXPRESSION._serialized_start = 18707
    _EXPRESSION_MASKEXPRESSION_MAPSELECT_MAPKEYEXPRESSION._serialized_end = 18771
    _EXPRESSION_FIELDREFERENCE._serialized_start = 18784
    _EXPRESSION_FIELDREFERENCE._serialized_end = 19289
    _EXPRESSION_FIELDREFERENCE_ROOTREFERENCE._serialized_start = 19196
    _EXPRESSION_FIELDREFERENCE_ROOTREFERENCE._serialized_end = 19211
    _EXPRESSION_FIELDREFERENCE_OUTERREFERENCE._serialized_start = 19213
    _EXPRESSION_FIELDREFERENCE_OUTERREFERENCE._serialized_end = 19258
    _EXPRESSION_SUBQUERY._serialized_start = 19292
    _EXPRESSION_SUBQUERY._serialized_end = 20541
    _EXPRESSION_SUBQUERY_SCALAR._serialized_start = 19605
    _EXPRESSION_SUBQUERY_SCALAR._serialized_end = 19647
    _EXPRESSION_SUBQUERY_INPREDICATE._serialized_start = 19649
    _EXPRESSION_SUBQUERY_INPREDICATE._serialized_end = 19747
    _EXPRESSION_SUBQUERY_SETPREDICATE._serialized_start = 19750
    _EXPRESSION_SUBQUERY_SETPREDICATE._serialized_end = 19983
    _EXPRESSION_SUBQUERY_SETPREDICATE_PREDICATEOP._serialized_start = 19890
    _EXPRESSION_SUBQUERY_SETPREDICATE_PREDICATEOP._serialized_end = 19983
    _EXPRESSION_SUBQUERY_SETCOMPARISON._serialized_start = 19986
    _EXPRESSION_SUBQUERY_SETCOMPARISON._serialized_end = 20524
    _EXPRESSION_SUBQUERY_SETCOMPARISON_COMPARISONOP._serialized_start = 20258
    _EXPRESSION_SUBQUERY_SETCOMPARISON_COMPARISONOP._serialized_end = 20435
    _EXPRESSION_SUBQUERY_SETCOMPARISON_REDUCTIONOP._serialized_start = 20437
    _EXPRESSION_SUBQUERY_SETCOMPARISON_REDUCTIONOP._serialized_end = 20524
    _SORTFIELD._serialized_start = 20556
    _SORTFIELD._serialized_end = 20977
    _SORTFIELD_SORTDIRECTION._serialized_start = 20743
    _SORTFIELD_SORTDIRECTION._serialized_end = 20964
    _AGGREGATEFUNCTION._serialized_start = 20980
    _AGGREGATEFUNCTION._serialized_end = 21598
    _AGGREGATEFUNCTION_REFERENCEREL._serialized_start = 21408
    _AGGREGATEFUNCTION_REFERENCEREL._serialized_end = 21463
    _AGGREGATEFUNCTION_AGGREGATIONINVOCATION._serialized_start = 21466
    _AGGREGATEFUNCTION_AGGREGATIONINVOCATION._serialized_end = 21598