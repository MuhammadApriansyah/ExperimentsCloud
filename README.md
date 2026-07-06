# ExperimentsCloud

ExperimentsCloud adalah personal cloud server yang dibangun menggunakan Flask dengan fokus pada:

- File Management
- Folder Management
- Metadata Extraction
- Storage Management
- Modular Service Architecture

---

## Primary Development Environment

Mulai Sprint 2.0, environment utama pengembangan adalah:

- AlmaLinux 10.2
- Python 3.12
- Git (SSH)
- SQLite
- FFmpeg
- FFprobe

Termux tetap didukung sebagai compatibility environment.

---

## External Dependencies

ExperimentsCloud menggunakan Binary Discovery Framework.

Dependency eksternal:

- ffprobe
- ffmpeg

Binary akan dicari dengan urutan:

1. Flask Config
2. Environment Variable
3. System PATH

---

## Verify Environment

```bash
./scripts/check_system.sh
```

---

## Run Tests

```bash
pytest -v
```

Current regression status:

```
142 passed
```

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
