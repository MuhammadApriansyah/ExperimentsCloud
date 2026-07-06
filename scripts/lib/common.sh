#!/usr/bin/env bash

#
# Shared Library
# ExperimentsCloud Utilities
#

set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

header() {

    echo
    echo "========================================"
    echo " ExperimentsCloud Utility"
    echo "========================================"
    echo

}

section() {

    echo
    echo "$1"

}

check() {

    PASSED=$((PASSED + 1))

    printf "    ✓ %s\n" "$1"

}

fail() {

    FAILED=$((FAILED + 1))

    printf "    ✗ %s\n" "$1"

}

info() {

    printf "    * %s\n" "$1"

}

stat() {

    printf "    %-14s : %s\n" "$1" "$2"

}

die() {

    fail "$1"
    exit 1

}

require_file() {

    local FILE="$1"
    local NAME="$2"

    if [ ! -f "$FILE" ]; then
        die "$NAME not found: $FILE"
    fi

}

require_directory() {

    local DIR="$1"
    local NAME="$2"

    if [ ! -d "$DIR" ]; then
        die "$NAME not found: $DIR"
    fi

}

ensure_directory() {

    mkdir -p "$1"

}

line() {

    echo "========================================"

}

footer() {

    echo

    line

    echo " $1"

    line

    echo

}

action() {

    header

    echo " Action : $1"

    echo

}

check() {

    PASSED=$((PASSED + 1))

    printf "    ✓ %s\n" "$1"

}

fail() {

    FAILED=$((FAILED + 1))

    printf "    ✗ %s\n" "$1"

}

verify_table() {

    local table="$1"
    local tables="$2"

    if echo "$tables" | grep -qw "$table"; then
        check "$table"
    else
        die "Missing table: $table"
    fi

}
