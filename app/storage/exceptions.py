class StorageError(Exception):
    """Base storage exception."""


class StorageFileNotFound(StorageError):
    """Requested file does not exist."""


class StorageConfigurationError(StorageError):
    """Storage backend configuration is invalid."""
