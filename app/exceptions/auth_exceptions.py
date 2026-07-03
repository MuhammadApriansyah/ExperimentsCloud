class AuthenticationError(Exception):
    """Base authentication exception."""


class InvalidCredentialError(AuthenticationError):
    """Raised when credential is invalid."""


class UserLockedError(AuthenticationError):
    """Raised when user account is locked."""
