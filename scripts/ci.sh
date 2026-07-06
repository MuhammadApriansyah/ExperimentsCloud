#!/usr/bin/env bash

set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo
echo "========================================"
echo "      ExperimentsCloud CI Pipeline"
echo "========================================"
echo

echo "[1/3] Bootstrap"
"$SCRIPT_DIR/bootstrap.sh"

echo
echo "[2/3] Verification"
"$SCRIPT_DIR/verify.sh"

echo
echo "[3/3] Final Doctor"
"$SCRIPT_DIR/doctor.sh"

echo
echo "========================================"
echo "                CI PASSED"
echo "========================================"
