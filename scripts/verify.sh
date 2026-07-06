#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$SCRIPT_DIR/lib/common.sh"
source "$SCRIPT_DIR/lib/output.sh"

print_header
print_action "Verify"

print_section "Compile"

python -m compileall app >/dev/null
pass "compileall"

print_section "Tests"

pytest -q --disable-warnings
pass "pytest"

print_section "Health"

"$SCRIPT_DIR/doctor.sh"
pass "doctor"

echo
pass "Project verification successful"
