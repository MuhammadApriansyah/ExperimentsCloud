#!/data/data/com.termux/files/usr/bin/bash

python -m compileall app

python -c "import app"

flask --app run.py routes
