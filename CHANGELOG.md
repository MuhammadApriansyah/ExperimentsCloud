# Changelog

Semua perubahan penting pada proyek **ExperimentsCloud** didokumentasikan dalam berkas ini.

Proyek ini mengikuti **milestone-based semantic versioning**.

- **v0.x** → Foundation & Initial Development
- **v1.x** → Structured Sprint Development

---

# Development Releases

## [v1.2.0-dev] - Sprint 1.8
### Objective
Audio Metadata Foundation

### Added

- Audio metadata extraction using **Mutagen**.
- `MetadataGenerator.audio_duration()`.
- Audio duration integration into `FileMetadataService`.
- Unit tests for audio metadata.
- Service tests for audio metadata.

### Improved

Metadata Engine now supports:

- SHA256 Checksum
- Image Resolution
- PDF Page Count
- Audio Duration

### Testing

- MetadataGenerator tests: **10/10 PASSED**
- FileMetadataService tests: **5/5 PASSED**
- Full Regression Suite: **140/140 PASSED**

### Status

✅ Completed

---

## [v1.1.0-dev] - Sprint 1.7

### Objective

PDF Metadata Foundation

### Added

- PDF page count extraction using **pypdf**.
- `MetadataGenerator.pdf_page_count()`.
- PDF metadata integration into `FileMetadataService`.
- Unit tests for PDF metadata.
- Service tests for PDF metadata.

### Improved

Metadata Engine now supports:

- SHA256 Checksum
- Image Resolution
- PDF Page Count

### Testing

- Full Regression Suite: **137/137 PASSED**

### Status

✅ Completed

---

## [v1.0.0-dev] - Sprint 1.6

### Objective

Image Metadata Foundation

### Added

- Image dimension extraction using **Pillow**.
- `MetadataGenerator.image_size()`.
- Image metadata integration into `FileMetadataService`.

### Improved

Metadata Engine now supports:

- SHA256 Checksum
- Image Resolution

### Testing

- Full Regression Suite: **134/134 PASSED**

### Status

✅ Completed

---

# Legacy Releases (v0.x)

## v0.3.3 (2026-07-04)

### Added

- Environment-aware configuration
- `DevelopmentConfig`
- `TestingConfig`
- `ProductionConfig`

### Changed

- App Factory now loads configuration dynamically.
- Storage configuration centralized.
- Upload validator now uses application configuration.

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

- Secure upload
- File download
- File deletion

---

## v0.1

### Initial Release

- Flask foundation
- Authentication
- Database integration
