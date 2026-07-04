# Development

## Setup

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python run.py

## Database

flask db migrate

flask db upgrade

## Tests

pytest
