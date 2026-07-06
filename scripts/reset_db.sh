#!/usr/bin/env bash

set -e

source "$(dirname "$0")/lib/common.sh"

action "Reset Database"

echo

info "Removing existing database..."

rm -f "$ROOT_DIR/database/experiments.db"

check "Database removed"

info "Running Alembic migrations..."

flask db upgrade || fail "Migration failed"

check "Migration completed"

info "Verifying database..."

TABLES=$(sqlite3 "$ROOT_DIR/database/experiments.db" ".tables")

for TABLE in users files folders alembic_version
do
    verify_table "$TABLE" "$TABLES"
done

echo

for TABLE in users files folders
do
    echo "$TABLES" | grep -q "$TABLE" \
        || fail "$TABLE table missing"
done

check "Database verification passed"

footer "Reset completed successfully."
