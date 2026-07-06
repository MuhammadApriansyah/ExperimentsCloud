#!/usr/bin/env bash

check_directory() {

    local dir="$1"

    if [ -d "$dir" ]; then

        pass "$dir"

    else

        warn "$dir (missing)"

    fi

}

check_project() {

    check_directory app
    check_directory database
    check_directory storage
    check_directory logs

}
