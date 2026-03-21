#!/bin/bash
set -e

# Fetch the official standalone mdBook binary from the Rust releases page
MDBOOK_VERSION="0.4.37"
echo "Downloading mdBook v${MDBOOK_VERSION}..."
curl -sL https://github.com/rust-lang/mdBook/releases/download/v${MDBOOK_VERSION}/mdbook-v${MDBOOK_VERSION}-x86_64-unknown-linux-gnu.tar.gz | tar -xz

echo "Downloading mdbook-blame wrapper..."
BLAME_TAG=$(curl -s 'https://api.github.com/repos/Froze-N-Milk/mdbook-blame/releases/latest' | jq -r '.tag_name')
mkdir -p mdbook-blame
curl -sSL "https://github.com/Froze-N-Milk/mdbook-blame/releases/download/${BLAME_TAG}/mdbook-blame-${BLAME_TAG}-x86_64-unknown-linux-gnu.tar.gz" | tar -xz --directory=./mdbook-blame

# Add both downloaded binaries to the execution PATH
export PATH=$PATH:$(pwd):$(pwd)/mdbook-blame

echo "Running the unified documentation build script..."
python build.py
