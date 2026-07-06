#!/usr/bin/env bash

PASS_COUNT=0
WARN_COUNT=0
FAIL_COUNT=0


print_header() {
    echo
    echo "========================================"
    echo "        ExperimentsCloud Utility"
    echo "========================================"
    echo
}

print_action() {
    echo " Action : $1"
    echo
}

print_section() {
    echo
    echo "$1"
    printf '%*s\n' "${#1}" "" | tr ' ' '-'
}

pass() {
    printf "    ✓ %s\n" "$1"
    PASS_COUNT=$((PASS_COUNT + 1))
}

warn() {
    printf "    ⚠ %s\n" "$1"
    WARN_COUNT=$((WARN_COUNT + 1))
}

fail() {
    printf "    ✗ %s\n" "$1"
    FAIL_COUNT=$((FAIL_COUNT + 1))
}

summary() {

    echo
    echo "========================================"
    echo "               Summary"
    echo "========================================"
    echo

    printf " PASS : %d\n" "$PASS_COUNT"
    printf " WARN : %d\n" "$WARN_COUNT"
    printf " FAIL : %d\n" "$FAIL_COUNT"

    echo

    if [ "$FAIL_COUNT" -eq 0 ]; then
        return 0
    fi

    return 1
}
