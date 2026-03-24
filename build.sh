#!/bin/bash

# Fetch full history for mdbook-blame
git fetch --unshallow

set -e

echo "Running the unified documentation build script..."
python build.py