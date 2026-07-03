class FileError(Exception):
    """Base exception for file module."""


class FileAlreadyExistsError(FileError):
    """Raised when a file already exists."""


class InvalidFileExtensionError(FileError):
    """Raised when file extension is not allowed."""


class FileTooLargeError(FileError):
    """Raised when uploaded file exceeds maximum size."""
