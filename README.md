# pygrpc-example

A hands-on learning project demonstrating modern Python gRPC development, protobuf code generation, type hinting, and service implementation using `uv` and `buf`.

---

## 🚀 Features

- **gRPC Services**:
  - `GreeterService`: Simple unary RPC (`SayHello`) returning greeting messages.
  - `TimeService`: Unary RPC (`Time`) utilizing Google's well-known `google.protobuf.Timestamp`.
- **Modern Tooling**:
  - **[uv](https://github.com/astral-sh/uv)** for fast Python packaging and dependency management.
  - **[Buf](https://buf.build/)** for remote code generation with type stubs (`mypy-protobuf`).
  - **[Ruff](https://docs.astral.sh/ruff/)** & **[Pyright](https://github.com/microsoft/pyright)** for linting and static typing.
- **Nix Flake support** (`flake.nix`) for reproducible development environments.

---

## 📁 Project Structure

```text
.
├── Makefile                     # Helper targets for code generation
├── buf.gen.yaml                 # Buf code generation configuration
├── buf.yaml                     # Buf module definition
├── flake.nix                    # Nix development shell
├── pyproject.toml               # Project metadata & dependencies
├── greeter/
│   └── v1/
│       └── greeter.proto        # Protobuf schema definition
└── src/
    └── pygrpc/
        ├── client.py            # Example gRPC client
        ├── server.py            # gRPC server implementation
        └── greeter/v1/          # Generated protobuf/gRPC Python stubs
```

---

## 🛠️ Prerequisites & Setup

### Option A: Using Nix (Recommended)
The included [`flake.nix`](file:///home/kiskaadee/Experiments/pygrpc/flake.nix) provides a hermetic dev environment with `uv`, `buf`, and `gnumake` bundled, and automatically syncs the virtual environment on entry:

```bash
nix develop
```

### Option B: Manual Setup (Without Nix)
If not using Nix, install [uv](https://docs.astral.sh/uv/) and run:

```bash
uv sync
```

---

## ⚙️ Protobuf Code Generation

The repository supports two methods for generating gRPC stubs:

### Option 1: Buf (Recommended)
Uses remote plugins configured in `buf.gen.yaml` to generate Python code and `.pyi` type stubs:

```bash
make generate
# or directly:
uv run buf generate
```

### Option 2: Legacy `grpc_tools.protoc`
Generates stubs locally via `grpcio-tools` and `mypy-protobuf`:

```bash
make gen-legacy
```

---

## 🏃 Running the Services

### 1. Start the gRPC Server
Run the server (listening on port `50051` by default):

```bash
uv run python -m pygrpc.server
```

### 2. Run the gRPC Client
In another terminal, run the client to test both `GreeterService` and `TimeService`:

```bash
uv run python -m pygrpc.client
```

**Expected Output:**
```text
GreeterService Response:
Message:  Hello, Developer!
TimeService Response
Message: It's a beautiful day
Server Time: 2026-09-01T17:22:15.123456+00:00 UTC.
```

---

## 🧹 Code Quality & Linting

Run formatting, linting, and type checking:

```bash
# Check linting & formatting with Ruff
uv run ruff check .
uv run ruff format --check .

# Type check with Pyright
uv run pyright
```
