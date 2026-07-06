#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"

DATABASE="$ROOT_DIR/database/experiments.db"
BACKUP_DIR="$ROOT_DIR/backups"

header

echo " Action : Backup Database"

echo

info "Creating backup directory..."
mkdir -p "$BACKUP_DIR"
check "Backup directory ready"

if [ ! -f "$DATABASE" ]; then

    die "Database not found: $DATABASE"

fi

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

BACKUP_FILE="$BACKUP_DIR/experiments_$TIMESTAMP.db"

info "Creating backup..."
cp "$DATABASE" "$BACKUP_FILE"

check "Backup created"

echo
echo "Location:"
echo "$BACKUP_FILE"

echo
echo "========================================"
echo " Backup completed successfully."
echo "========================================"
