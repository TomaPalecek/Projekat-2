class AdminNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class AdminTypeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class AdminTypeExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotSuperUser(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class PlayerNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class PlayerExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
