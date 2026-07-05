# ExperimentsCloud

A lightweight, modular, self-hosted personal cloud storage platform built with Flask.

---

# Project Status

**Current Version**

v1.2.0-dev

Status:

Active Development

Current Sprint:

Documentation & Project Hygiene

---

# Features

## Authentication

- User Login
- User Logout
- Password Hashing
- Session Management

## Storage

- Secure Upload
- Download
- Delete
- Rename
- UUID-based Storage

## Folder Management

- Create Folder
- Rename Folder
- Delete Folder
- Nested Storage Structure

## Metadata Engine

- SHA256 Checksum
- Image Resolution
- PDF Page Count
- Audio Duration

Upcoming:

- Video Metadata
- Thumbnail Generation
- Preview Generation

---

# Architecture Overview

Current architecture follows a modular service-oriented design.

Core Components

- App Factory
- SQLAlchemy Models
- Service Layer
- Storage Layer
- Metadata Engine
- Authentication
- Validation Layer

---

# Tech Stack

- Python 3.14
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Migrate
- SQLite
- Pillow
- pypdf
- Mutagen

---

# Project Structure

```
app/
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

# Metadata Engine

Currently supported metadata:

- SHA256 Checksum
- Image Width
- Image Height
- PDF Page Count
- Audio Duration

Planned:

- Video Resolution
- Video Duration
- Thumbnail Generation
- Preview Generation

---

# Testing

Current Regression Status

```
140 / 140 PASSED
```

Testing includes

- Unit Tests
- Integration Tests
- Regression Tests

---

# Development Commands

| Command | Description |
|---------|-------------|
| ./scripts/dev.sh clean | Remove cache |
| ./scripts/dev.sh check | Project verification |
| ./scripts/dev.sh verify | Full verification |
| ./scripts/dev.sh test | Run test suite |
| ./scripts/dev.sh lint | Static analysis |

---

# Roadmap

Completed

- Authentication
- Storage
- Upload
- Folder Management
- Metadata Engine
  - Checksum
  - Image
  - PDF
  - Audio

In Progress

- Documentation & Project Hygiene

Planned

- Video Metadata
- Thumbnail Engine
- Preview Engine
- Sharing
- Search
- Recycle Bin

---

# Version

Current Version

v1.2.0-dev

Versioning follows milestone-based semantic versioning.

---

# License

This project is currently developed as a personal learning and experimentation project.
