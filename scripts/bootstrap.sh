#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$SCRIPT_DIR/lib/common.sh"
source "$SCRIPT_DIR/lib/output.sh"
source "$SCRIPT_DIR/lib/dependencies.sh"

print_header
print_action "Bootstrap"

print_section "Environment"

check_python
check_pip

print_section "Virtual Environment"

if [ ! -d venv ]; then
    python -m venv venv
    pass "virtual environment created"
else
    pass "virtual environment exists"
fi

source venv/bin/activate

print_section "Dependencies"

pip install --upgrade pip

pip install -r requirements.txt

pass "requirements installed"

print_section "Project"

mkdir -p database
mkdir -p logs
mkdir -p storage/users
mkdir -p storage/temp
mkdir -p storage/trash
mkdir -p storage/thumbnails

pass "project directories ready"

print_section "Database"

python - <<'EOF'
from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
EOF

pass "database initialized"

print_section "Health Check"

"$SCRIPT_DIR/doctor.sh"

echo
pass "Bootstrap complete"
