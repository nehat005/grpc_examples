# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsend_data.proto\"&\n\x0bSendRequest\x12\x17\n\x0frequest_message\x18\x01 \x01(\t\"Y\n\x05Queue\x12\x1d\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0f.Queue.TimeData\x1a\x31\n\x08TimeData\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x12\n\nspeaker_id\x18\x02 \x01(\t\"&\n\x0cSendResponse\x12\x16\n\x06queues\x18\x01 \x01(\x0b\x32\x06.Queue27\n\x08SendData\x12+\n\nSingleData\x12\x0c.SendRequest\x1a\r.SendResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'send_data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SENDREQUEST._serialized_start=19
  _SENDREQUEST._serialized_end=57
  _QUEUE._serialized_start=59
  _QUEUE._serialized_end=148
  _QUEUE_TIMEDATA._serialized_start=99
  _QUEUE_TIMEDATA._serialized_end=148
  _SENDRESPONSE._serialized_start=150
  _SENDRESPONSE._serialized_end=188
  _SENDDATA._serialized_start=190
  _SENDDATA._serialized_end=245
# @@protoc_insertion_point(module_scope)
