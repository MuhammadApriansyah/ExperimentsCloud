#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$SCRIPT_DIR/lib/common.sh"
source "$SCRIPT_DIR/lib/output.sh"
source "$SCRIPT_DIR/lib/dependencies.sh"
source "$SCRIPT_DIR/lib/project.sh"
source "$SCRIPT_DIR/lib/database.sh"
source "$SCRIPT_DIR/lib/git.sh"

print_header

print_action "Doctor"

print_section "Environment"

check_python
check_pip

print_section "Dependencies"

check_git
check_sqlite
check_ffmpeg
check_ffprobe

print_section "Project"

check_project

print_section "Database"

check_database

print_section "Git"

check_repository
check_remote
check_clean_tree

summary
