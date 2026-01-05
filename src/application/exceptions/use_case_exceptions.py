from src.shared.exceptions.application_exception import ApplicationException
from src.shared.exceptions.forbidden_error import ForbiddenError


class UseCaseException(ApplicationException):
    pass


class AggregateVersionMismatchError(UseCaseException, ForbiddenError):
    pass
