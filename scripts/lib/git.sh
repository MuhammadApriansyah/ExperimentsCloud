#!/usr/bin/env bash

check_repository() {

    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then

        pass "Git repository"

    else

        fail "Git repository"

    fi

}

check_remote() {

    if git remote get-url origin >/dev/null 2>&1; then

        pass "Git remote"

    else

        warn "Git remote"

    fi

}

check_clean_tree() {

    if git diff --quiet && git diff --cached --quiet; then

        pass "Working tree clean"

    else

        warn "Working tree dirty"

    fi

}
