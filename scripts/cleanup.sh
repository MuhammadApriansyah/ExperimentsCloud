#!/usr/bin/env bash

echo "========================================"
echo "ExperimentsCloud Cleanup"
echo "========================================"

echo "[1/4] Removing __pycache__..."
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "[2/4] Removing *.pyc..."
find . -type f -name "*.pyc" -delete

echo "[3/4] Removing *.pyo..."
find . -type f -name "*.pyo" -delete

echo "[4/4] Removing temporary files..."
find . -type f -name "*.tmp" -delete

echo
echo "Cleanup completed successfully."
