class QuizNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class QandANotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class QuizHasTenQuestionsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class QuizHasntTenQuestionsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class NoMoreQuestionsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class QuizNotFinishedException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
