"""Example gRPC client invoking GreeterService and TimeService."""

import logging

import grpc

from pygrpc.greeter.v1 import greeter_pb2, greeter_pb2_grpc


def run() -> None:
    """Connect to the gRPC server and invoke RPC methods."""
    # Open a gRPC channel to the running server
    with grpc.insecure_channel("localhost:50051") as channel:
        # Test the GreeterService
        greeter_stub = greeter_pb2_grpc.GreeterServiceStub(channel)
        hello_request = greeter_pb2.SayHelloRequest(name="Developer")
        hello_response = greeter_stub.SayHello(hello_request)

        print("GreeterService Response:")
        print("Message: ", hello_response.message)

        # Test the TimeService
        time_stub = greeter_pb2_grpc.TimeServiceStub(channel)
        time_request = greeter_pb2.TimeRequest(name="Developer")
        time_response = time_stub.Time(time_request)

        dt = time_response.current_time.ToDatetime()

        print("TimeService Response")
        print(f"Message: {time_response.message}")
        print(f"Server Time: {dt.isoformat()} UTC.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
