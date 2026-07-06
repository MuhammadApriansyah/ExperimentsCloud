#!/usr/bin/env bash

source "$(dirname "$0")/lib/common.sh"

DATABASE="$ROOT_DIR/database/experiments.db"
BACKUP_DIR="$ROOT_DIR/backups"

header

echo " Action : Restore Database"

echo

if [ $# -eq 0 ]; then

    die "Usage: ./scripts/restore_db.sh <backup_file>"

fi

BACKUP_FILE="$1"

info "Validating backup..."

require_file "$BACKUP_FILE" "Backup"

check "Backup found"

mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

SAFETY_BACKUP="$BACKUP_DIR/pre_restore_$TIMESTAMP.db"

info "Creating safety backup..."

if [ -f "$DATABASE" ]; then
    cp "$DATABASE" "$SAFETY_BACKUP"
fi

check "Safety backup created"

info "Restoring database..."

cp "$BACKUP_FILE" "$DATABASE"

check "Restore complete"

info "Verifying tables..."

TABLES=$(sqlite3 "$DATABASE" ".tables")

for TABLE in users files folders alembic_version
do
    if echo "$TABLES" | grep -q "$TABLE"; then
        check "$TABLE"
    else
        die "Missing table: $TABLE"
    fi
done

echo
echo "========================================"
echo " Restore completed successfully."
echo "========================================"
