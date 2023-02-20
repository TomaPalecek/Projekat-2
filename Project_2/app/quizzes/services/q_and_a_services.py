from app.db.database import SessionLocal
from app.quizzes.repository.q_and_a_repository import QandARepository


class QandAServices:

    @staticmethod
    def generate_question_for_quiz(quiz_id):
        try:
            with SessionLocal() as db:
                q_and_a_repository = QandARepository(db)
                return q_and_a_repository.generate_question_for_quiz(quiz_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_q_and_a_by_id(q_and_a_id: str):
        try:
            with SessionLocal() as db:
                q_and_a_repository = QandARepository(db)
                return q_and_a_repository.get_q_and_a_by_id(q_and_a_id)
        except Exception as e:
            raise e
        
    @staticmethod
    def get_all_q_and_as_by_quiz_id(quiz_id: str):
        try:
            with SessionLocal() as db:
                q_and_a_repository = QandARepository(db)
                return q_and_a_repository.get_all_q_and_as_by_quiz_id(quiz_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_q_and_a_by_id(q_and_a_id: str):
        try:
            with SessionLocal() as db:
                q_and_a_repository = QandARepository(db)
                q_and_a_repository.delete_q_and_a_by_id(q_and_a_id)
                return True
        except Exception as e:
            raise e
