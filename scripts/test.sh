#!/usr/bin/env bash

set -e

pytest \
    -v \
    --cov=app \
    --cov-branch \
    --cov-report=term-missing \
    --cov-report=html
