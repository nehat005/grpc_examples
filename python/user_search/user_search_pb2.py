# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_search.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11user_search.proto\"\x1e\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\"\x88\x01\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x1e\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\r.User.Address\x1a(\n\x07\x41\x64\x64ress\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\"8\n\x0eSearchResponse\x12\x10\n\x08page_num\x18\x01 \x01(\x05\x12\x14\n\x05users\x18\x02 \x03(\x0b\x32\x05.User2Y\n\nUserSearch\x12K\n$ListUsersStreamRequestSingleResponse\x12\x0e.SearchRequest\x1a\x0f.SearchResponse\"\x00(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_search_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SEARCHREQUEST._serialized_start=21
  _SEARCHREQUEST._serialized_end=51
  _USER._serialized_start=54
  _USER._serialized_end=190
  _USER_ADDRESS._serialized_start=150
  _USER_ADDRESS._serialized_end=190
  _SEARCHRESPONSE._serialized_start=192
  _SEARCHRESPONSE._serialized_end=248
  _USERSEARCH._serialized_start=250
  _USERSEARCH._serialized_end=339
# @@protoc_insertion_point(module_scope)
