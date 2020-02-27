# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pptloggi/v1/pptloggi.proto

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
  name='pptloggi/v1/pptloggi.proto',
  package='loggi.pptloggi.v1',
  syntax='proto3',
  serialized_options=_b('\n\025com.loggi.pptloggi.v1B\rPptloggiProtoP\001Z\npptloggiv1\242\002\003LPX\252\002\021Loggi.Pptloggi.V1\312\002\021Loggi\\Pptloggi\\V1'),
  serialized_pb=_b('\n\x1apptloggi/v1/pptloggi.proto\x12\x11loggi.pptloggi.v1\":\n\x07\x44isplay\x12\x16\n\x0estation_number\x18\x01 \x01(\x05\x12\x17\n\x0f\x64isplay_address\x18\x02 \x01(\t*9\n\x04Mode\x12\x10\n\x0cMODE_INVALID\x10\x00\x12\x0f\n\x0bMODE_NORMAL\x10\x01\x12\x0e\n\nMODE_BLINK\x10\x02*\x81\x01\n\x05\x43olor\x12\x11\n\rCOLOR_INVALID\x10\x00\x12\r\n\tCOLOR_RED\x10\x01\x12\x0f\n\x0b\x43OLOR_GREEN\x10\x02\x12\x0e\n\nCOLOR_BLUE\x10\x03\x12\x10\n\x0c\x43OLOR_YELLOW\x10\x04\x12\x11\n\rCOLOR_MAGENTA\x10\x05\x12\x10\n\x0c\x43OLOR_PURPLE\x10\x06\x42\x62\n\x15\x63om.loggi.pptloggi.v1B\rPptloggiProtoP\x01Z\npptloggiv1\xa2\x02\x03LPX\xaa\x02\x11Loggi.Pptloggi.V1\xca\x02\x11Loggi\\Pptloggi\\V1b\x06proto3')
)

_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='loggi.pptloggi.v1.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODE_NORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODE_BLINK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=109,
  serialized_end=166,
)
_sym_db.RegisterEnumDescriptor(_MODE)

Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='loggi.pptloggi.v1.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLOR_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_RED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_GREEN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_BLUE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_YELLOW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_MAGENTA', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR_PURPLE', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=298,
)
_sym_db.RegisterEnumDescriptor(_COLOR)

Color = enum_type_wrapper.EnumTypeWrapper(_COLOR)
MODE_INVALID = 0
MODE_NORMAL = 1
MODE_BLINK = 2
COLOR_INVALID = 0
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_BLUE = 3
COLOR_YELLOW = 4
COLOR_MAGENTA = 5
COLOR_PURPLE = 6



_DISPLAY = _descriptor.Descriptor(
  name='Display',
  full_name='loggi.pptloggi.v1.Display',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station_number', full_name='loggi.pptloggi.v1.Display.station_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_address', full_name='loggi.pptloggi.v1.Display.display_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=49,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Display'] = _DISPLAY
DESCRIPTOR.enum_types_by_name['Mode'] = _MODE
DESCRIPTOR.enum_types_by_name['Color'] = _COLOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Display = _reflection.GeneratedProtocolMessageType('Display', (_message.Message,), {
  'DESCRIPTOR' : _DISPLAY,
  '__module__' : 'pptloggi.v1.pptloggi_pb2'
  # @@protoc_insertion_point(class_scope:loggi.pptloggi.v1.Display)
  })
_sym_db.RegisterMessage(Display)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)