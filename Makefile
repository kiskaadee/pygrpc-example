.PHONY: generate generate-buf gen-buf gen-legacy

# Default action targets the recommended approach
generate: generate-buf

generate-buf:
	uv run buf generate

gen-buf: generate-buf

gen-legacy:
	uv run python -m grpc_tools.protoc \
		-I. \
		--python_out=src/pygrpc/ \
		--grpc_python_out=src/pygrpc/ \
		--mypy_out=src/pygrpc/ \
		--mypy_grpc_out=src/pygrpc/ \
		greeter/v1/greeter.proto
