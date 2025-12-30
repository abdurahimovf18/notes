from src.shared.exceptions import (
    ApplicationException,
    ConflictError,
    ForbiddenError,
    NotFoundError,
)


class RepositoryException(ApplicationException):
    pass


class AggregateNotFoundError(NotFoundError, RepositoryException):
    """
    Raised on attempt to update or delete aggregate that does not exist.
    """
    pass


class AggregateAlreadyExistsError(ConflictError, RepositoryException):
    """
    Raised on attempt to create a new aggregate with unique credentials that
    already exists.
    """
    pass


class VersionMismatchError(ForbiddenError, RepositoryException):
    """
    Raised on attempt to update an aggregate, but its version is old.
    """
    pass
