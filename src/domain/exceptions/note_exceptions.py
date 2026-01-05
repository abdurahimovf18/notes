from src.shared.exceptions import ApplicationException, ValidationError


class NoteException(ApplicationException):
    pass


class NoteContentTooLongError(NoteException, ValidationError):
    pass


class NoteTitleTooLongError(NoteException, ValidationError):
    pass


class NoteTitleTooShortError(NoteException, ValidationError):
    pass
