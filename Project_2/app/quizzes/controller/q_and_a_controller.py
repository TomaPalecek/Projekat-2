from fastapi import HTTPException, status, Response

from app.quizzes.exceptions import *
from app.quizzes.services import QandAServices, QuizServices


class QandAController:

    @staticmethod
    def generate_question_for_quiz(quiz_id):
        try:
            QuizServices.get_quiz_by_id(quiz_id)
            q_and_a = QandAServices.generate_question_for_quiz(quiz_id)
            return q_and_a
        except QuizNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_q_and_a_by_id(q_and_a_id: str):
        try:
            q_and_a = QandAServices.get_q_and_a_by_id(q_and_a_id)
            if q_and_a:
                return q_and_a
        except QandANotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def get_all_q_and_as_by_quiz_id(quiz_id: str):
        q_and_as = QandAServices.get_all_q_and_as_by_quiz_id(quiz_id)
        if q_and_as:
            return q_and_as
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Q and As with provided quiz id {quiz_id} does not exist")

    @staticmethod
    def delete_q_and_a_by_id(q_and_a_id: str):
        try:
            QandAServices.delete_q_and_a_by_id(q_and_a_id)
            return Response(content=f"Q and A with id - {q_and_a_id} is deleted")
        except QandANotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def players_answers(
            q_and_a_id: str,
            player1_answer: str = None,
            player2_answer: str = None
    ):
        try:
            q_and_a = QandAServices.players_answers(q_and_a_id, player1_answer, player2_answer)
            return q_and_a
        except QandANotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
