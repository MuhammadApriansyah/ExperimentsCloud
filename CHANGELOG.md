# Changelog

Semua perubahan penting pada proyek ini akan didokumentasikan di sini.

## [v1.2.0-dev] - Sprint 1.8

### Added
- Audio metadata extraction using Mutagen.
- MetadataGenerator.audio_duration().
- Audio duration integration into FileMetadataService.
- Unit tests for audio metadata.
- Service tests for audio metadata.

### Improved
- Metadata pipeline now supports:
  - Checksum
  - Image metadata
  - PDF metadata
  - Audio duration

### Testing
- 140/140 tests passed.

---

## v0.3.3 (2026-07-04)

### Added

- Environment-aware configuration
- DevelopmentConfig
- TestingConfig
- ProductionConfig

### Changed

- App Factory now loads configuration dynamically.
- Storage configuration centralized.
- Upload validator uses application config.

### Removed

- Legacy storage constants.

---

## v0.3.2

### Added

- Centralized logging
- Error logging
- Custom error handlers

---

## v0.3.1

### Added

- Logging infrastructure

---

## v0.3

### Added

- Modular architecture
- Service layer

---

## v0.2

### Added

- Upload
- Download
- Delete

---

## v0.1

### Initial Release

- Authentication
- Database
- Flask Foundation
