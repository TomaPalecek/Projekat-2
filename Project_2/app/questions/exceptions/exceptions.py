class CategoryNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CategoryExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class QuestionNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code