{
  description = "gRPC Python development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          name = "pygrpc-dev-shell";

          # generate protoc stubs for python
          nativeBuildInputs = with pkgs; [
            gnumake    # provides 'make' binary for 'make generate'
            buf        # provices 'buf' binary for 'buf generate'
          ];

          # Runtimes and package managers
          buildInputs = with pkgs; [
            uv         # High-speed package management
            # python312Packages.python provided by uv
          ];

          # Automation hook on environment entry
          shellHook = ''
            echo "Entered pygrpc Nix DevShell"
            echo "Available commands:"
            echo "  - uv run buf generate  (Recommended)"
            echo "  - make generate        (Alternative)"

            # Automatically provision environment and sync locks if missing
            if [ ! -d ".venv" ]; then
              echo "Creating virtual environment and sync dependencies..."
              uv venv
              uv sync
            fi
          '';
        };
      });
}
