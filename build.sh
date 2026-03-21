#!/bin/bash
set -e

# Fetch the official standalone mdBook binary from the Rust releases page
MDBOOK_VERSION="0.4.37"
echo "Downloading mdBook v${MDBOOK_VERSION}..."
curl -sL https://github.com/rust-lang/mdBook/releases/download/v${MDBOOK_VERSION}/mdbook-v${MDBOOK_VERSION}-x86_64-unknown-linux-gnu.tar.gz | tar -xz

# Add the downloaded mdbook binary to the PATH so build.py can natively call it
export PATH=$PATH:$(pwd)

echo "Running the unified documentation build script..."
python build.py

