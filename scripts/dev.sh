#!/usr/bin/env bash

case "$1" in

clean)

    bash scripts/cleanup.sh
    ;;

verify)

    bash scripts/verify.sh
    ;;

check)

    bash scripts/check.sh
    ;;

test)

    bash scripts/test.sh
    ;;

*)

    echo
    echo "ExperimentsCloud Developer Tools"
    echo
    echo "Usage:"
    echo
    echo "  ./scripts/dev.sh clean"
    echo "  ./scripts/dev.sh verify"
    echo "  ./scripts/dev.sh check"
    echo "  ./scripts/dev.sh test"
    echo
    ;;

esac
