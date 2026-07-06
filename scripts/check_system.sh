#!/usr/bin/env bash

echo "========== System Dependency Check =========="

check_binary () {
    if command -v "$1" >/dev/null 2>&1; then
        echo "[PASS] $1"
        "$1" -version | head -1
    else
        echo "[FAIL] $1"
    fi
    echo
}

check_binary ffprobe
check_binary ffmpeg
