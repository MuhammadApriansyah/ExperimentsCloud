# ExperimentsCloud Architecture

# Binary Discovery Framework

ExperimentsCloud tidak menggunakan hardcoded executable path.

Semua executable dicari melalui Binary Discovery Framework.

Priority:

1. Flask Config

2. Environment Variable

3. PATH

4. BinaryNotFoundError

Framework ini memastikan project dapat berjalan pada:

- AlmaLinux
- Termux
- Ubuntu
- Debian
- Fedora
- Docker
- CI/CD

tanpa perubahan source code.

# External Dependencies

Core binaries

- ffprobe
- ffmpeg

Future

- ImageMagick
- LibreOffice
- Tesseract
- ExifTool
- Ghostscript
- Pandoc

## Core Philosophy

- Modular
- Service-Oriented
- Test-Driven
- Maintainable
- Progressive Development

---

# High-Level Architecture

```
Client

↓

Flask

↓

Routes

↓

Services

↓

Models

↓

Database
```

---

# Metadata Pipeline

```
Upload

↓

StorageService

↓

FileMetadataService

├── MetadataGenerator
│      ├── SHA256
│      ├── Image
│      ├── PDF
│      └── Audio
│
└── VideoMetadataService
       ↓
    FFprobe

↓

FileMetadata

↓

Database
```

---

# Service Responsibilities

StorageService

- File storage
- Directory management

MetadataGenerator

- SHA256
- Image metadata
- PDF metadata
- Audio metadata

VideoMetadataService

- FFprobe wrapper
- Video parser
- Metadata normalization

FileMetadataService

- Metadata orchestration
- Database persistence

---

# Design Principles

- Single Responsibility Principle
- Separation of Concerns
- Composition over Complexity
- Small Testable Components
