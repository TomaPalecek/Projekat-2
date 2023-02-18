from app.db.database import SessionLocal
from app.quizzes.repository.quiz_repository import QuizRepository


class QuizServices:
    @staticmethod
    def create_quiz(player1, player2):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.create_quiz(player1, player2)
        except Exception as e:
            raise e

    @staticmethod
    def get_quiz_by_id(quiz_id: str):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.get_quiz_by_id(quiz_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_quizzes():
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.get_all_quizzes()
        except Exception as e:
            raise e

    @staticmethod
    def delete_quiz_by_id(quiz_id: str):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                quiz_repository.delete_quiz_by_id(quiz_id)
                return True
        except Exception as e:
            raise e