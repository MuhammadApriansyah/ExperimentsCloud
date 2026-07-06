#!/usr/bin/env bash

DB_FILE="database/experiments.db"

check_database() {

    if [ ! -d database ]; then

        mkdir -p database

        warn "database directory created"

    else

        pass "database directory"

    fi

    if [ -f "$DB_FILE" ]; then
        TABLE_COUNT=$(
            sqlite3 "$DB_FILE" \
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table';" \
            2>/dev/null
        )

        if [ "${TABLE_COUNT:-0}" -gt 0 ]; then
            pass "database initialized ($TABLE_COUNT tables)"
        else
            warn "database empty"
        fi
    else
        warn "database not initialized"
    fi

}
