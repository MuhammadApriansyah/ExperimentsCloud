#!/data/data/com.termux/files/usr/bin/bash

source "$(dirname "$0")/lib/common.sh"

START_TIME=$(date +%s%N)

DATABASE="$ROOT_DIR/database/experiments.db"

HEALTH=0

action "Doctor"

#
# Python
#

section "Python"

if command -v python >/dev/null 2>&1; then
    check "$(python --version)"
else
    fail "Python not found"
    HEALTH=$((HEALTH + 1))
fi

echo

#
# Virtual Environment
#

section "Virtual Environment"

if [ -n "$VIRTUAL_ENV" ]; then
    check "Active"
else
    fail "Not active"
    HEALTH=$((HEALTH + 1))
fi

echo

#
# Database
#

section "Database"

if [ -f "$DATABASE" ]; then

    check "Found"

    SIZE=$(du -h "$DATABASE" | cut -f1)

    echo "    Size : $SIZE"

else

    fail "Missing"

    HEALTH=$((HEALTH + 1))

fi

echo

#
# Tables
#

section "Tables"

TABLES=$(sqlite3 "$DATABASE" ".tables")

for TABLE in users files folders alembic_version

do
    if echo "$TABLES" | grep -q "$TABLE"; then
        check "$TABLE"
    else
        fail "$TABLE"
        HEALTH=$((HEALTH + 1))
fi

done

echo

#
# Database Records
#

section "Database Records"

for TABLE in users folders files
do
    if echo "$TABLES" | grep -qw "$TABLE"; then

        COUNT=$(sqlite3 "$DATABASE" "SELECT COUNT(*) FROM $TABLE;")

        stat "$(tr '[:lower:]' '[:upper:]' <<< ${TABLE:0:1})${TABLE:1}" "$COUNT"

    else

        stat "$(tr '[:lower:]' '[:upper:]' <<< ${TABLE:0:1})${TABLE:1}" "N/A"

    fi
done

echo

#
# Storage
#

section "Storage"

for DIR in \
storage \
storage/users \
storage/temp \
storage/thumbnails \
storage/trash
do

    if [ -d "$ROOT_DIR/$DIR" ]; then
        check "$DIR"

        SIZE=$(du -sh "$ROOT_DIR/$DIR" | cut -f1)

        echo "      Size : $SIZE"
    else
        fail "$DIR"

        HEALTH=$((HEALTH + 1))

    fi

done

echo

TOTAL_STORAGE=$(du -sh "$ROOT_DIR/storage" 2>/dev/null | cut -f1)

echo "    Total : $TOTAL_STORAGE"

echo

#
# Backups
#

section "Backups"

if [ -d "$ROOT_DIR/backups" ]; then

    check "backups"

    BACKUP_COUNT=$(find "$ROOT_DIR/backups" -maxdepth 1 -name "*.db" | wc -l)

    BACKUP_SIZE=$(du -sh "$ROOT_DIR/backups" | cut -f1)

    echo "    Count : $BACKUP_COUNT"

    echo "    Size  : $BACKUP_SIZE"

    LATEST_BACKUP=$(
    find "$ROOT_DIR/backups" \
    -maxdepth 1 \
    -type f \
    -name "*.db" \
    -print0 |
    xargs -0 ls -t |
    head -1
    )

    if [ -n "$LATEST_BACKUP" ]
    then
        echo "    Latest: $(basename "$LATEST_BACKUP")"
    fi

else

    fail "backups"

    HEALTH=$((HEALTH + 1))

fi

echo

#
# Scripts
#

section "Scripts"

for FILE in \
run.sh \
test.sh \
check.sh \
clean.sh \
reset_db.sh \
backup_db.sh \
restore_db.sh
do

    if [ -x "$ROOT_DIR/scripts/$FILE" ]; then
        check "$FILE"

    else

        fail "$FILE"

        HEALTH=$((HEALTH + 1))

    fi

done

echo

#
# Migration
#

section "Migration"

CURRENT=$(flask db current 2>/dev/null | head -1)

if [ -n "$CURRENT" ]; then

    check "$CURRENT"

else

    fail "Unable to determine revision"

    HEALTH=$((HEALTH + 1))

fi

echo

#
# Git
#

section "Git"

if git rev-parse --is-inside-work-tree >/dev/null 2>&1
then

    check "Repository"

    BRANCH=$(git branch --show-current)

    COMMIT=$(git rev-parse --short HEAD)

    STATUS=$(git status --porcelain)

    STATUS_COUNT=$(echo "$STATUS" | sed '/^$/d' | wc -l)

    echo "    Branch : $BRANCH"

    echo "    Commit : $COMMIT"

    if [ -z "$STATUS" ]
    then
        echo "    Status : Clean"
    else
        echo "    Status : Modified ($STATUS_COUNT files)"
    fi

else

    fail "Not a Git repository"

    HEALTH=$((HEALTH + 1))

fi

echo

#
# Project Statistics
#

section "Project Statistics"

model_count=$(
    find app/models \
    -type f \
    -name "*.py" \
    ! -name "__init__.py" \
    | wc -l
)

template_count=$(
    find app/templates \
    -type f \
    -name "*.html" \
    | wc -l
)

script_count=$(
    find scripts \
    -maxdepth 1 \
    -type f \
    -name "*.sh" \
    | wc -l
)

test_count=$(
    pytest --collect-only -q 2>/dev/null \
    | awk '/tests collected/ {print $1}'
)

route_count=$(
python - <<'PY'
from app import create_app

app = create_app()

print(
    sum(
        1
        for _ in app.url_map.iter_rules()
    )
)
PY
)

stat "Models" "$model_count"
stat "Scripts" "$script_count"
stat "Templates" "$template_count"
stat "Backups" "$BACKUP_COUNT"
stat "Routes" "$route_count"

echo

stat "Tests" "$test_count"

echo

#
# Overall Health
#

section "Overall Health"

TOTAL=$((PASSED + FAILED))

SCORE=$((PASSED * 100 / TOTAL))

stat "Passed" "$PASSED"
stat "Failed" "$FAILED"
stat "Score" "${SCORE}%"

echo

END_TIME=$(date +%s%N)

ELAPSED_MS=$(((END_TIME - START_TIME)/1000000))

section "Execution"

echo "    Time : ${ELAPSED_MS} ms"

footer "Doctor finished."


