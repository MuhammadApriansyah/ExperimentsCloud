#!/usr/bin/env bash

set -e

trap 'echo; echo "CI failed."; exit 1' ERR

echo "========================================"
echo "ExperimentsCloud CI"
echo "========================================"

echo
echo "[1/3] Static checks..."
bash scripts/check.sh

echo
echo "[2/3] Running tests..."
bash scripts/test.sh

echo
echo "[3/3] Cleanup..."
bash scripts/cleanup.sh

echo
echo "CI completed successfully."
