#!/usr/bin/env bash

set -e

echo "Compile..."

python -m compileall app

echo "Import..."

python -c "import app"

echo "Routes..."

flask --app run.py routes

echo "Done."
