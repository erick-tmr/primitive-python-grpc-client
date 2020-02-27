# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: postalcodetable/v2/service_type_group_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='postalcodetable/v2/service_type_group_info.proto',
  package='loggi.postalcodetable.v2',
  syntax='proto3',
  serialized_options=_b('\n\034com.loggi.postalcodetable.v2B\031ServiceTypeGroupInfoProtoP\001Z\021postalcodetablev2\242\002\003LPX\252\002\030Loggi.Postalcodetable.V2\312\002\030Loggi\\Postalcodetable\\V2'),
  serialized_pb=_b('\n0postalcodetable/v2/service_type_group_info.proto\x12\x18loggi.postalcodetable.v2\"\xa0\x01\n\x14ServiceTypeGroupInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\x0cservice_type\x18\x03 \x01(\x0e\x32%.loggi.postalcodetable.v2.ServiceType\x12\x0b\n\x03slo\x18\x04 \x01(\x05\x12$\n\x1c\x63onfirmation_deadline_offset\x18\x05 \x01(\x02*\x9b\x01\n\x0bServiceType\x12\x18\n\x14SERVICE_TYPE_INVALID\x10\x00\x12\x18\n\x14SERVICE_TYPE_UNKNOWN\x10\x01\x12\x1b\n\x17SERVICE_TYPE_LOGGI_HOJE\x10\x02\x12\x1e\n\x1aSERVICE_TYPE_LOGGI_EXPRESS\x10\x03\x12\x1b\n\x17SERVICE_TYPE_REDISPATCH\x10\x04\x42\x8a\x01\n\x1c\x63om.loggi.postalcodetable.v2B\x19ServiceTypeGroupInfoProtoP\x01Z\x11postalcodetablev2\xa2\x02\x03LPX\xaa\x02\x18Loggi.Postalcodetable.V2\xca\x02\x18Loggi\\Postalcodetable\\V2b\x06proto3')
)

_SERVICETYPE = _descriptor.EnumDescriptor(
  name='ServiceType',
  full_name='loggi.postalcodetable.v2.ServiceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_LOGGI_HOJE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_LOGGI_EXPRESS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_REDISPATCH', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=242,
  serialized_end=397,
)
_sym_db.RegisterEnumDescriptor(_SERVICETYPE)

ServiceType = enum_type_wrapper.EnumTypeWrapper(_SERVICETYPE)
SERVICE_TYPE_INVALID = 0
SERVICE_TYPE_UNKNOWN = 1
SERVICE_TYPE_LOGGI_HOJE = 2
SERVICE_TYPE_LOGGI_EXPRESS = 3
SERVICE_TYPE_REDISPATCH = 4



_SERVICETYPEGROUPINFO = _descriptor.Descriptor(
  name='ServiceTypeGroupInfo',
  full_name='loggi.postalcodetable.v2.ServiceTypeGroupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='loggi.postalcodetable.v2.ServiceTypeGroupInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='loggi.postalcodetable.v2.ServiceTypeGroupInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_type', full_name='loggi.postalcodetable.v2.ServiceTypeGroupInfo.service_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slo', full_name='loggi.postalcodetable.v2.ServiceTypeGroupInfo.slo', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmation_deadline_offset', full_name='loggi.postalcodetable.v2.ServiceTypeGroupInfo.confirmation_deadline_offset', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=79,
  serialized_end=239,
)

_SERVICETYPEGROUPINFO.fields_by_name['service_type'].enum_type = _SERVICETYPE
DESCRIPTOR.message_types_by_name['ServiceTypeGroupInfo'] = _SERVICETYPEGROUPINFO
DESCRIPTOR.enum_types_by_name['ServiceType'] = _SERVICETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceTypeGroupInfo = _reflection.GeneratedProtocolMessageType('ServiceTypeGroupInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVICETYPEGROUPINFO,
  '__module__' : 'postalcodetable.v2.service_type_group_info_pb2'
  # @@protoc_insertion_point(class_scope:loggi.postalcodetable.v2.ServiceTypeGroupInfo)
  })
_sym_db.RegisterMessage(ServiceTypeGroupInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)