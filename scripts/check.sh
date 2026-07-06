#!/usr/bin/env bash

source "$(dirname "$0")/lib/common.sh"

action "Project Validation"

info "Compiling project..."

python -m compileall app

check "Compilation successful"

info "Importing application..."

python -c "import app"

check "Import successful"

info "Checking routes..."

flask --app run.py routes

check "Routes loaded"

footer "Project validation completed."
