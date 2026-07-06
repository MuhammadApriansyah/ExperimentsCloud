#!/usr/bin/env bash

check_binary() {

    local binary="$1"

    if command -v "$binary" >/dev/null 2>&1; then

        pass "$binary"

    else

        fail "$binary"

    fi

}

check_python() {

    if command -v python >/dev/null 2>&1; then

        pass "Python $(python --version | awk '{print $2}')"

    else

        fail "Python"

    fi

}

check_git() {

    check_binary git

}

check_sqlite() {

    check_binary sqlite3

}

check_ffmpeg() {

    check_binary ffmpeg

}

check_ffprobe() {

    check_binary ffprobe

}

check_pip() {

    check_binary pip

}
