#!/data/data/com.termux/files/usr/bin/bash

source "$(dirname "$0")/lib/common.sh"

action "Run Server"

info "Starting Flask development server..."

echo

python run.py
