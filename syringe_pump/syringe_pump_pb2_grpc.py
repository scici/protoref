# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import syringe_pump_pb2 as syringe__pump__pb2


class SyringePumpStub(object):
  """Interface exported by each Syringe Pump server
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendInstruction = channel.unary_unary(
        '/syringe_pump.SyringePump/SendInstruction',
        request_serializer=syringe__pump__pb2.Instruction.SerializeToString,
        response_deserializer=syringe__pump__pb2.Status.FromString,
        )
    self.GetStatus = channel.unary_unary(
        '/syringe_pump.SyringePump/GetStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=syringe__pump__pb2.Status.FromString,
        )
    self.GetStatusStreamed = channel.unary_stream(
        '/syringe_pump.SyringePump/GetStatusStreamed',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=syringe__pump__pb2.Status.FromString,
        )


class SyringePumpServicer(object):
  """Interface exported by each Syringe Pump server
  """

  def SendInstruction(self, request, context):
    """Sends syringe pump instructions and receives current status back
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStatus(self, request, context):
    """Receive current syringe pump status
    Empty argument indicates that no arguments are passed
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStatusStreamed(self, request, context):
    """Stream status from a syringe pump
    Empty argument indicates that no arguments are passed
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SyringePumpServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendInstruction': grpc.unary_unary_rpc_method_handler(
          servicer.SendInstruction,
          request_deserializer=syringe__pump__pb2.Instruction.FromString,
          response_serializer=syringe__pump__pb2.Status.SerializeToString,
      ),
      'GetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=syringe__pump__pb2.Status.SerializeToString,
      ),
      'GetStatusStreamed': grpc.unary_stream_rpc_method_handler(
          servicer.GetStatusStreamed,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=syringe__pump__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'syringe_pump.SyringePump', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
