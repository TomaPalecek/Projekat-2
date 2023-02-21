from pydantic import NonNegativeInt

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
    def get_players_challenges(player: str):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.get_players_challenges(player)
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

    @staticmethod
    def answer_challenge_request(
            quiz_id: str,
            player_decision: bool = None
    ):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.answer_challenge_request(quiz_id, player_decision)
        except Exception as e:
            raise e

    @staticmethod
    def record_players_times(
            quiz_id: str,
            player1_time: NonNegativeInt = None,
            player2_time: NonNegativeInt = None
    ):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.record_players_times(quiz_id, player1_time, player2_time)
        except Exception as e:
            raise e

    @staticmethod
    def calculate_player_score(
            quiz_id: str,
            player_username: str,
            q_and_as: list
    ):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.calculate_player_score(quiz_id, player_username, q_and_as)
        except Exception as e:
            raise e

    @staticmethod
    def declare_winner(
            quiz_id: str,
            q_and_as: list
    ):
        try:
            with SessionLocal() as db:
                quiz_repository = QuizRepository(db)
                return quiz_repository.declare_winner(quiz_id, q_and_as)
        except Exception as e:
            raise e
