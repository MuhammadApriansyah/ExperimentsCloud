# ExperimentsCloud Architecture

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
