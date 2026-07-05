# ExperimentsCloud Architecture

## System Overview

ExperimentsCloud is a modular personal cloud storage platform built with Flask.

The architecture follows a layered, service-oriented design where each layer has a single responsibility.

---

## High-Level Architecture

```
Client
   │
   ▼
Routes
   │
   ▼
Validation
   │
   ▼
Services
   │
   ▼
Models
   │
   ▼
Database

Services
   │
   ▼
Storage

Metadata Generator
   │
   ▼
File Metadata
```

---

## Directory Structure

```
app/
auth/
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

## Application Layers

### Presentation Layer

- Flask Routes
- Templates

### Validation Layer

- Validators
- Error Handling

### Service Layer

- FileService
- FolderService
- StorageService
- FileMetadataService
- MetadataGenerator
- LoggingService

### Data Layer

- SQLAlchemy Models
- SQLite

---

## Database Layer

Current Models

- User
- File
- Folder
- FileMetadata

Relationships

User

↓

Folder

↓

File

↓

FileMetadata

---

## Storage Layer

Responsibilities

- Upload
- Delete
- File Path Resolution
- User Storage Isolation

Implemented by

StorageService

---

## Metadata Engine

Supported

- SHA256 Checksum
- Image Resolution
- PDF Page Count
- Audio Duration

Planned

- Video Metadata
- Thumbnail Generation
- Preview Generation

---

## Request Lifecycle

Upload Request

↓

Validation

↓

StorageService

↓

Database

↓

Metadata Extraction

↓

Response

---

## Testing Strategy

Current Test Types

- Unit Tests
- Integration Tests
- Regression Tests

Regression is mandatory before every checkpoint.

---

## Design Principles

- Modular
- Layered Architecture
- Service-Oriented
- Single Responsibility
- Explicit Testing
- Incremental Development

---

## Future Architecture

Planned additions

- Sharing
- Search
- Thumbnail Engine
- Preview Engine
- REST API
- Synchronization
- Background Jobs
