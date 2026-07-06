# Contributing to ExperimentsCloud

## Purpose

This document defines the development standards and workflow used throughout the ExperimentsCloud project.

Even when developed by a single developer, these rules ensure consistency, maintainability, and long-term scalability.

---

# Development Environment

Primary environment

- AlmaLinux 10.2

Supported

- Termux

---

## Before Commit

Always execute

```bash
./scripts/check_system.sh
```

```bash
pytest -v
```

Both commands must pass before creating a commit.

---

## Sprint Workflow

Every sprint follows:

1. Development
2. Compile Check
3. Unit Test
4. Integration Test
5. Full Regression
6. Documentation Update
7. Git Audit
8. Commit
9. Push
10. Remote Verification
11. Start Next Sprint

Skipping checkpoint is discouraged.

# Development Workflow

Every feature follows the same lifecycle.

Planning

↓

Implementation

↓

Compile

↓

Unit Tests

↓

Integration Tests

↓

Regression Tests

↓

Documentation Update

↓

Gate Review

↓

Git Checkpoint

↓

Release Archive

---

# Coding Standards

General principles

- Follow PEP 8.
- Keep functions focused on a single responsibility.
- Prefer explicit code over implicit behavior.
- Avoid duplicated logic.
- Keep services independent from presentation.

Naming

Classes

PascalCase

Functions

snake_case

Constants

UPPER_CASE

---

# Project Structure

Business logic belongs inside the Service Layer.

Database access belongs to Models.

HTTP handling belongs to Routes.

Validation belongs to Validators.

Metadata extraction belongs to MetadataGenerator.

---

# Testing Policy

Every new feature must include tests.

Required:

- Unit Tests
- Service Tests (if applicable)
- Integration Tests (when applicable)

Regression testing is mandatory before every checkpoint.

---

# Documentation Policy

Every completed sprint must synchronize:

- README.md
- ROADMAP.md
- CHANGELOG.md
- VERSION.md
- ARCHITECTURE.md
- CONTRIBUTING.md

Documentation is part of the Definition of Done.

---

# Git Workflow

Recommended sequence

git status

↓

git add

↓

git commit

↓

git push

↓

ZIP Checkpoint

---

# Pull Request Checklist

Before merging:

- Code compiles
- Tests pass
- Regression passes
- Documentation updated
- Version verified

---

# Definition of Done

A sprint is complete only if:

- Feature implemented
- Compile successful
- Unit Tests passed
- Integration Tests passed
- Regression Tests passed
- Documentation synchronized
- Gate Review approved
- Git Checkpoint created
- Release Archive created

---

# Development Principles

ExperimentsCloud follows these principles:

- Modular Architecture
- Service-Oriented Design
- Single Responsibility Principle
- Incremental Development
- Regression First
- Documentation First
- Long-Term Maintainability
