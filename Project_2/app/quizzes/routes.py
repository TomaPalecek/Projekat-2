from fastapi import APIRouter, Depends
from app.quizzes.controller import QuizController
from app.users.controller.user_auth_controller import JWTBearer
from app.quizzes.schemas import *

quiz_router = APIRouter(tags=["Quiz"], prefix="/api/quizzes")


@quiz_router.post("/add-new-quiz", response_model=QuizSchema)
def create_quiz(quiz: QuizSchemaIn):
    return QuizController.create_quiz(quiz.player1, quiz.player2)


@quiz_router.get("/id", response_model=QuizSchema)
def get_quiz_by_id(quiz_id: str):
    return QuizController.get_quiz_by_id(quiz_id)


@quiz_router.get("/get-players-challenges", response_model=list[QuizSchema])
def get_players_challenges(players: str):
    return QuizController.get_players_challenges(players)


@quiz_router.get("/get-all-quizzes", response_model=list[QuizSchema])
def get_all_quizzes():
    return QuizController.get_all_quizzes()


@quiz_router.delete("/")
def delete_quiz_by_id(quiz_id: str):
    return QuizController.delete_quiz_by_id(quiz_id)


@quiz_router.put("/update_challenge-request", response_model=QuizSchema)
def answer_challenge_request(
        quiz_id: str,
        player_decision: bool = None
):
    return QuizController.answer_challenge_request(quiz_id, player_decision)


@quiz_router.put("/update_answers-by-quiz-id", response_model=QuizSchema)
def player_answers(
        quiz_id: str,
        player1_answers: str = None,
        player2_answers: str = None,
        player1_time: NonNegativeInt = None,
        player2_time: NonNegativeInt = None
):
    return QuizController.player_answers(quiz_id, player1_answers, player2_answers,
                                         player1_time, player2_time)
