#!/usr/bin/env bash

source "$(dirname "$0")/lib/common.sh"


header

echo " Action : Clean Development Artifacts"

echo

info "Removing Python cache..."

find . -type d -name "__pycache__" -exec rm -rf {} +

find . -name "*.pyc" -delete

find . -name "*.pyo" -delete

check "Python cache removed"

info "Removing pytest cache..."

rm -rf .pytest_cache

check "Pytest cache removed"

info "Removing coverage files..."

rm -f .coverage

rm -rf htmlcov

check "Coverage artifacts removed"

echo
echo "========================================"
echo " Clean completed successfully."
echo "========================================"
echo
