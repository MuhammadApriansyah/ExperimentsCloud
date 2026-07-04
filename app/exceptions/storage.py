class StorageError(Exception):
    """Base storage exception."""
    pass


class StorageDirectoryError(StorageError):
    """Storage directory could not be created."""
    pass


class StorageFileError(StorageError):
    """Storage file operation failed."""
    pass
