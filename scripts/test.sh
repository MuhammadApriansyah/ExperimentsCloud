#!/data/data/com.termux/files/usr/bin/bash

source "$(dirname "$0")/lib/common.sh"

action "Run Test Suite"

info "Running pytest..."

echo

START=$(date +%s)

pytest || fail "Test suite failed"

END=$(date +%s)

DURATION=$((END - START))

echo

check "All tests passed"

echo

stat "Execution" "${DURATION} seconds"

footer "Test suite completed successfully."
