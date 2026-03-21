#!/bin/bash
git fetch --unshallow

set -e

echo "Running the unified documentation build script..."
python build.py