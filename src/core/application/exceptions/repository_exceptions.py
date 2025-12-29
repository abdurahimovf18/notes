from src.core.base.exceptions import (
    ApplicationException,
    ConflictError,
    ForbiddenError,
    NotFoundError,
)


class RepositoryException(ApplicationException):
    pass


class AggregateNotFoundError(NotFoundError):
    """
    Raised on attempt to update or delete aggregate that does not exist.
    """
    pass


class AggregateAlreadyExistsError(ConflictError):
    """
    Raised on attempt to create a new aggregate with unique credentials that
    already exists.
    """
    pass


class VersionMismatchError(ForbiddenError):
    """
    Raised on attempt to update an aggregate, but its version is old.
    """
    pass
