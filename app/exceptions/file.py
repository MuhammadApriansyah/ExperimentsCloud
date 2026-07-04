class FileError(Exception):
    """Base exception for file operations."""
    pass


class FileNotFound(FileError):
    """Requested file was not found."""
    pass


class InvalidFileExtension(FileError):
    """File extension is not allowed."""
    pass


class FileTooLarge(FileError):
    """Uploaded file exceeds maximum size."""
    pass
