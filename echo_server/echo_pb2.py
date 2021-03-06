# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo_server/echo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo_server/echo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x65\x63ho_server/echo.proto\"=\n\x0bTextMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t2]\n\x0b\x45\x63hoService\x12\"\n\x04\x45\x63ho\x12\x0c.TextMessage\x1a\x0c.TextMessage\x12*\n\x08\x45\x63hoMany\x12\x0c.TextMessage\x1a\x0c.TextMessage(\x01\x30\x01\x62\x06proto3'
)




_TEXTMESSAGE = _descriptor.Descriptor(
  name='TextMessage',
  full_name='TextMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TextMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='TextMessage.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='TextMessage.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['TextMessage'] = _TEXTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextMessage = _reflection.GeneratedProtocolMessageType('TextMessage', (_message.Message,), {
  'DESCRIPTOR' : _TEXTMESSAGE,
  '__module__' : 'echo_server.echo_pb2'
  # @@protoc_insertion_point(class_scope:TextMessage)
  })
_sym_db.RegisterMessage(TextMessage)



_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='EchoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=89,
  serialized_end=182,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='EchoService.Echo',
    index=0,
    containing_service=None,
    input_type=_TEXTMESSAGE,
    output_type=_TEXTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EchoMany',
    full_name='EchoService.EchoMany',
    index=1,
    containing_service=None,
    input_type=_TEXTMESSAGE,
    output_type=_TEXTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHOSERVICE)

DESCRIPTOR.services_by_name['EchoService'] = _ECHOSERVICE

# @@protoc_insertion_point(module_scope)
