"""gRPC server implementation hosting GreeterService and TimeService."""

import logging
from concurrent import futures

import grpc
from google.protobuf.timestamp_pb2 import Timestamp

from pygrpc.greeter.v1 import greeter_pb2, greeter_pb2_grpc


class GreeterService(greeter_pb2_grpc.GreeterServiceServicer):
    """Provides greeting responses."""

    def SayHello(
        self,
        request: greeter_pb2.SayHelloRequest,
        context: grpc.ServicerContext,
    ) -> greeter_pb2.SayHelloResponse:

        logging.info(f"Received request from {request.name}")
        return greeter_pb2.SayHelloResponse(message=f"Hello, {request.name}!")


class TimeService(greeter_pb2_grpc.TimeServiceServicer):
    """Provides current server time with timestamp protobuf."""

    def Time(
        self,
        request: greeter_pb2.TimeRequest,
        context: grpc.ServicerContext,
    ) -> greeter_pb2.TimeResponse:
        logging.info(f"Time request received by {request.name}")
        current_time = Timestamp()
        current_time.GetCurrentTime()
        return greeter_pb2.TimeResponse(
            current_time=current_time,
            message="It's a beautiful day",
        )


def serve(port: int = 50051) -> None:
    """Start the gRPC server and block waiting for termination."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    greeter_pb2_grpc.add_GreeterServiceServicer_to_server(GreeterService(), server)
    greeter_pb2_grpc.add_TimeServiceServicer_to_server(TimeService(), server)

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    logging.info(f"Server started, listening on port: {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
