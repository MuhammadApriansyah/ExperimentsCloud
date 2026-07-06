# ADR-0004: Storage Backend Abstraction

## Status

Accepted

## Date

2026-07-07

## Authors

ExperimentsCloud Project

## Context

ExperimentsCloud originally relied directly on the local filesystem.

This tightly coupled upload, download, metadata generation, and file management to a single storage implementation, making future cloud storage integration difficult.

To support Local Storage, Amazon S3, MinIO, and future object storage providers, a storage abstraction layer became necessary.

## Decision Drivers

- Support multiple storage providers
- Decouple services from filesystem implementation
- Improve maintainability
- Improve testability
- Enable future cloud-native storage backends

## Decision

Introduce a `StorageBackend` interface.

Concrete implementations include:

- LocalStorage
- S3Storage
- MinIOStorage

Each backend exposes a common interface:

- `save()`
- `open()`
- `exists()`
- `delete()`
- `file_path()`

A storage manager selects the active backend based on application configuration.

## Consequences

### Positive

- Storage backend becomes configurable.
- Local and cloud storage share a common interface.
- Services no longer depend on implementation details.
- New providers can be added with minimal application changes.
- Unit testing becomes easier.

### Negative

- Slight increase in abstraction.
- Additional interface maintenance.

## Alternatives Considered

### Continue using filesystem directly

Rejected because it prevents storage portability.

### Conditional logic inside services

Rejected because it increases coupling and violates separation of concerns.

## Future Work

- Evaluate replacing `file_path()` with a storage-neutral object key abstraction.
- Implement production-ready MinIO backend.
- Implement multipart uploads for S3.
