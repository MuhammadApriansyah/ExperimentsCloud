#!/data/data/com.termux/files/usr/bin/bash

echo "Compile..."

python -m compileall app

echo "Import..."

python -c "import app"

echo "Routes..."

flask --app run.py routes

echo "Done."
