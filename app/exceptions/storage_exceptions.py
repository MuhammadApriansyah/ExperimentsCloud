class StorageError(Exception):
    """Base exception for storage."""


class StorageFullError(StorageError):
    """Raised when storage capacity is exceeded."""


class StorageWriteError(StorageError):
    """Raised when writing file fails."""


class StorageReadError(StorageError):
    """Raised when reading file fails."""
