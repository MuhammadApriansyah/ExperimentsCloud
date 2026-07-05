# ExperimentsCloud

Personal Cloud Storage

## Features

Authentication

Upload

Download

File Listing

## Stack

Python

Flask

SQLite

SQLAlchemy

Flask Login

Flask Migrate

## Structure

app/

storage/

database/

migrations/

docs/

tests/

# ExperimentsCloud

ExperimentsCloud is a lightweight personal cloud storage application built with Flask.

## Features

- User authentication
- Secure file upload
- File download
- File deletion
- UUID-based file storage
- Centralized configuration
- Centralized logging
- Error handling
- Environment-based configuration

## Tech Stack

- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Migrate
- SQLite

## Project Structure

app/
config/
database/
logs/
storage/
templates/

## Current Version

v0.8.0

## Status

Active Development

## Developer Commands

| Command | Description |
|---------|-------------|
| ./scripts/dev.sh clean | Remove cache and temporary files |
| ./scripts/dev.sh check | Static verification |
| ./scripts/dev.sh verify | Full verification |
| ./scripts/dev.sh test | Run pytest |
| ./scripts/dev.sh lint | Static analysis |

## Latest Release

### v0.8.0 Stable

- Modular service architecture
- Unit & Integration Tests
- CI scripts
- Storage Service
- Logging Service
- File Service
- Authentication
- Repository cleanup

## Metadata Engine

- [x] Checksum
- [x] Image Metadata
- [x] PDF Metadata
- [x] Audio Metadata
- [ ] Video Metadata
- [ ] Thumbnail Engine
- [ ] Preview Engine
