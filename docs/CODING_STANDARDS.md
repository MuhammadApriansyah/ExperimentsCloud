# ExperimentsCloud Coding Standards

## Architecture

Route
↓
Service
↓
Storage / Repository
↓
Model

Routes never contain business logic.

Services never contain HTML.

Templates never access the database.

Validators never modify data.

StorageService is the only module allowed to access file storage paths.

---

## Naming

Classes

PascalCase

Functions

snake_case

Constants

UPPER_CASE

Files

snake_case.py

---

## Imports

Standard Library

↓

Third Party

↓

Project Imports

---

## Git

Every milestone:

Verification

↓

Commit

↓

Tag

↓

ZIP Snapshot
