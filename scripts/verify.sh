#!/usr/bin/env bash

set -e

echo "========================================"
echo "ExperimentsCloud Verification"
echo "========================================"

echo
echo "[1/3] Static checks..."
bash scripts/check.sh

echo
echo "[2/3] Application factory..."

python -c "
from app import create_app

app = create_app()

print('Application OK')
"

echo
echo "[3/3] Configuration..."

python -c "
from app.config import get_config

print(get_config().__name__)
"

echo
echo "Verification completed successfully."
