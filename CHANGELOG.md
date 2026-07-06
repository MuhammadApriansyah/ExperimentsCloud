# Changelog

All notable changes to this project will be documented here.

# Sprint 2.0

## Added

- Binary Discovery Framework
- Auto-discovery external binaries
- Configurable binary path support
- System dependency verification script
- SYSTEM_DEPENDENCIES documentation

## Changed

- Primary development environment migrated to AlmaLinux 10.2
- Git workflow migrated to SSH
- Video metadata now uses configurable ffprobe discovery
- Video test generation now uses configurable ffmpeg discovery

## Fixed

- Testing configuration override
- Binary lookup portability
- Cross-platform FFmpeg detection

## Verification

- Full regression passed (142/142)
- FFmpeg verified
- FFprobe verified

---

## [v1.2.0-dev] — Sprint 1.9

Release Date:
2026-07-06

### Added

- VideoMetadataService
- FFprobe integration
- Video metadata parser
- Video metadata integration into FileMetadataService
- Video metadata unit tests
- FileMetadataService integration tests

### Metadata Engine

Added support for:

- SHA-256 Checksum
- Image Metadata
- PDF Metadata
- Audio Metadata
- Video Metadata

### Improved

- Cleaner metadata architecture
- Dedicated VideoMetadataService
- Normalized metadata parsing
- Better separation of internal generators and external adapters

### Testing

- 142 / 142 tests passed
- Full regression passed

---

## [v1.2.0-dev] — Sprint 1.8

### Added

- Audio metadata extraction using Mutagen
- Audio duration support
- Audio metadata tests

### Improved

- Metadata pipeline supports:
  - Checksum
  - Image
  - PDF
  - Audio

### Testing

- 140 / 140 tests passed

---

## v0.3.3

- Environment-aware configuration
- DevelopmentConfig
- TestingConfig
- ProductionConfig

---

## v0.3.2

- Centralized logging
- Error logging
- Custom error handlers

---

## v0.3.1

- Logging infrastructure

---

## v0.3

- Modular architecture
- Service layer

---

## v0.2

- Upload
- Download
- Delete

---

## v0.1

- Initial release
- Authentication
- Database
- Flask foundation
