# ExperimentsCloud Versioning

## Versioning Strategy

ExperimentsCloud uses **Milestone-Based Semantic Versioning**.

Version format:

MAJOR.MINOR.PATCH[-STAGE]

Example:

v1.2.0-dev

---

## Current Version

Current Version

v1.2.0-dev

Current Milestone

Metadata Engine

Current Sprint

Documentation & Project Hygiene

---

## Version Format

MAJOR

Breaking architectural changes.

MINOR

New milestone or major feature.

PATCH

Bug fixes, improvements, documentation, refactoring.

STAGE

Development stage.

Possible values:

- dev
- rc
- stable

Examples

v1.2.0-dev

Development milestone.

v1.2.0-rc

Release Candidate.

v1.2.0

Stable Release.

---

## Development Lifecycle

Planning

↓

Sprint

↓

Implementation

↓

Testing

↓

Regression

↓

Documentation

↓

Git Checkpoint

↓

Release Archive

↓

Next Sprint

---

## Release Types

Development

Internal development checkpoint.

Release Candidate

Feature complete.

Stable

Production-ready milestone.

---

## Version History

v0.x

Initial development.

v1.x

Structured sprint-based development.

---

## Upgrade Rules

MAJOR

Architecture changes.

MINOR

New subsystem completed.

PATCH

Bug fixes

Refactoring

Documentation

Tests

---

## Release Checklist

Before every checkpoint:

- README updated
- ROADMAP updated
- CHANGELOG updated
- ARCHITECTURE updated
- CONTRIBUTING updated
- VERSION updated
- Regression tests passed
- Git commit created
- Git push completed
- ZIP archive created
