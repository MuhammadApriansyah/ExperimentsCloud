class AuthenticationError(Exception):
    """Authentication failed."""
    pass


class AuthorizationError(Exception):
    """User is not authorized."""
    pass
