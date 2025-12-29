from src.core.base.exceptions import InternalError


class ContainerException(InternalError):
    pass


class InterfaceNotRegisteredError(ContainerException):
    """
    Raised on attempt to access unregistered Interface.
    """
    pass


class InterfaceAlreadyRegisteredError(ContainerException):
    """
    Raised on attempt to register the realization of the same interface twice.
    """
    pass
