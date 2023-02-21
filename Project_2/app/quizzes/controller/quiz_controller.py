from fastapi import HTTPException, Response
from pydantic import NonNegativeInt

from app.quizzes.exceptions import *
from app.users.exceptions import *
from app.quizzes.services import QuizServices, QandAServices
from app.users.services import PlayerServices


class QuizController:
    @staticmethod
    def create_quiz(player1, player2):
        try:
            PlayerServices.get_player_by_id(player1)
            PlayerServices.get_player_by_id(player2)
            quiz = QuizServices.create_quiz(player1, player2)
            return quiz
        except PlayerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_quiz_by_id(quiz_id: str):
        quiz = QuizServices.get_quiz_by_id(quiz_id)
        if quiz:
            return quiz
        raise HTTPException(
            status_code=400,
            detail=f"Quiz with provided id {quiz_id} does not exist",
        )

    @staticmethod
    def get_players_challenges(player: str):
        quiz = QuizServices.get_players_challenges(player)
        return quiz

    @staticmethod
    def get_all_quizzes():
        quiz = QuizServices.get_all_quizzes()
        return quiz

    @staticmethod
    def delete_quiz_by_id(quiz_id: str):
        try:
            QuizServices.delete_quiz_by_id(quiz_id)
            return Response(content=f"Quiz with id - {quiz_id} is deleted")
        except QuizNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def answer_challenge_request(
            quiz_id: str,
            player_decision: bool = None
    ):
        try:
            quiz = QuizServices.answer_challenge_request(quiz_id, player_decision)
            return quiz
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def record_players_times(
            quiz_id: str,
            player1_time: NonNegativeInt = None,
            player2_time: NonNegativeInt = None
    ):
        try:
            quiz = QuizServices.record_players_times(quiz_id, player1_time, player2_time)
            return quiz
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def calculate_player_score(
            quiz_id: str,
            player_username: str
    ):
        try:
            q_and_as = QandAServices.get_all_q_and_as_by_quiz_id(quiz_id)
            quiz = QuizServices.calculate_player_score(quiz_id, player_username, q_and_as)
            return quiz
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def declare_winner(
            quiz_id: str
    ):
        try:
            q_and_as = QandAServices.get_all_q_and_as_by_quiz_id(quiz_id)
            quiz = QuizServices.declare_winner(quiz_id, q_and_as)
            return quiz
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
