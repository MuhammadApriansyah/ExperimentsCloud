# ExperimentsCloud

ExperimentsCloud is a lightweight, modular, self-hosted personal cloud storage platform built with Flask.

The project focuses on clean architecture, maintainability, automated testing, and progressive feature development.

---

# Current Version

v1.2.0-dev

Status:
Active Development

Latest Stable Checkpoint:
Sprint 1.9

---

# Features

## Authentication

- User Login
- User Logout
- Password Hashing
- Session Management

## File Management

- Upload
- Download
- Delete
- Folder Management

## Metadata Engine

Supported metadata extraction:

- SHA-256 Checksum
- Image Width & Height
- PDF Page Count
- Audio Duration
- Video
  - Duration
  - Resolution
  - FPS
  - Codec
  - Bitrate

## Storage

- UUID-based Storage
- Organized User Directories
- Storage Service Layer

## Configuration

- Development
- Testing
- Production

## Logging

- Centralized Logging
- Error Logging
- Custom Error Handlers

---

# Tech Stack

- Python 3.14
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Migrate
- Pillow
- PyPDF
- Mutagen
- FFprobe (FFmpeg)

---

# Project Structure

```
app/
config/
database/
docs/
logs/
migrations/
scripts/
storage/
templates/
tests/
```

---

# Architecture

```
Upload
    │
    ▼
StorageService
    │
    ▼
FileMetadataService
    │
    ├── MetadataGenerator
    │      ├── SHA256
    │      ├── Image
    │      ├── PDF
    │      └── Audio
    │
    └── VideoMetadataService
            └── FFprobe
    │
    ▼
Database
```

---

# Testing

Current Test Suite

```
142 Tests

142 Passed

0 Failed

0 Skipped
```

Regression Status

PASS

---

# Developer Commands

| Command | Description |
|----------|-------------|
| ./scripts/dev.sh clean | Clean cache |
| ./scripts/dev.sh check | Project verification |
| ./scripts/dev.sh verify | Full verification |
| ./scripts/dev.sh test | Run pytest |
| ./scripts/dev.sh lint | Static analysis |

---

# Roadmap Highlights

Completed

- Authentication
- File Storage
- Folder Management
- Metadata Engine
  - Image
  - PDF
  - Audio
  - Video

Next

- Thumbnail Engine
- Preview Engine
- Video Thumbnail Generation
- Search Engine
- Sharing System

---

# License

Private Project
