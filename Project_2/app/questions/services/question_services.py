from app.db.database import SessionLocal
from app.questions.repository.question_repository import QuestionRepository


class QuestionServices:
    @staticmethod
    def create_question(text, answer_a, answer_b, answer_c, answer_d, correct_answer, category_id):
        try:
            with SessionLocal() as db:
                question_repository = QuestionRepository(db)
                return question_repository.create_question(text, answer_a, answer_b, answer_c, answer_d, correct_answer,
                                                           category_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_question_by_id(question_id: str):
        try:
            with SessionLocal() as db:
                question_repository = QuestionRepository(db)
                return question_repository.get_question_by_id(question_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_questions_by_category_id(category_id: str):
        try:
            with SessionLocal() as db:
                question_repository = QuestionRepository(db)
                return question_repository.get_questions_by_category_id(category_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_questions():
        try:
            with SessionLocal() as db:
                question_repository = QuestionRepository(db)
                return question_repository.get_all_questions()
        except Exception as e:
            raise e

    @staticmethod
    def delete_question_by_id(question_id: str):
        try:
            with SessionLocal() as db:
                question_repository = QuestionRepository(db)
                question_repository.delete_question_by_id(question_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_question(
            question_id: str,
            text: str = None,
            answer_a: str = None,
            answer_b: str = None,
            answer_c: str = None,
            answer_d: str = None,
            correct_answer: str = None,
            category_id: str = None
    ):
        try:
            with SessionLocal() as db:
                question_repository = QuestionRepository(db)
                return question_repository.update_question(question_id, text, answer_a, answer_b, answer_c, answer_d,
                                                           correct_answer, category_id)
        except Exception as e:
            raise e
