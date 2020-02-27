# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: integration/v1/outbound_monitoring.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='integration/v1/outbound_monitoring.proto',
  package='loggi.integration.v1',
  syntax='proto3',
  serialized_options=_b('\n\030com.loggi.integration.v1B\027OutboundMonitoringProtoP\001Z\rintegrationv1\242\002\003LIX\252\002\024Loggi.Integration.V1\312\002\024Loggi\\Integration\\V1'),
  serialized_pb=_b('\n(integration/v1/outbound_monitoring.proto\x12\x14loggi.integration.v1\"\xbb\x03\n\x15OutboundMonitoringApi\x12\x12\n\ncompany_id\x18\x01 \x01(\x03\x12\x12\n\npackage_id\x18\x02 \x01(\x03\x12\x1b\n\x13package_status_code\x18\x03 \x01(\x05\x12\x1c\n\x14package_tracking_key\x18\x04 \x01(\t\x12\x0f\n\x07task_id\x18\x05 \x01(\x03\x12\x11\n\ttask_type\x18\x06 \x01(\t\x12\x19\n\x11task_completed_at\x18\x07 \x01(\t\x12\x16\n\x0etask_is_mapped\x18\x08 \x01(\x08\x12\x1a\n\x12task_is_integrated\x18\t \x01(\x08\x12\"\n\x1atask_integration_latency_s\x18\n \x01(\x05\x12\x1c\n\x14http_request_headers\x18\x0b \x01(\t\x12\x1c\n\x14http_request_payload\x18\x0c \x01(\t\x12\x1a\n\x12http_response_body\x18\r \x01(\t\x12\x1a\n\x12http_response_code\x18\x0e \x01(\x05\x12\x1f\n\x17http_request_latency_ms\x18\x0f \x01(\x05\x12\x13\n\x0bobject_type\x18\x10 \x01(\t\"\xdb\x02\n\x16OutboundMonitoringFile\x12\x12\n\ncompany_id\x18\x01 \x01(\x03\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x17\n\x0f\x66ile_task_count\x18\x03 \x01(\x05\x12\x13\n\x0bpackage_ids\x18\x04 \x03(\x03\x12\x1d\n\x15package_tracking_keys\x18\x05 \x03(\t\x12\x10\n\x08task_ids\x18\x06 \x03(\x03\x12 \n\x18transfer_request_headers\x18\x07 \x01(\t\x12 \n\x18transfer_request_payload\x18\x08 \x01(\t\x12\x1e\n\x16transfer_response_body\x18\t \x01(\t\x12\x1e\n\x16transfer_response_code\x18\n \x01(\x05\x12#\n\x1btransfer_request_latency_ms\x18\x0b \x01(\x05\x12\x13\n\x0bobject_type\x18\x0c \x01(\tBx\n\x18\x63om.loggi.integration.v1B\x17OutboundMonitoringProtoP\x01Z\rintegrationv1\xa2\x02\x03LIX\xaa\x02\x14Loggi.Integration.V1\xca\x02\x14Loggi\\Integration\\V1b\x06proto3')
)




_OUTBOUNDMONITORINGAPI = _descriptor.Descriptor(
  name='OutboundMonitoringApi',
  full_name='loggi.integration.v1.OutboundMonitoringApi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='company_id', full_name='loggi.integration.v1.OutboundMonitoringApi.company_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='loggi.integration.v1.OutboundMonitoringApi.package_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_status_code', full_name='loggi.integration.v1.OutboundMonitoringApi.package_status_code', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_tracking_key', full_name='loggi.integration.v1.OutboundMonitoringApi.package_tracking_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='loggi.integration.v1.OutboundMonitoringApi.task_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='loggi.integration.v1.OutboundMonitoringApi.task_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_completed_at', full_name='loggi.integration.v1.OutboundMonitoringApi.task_completed_at', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_is_mapped', full_name='loggi.integration.v1.OutboundMonitoringApi.task_is_mapped', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_is_integrated', full_name='loggi.integration.v1.OutboundMonitoringApi.task_is_integrated', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_integration_latency_s', full_name='loggi.integration.v1.OutboundMonitoringApi.task_integration_latency_s', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_request_headers', full_name='loggi.integration.v1.OutboundMonitoringApi.http_request_headers', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_request_payload', full_name='loggi.integration.v1.OutboundMonitoringApi.http_request_payload', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_response_body', full_name='loggi.integration.v1.OutboundMonitoringApi.http_response_body', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_response_code', full_name='loggi.integration.v1.OutboundMonitoringApi.http_response_code', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_request_latency_ms', full_name='loggi.integration.v1.OutboundMonitoringApi.http_request_latency_ms', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_type', full_name='loggi.integration.v1.OutboundMonitoringApi.object_type', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=510,
)


_OUTBOUNDMONITORINGFILE = _descriptor.Descriptor(
  name='OutboundMonitoringFile',
  full_name='loggi.integration.v1.OutboundMonitoringFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='company_id', full_name='loggi.integration.v1.OutboundMonitoringFile.company_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='loggi.integration.v1.OutboundMonitoringFile.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_task_count', full_name='loggi.integration.v1.OutboundMonitoringFile.file_task_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_ids', full_name='loggi.integration.v1.OutboundMonitoringFile.package_ids', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_tracking_keys', full_name='loggi.integration.v1.OutboundMonitoringFile.package_tracking_keys', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_ids', full_name='loggi.integration.v1.OutboundMonitoringFile.task_ids', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_request_headers', full_name='loggi.integration.v1.OutboundMonitoringFile.transfer_request_headers', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_request_payload', full_name='loggi.integration.v1.OutboundMonitoringFile.transfer_request_payload', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_response_body', full_name='loggi.integration.v1.OutboundMonitoringFile.transfer_response_body', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_response_code', full_name='loggi.integration.v1.OutboundMonitoringFile.transfer_response_code', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_request_latency_ms', full_name='loggi.integration.v1.OutboundMonitoringFile.transfer_request_latency_ms', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_type', full_name='loggi.integration.v1.OutboundMonitoringFile.object_type', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=860,
)

DESCRIPTOR.message_types_by_name['OutboundMonitoringApi'] = _OUTBOUNDMONITORINGAPI
DESCRIPTOR.message_types_by_name['OutboundMonitoringFile'] = _OUTBOUNDMONITORINGFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OutboundMonitoringApi = _reflection.GeneratedProtocolMessageType('OutboundMonitoringApi', (_message.Message,), {
  'DESCRIPTOR' : _OUTBOUNDMONITORINGAPI,
  '__module__' : 'integration.v1.outbound_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:loggi.integration.v1.OutboundMonitoringApi)
  })
_sym_db.RegisterMessage(OutboundMonitoringApi)

OutboundMonitoringFile = _reflection.GeneratedProtocolMessageType('OutboundMonitoringFile', (_message.Message,), {
  'DESCRIPTOR' : _OUTBOUNDMONITORINGFILE,
  '__module__' : 'integration.v1.outbound_monitoring_pb2'
  # @@protoc_insertion_point(class_scope:loggi.integration.v1.OutboundMonitoringFile)
  })
_sym_db.RegisterMessage(OutboundMonitoringFile)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)