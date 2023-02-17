from fastapi import APIRouter, Depends
from app.quizzes.controller import QuizController
from app.users.controller.user_auth_controller import JWTBearer
from app.quizzes.schemas import *


quiz_router = APIRouter(tags=["Quiz"], prefix="/api/quizzes")


@quiz_router.post("/add-new-quiz", response_model=QuizSchema)
def create_quiz(quiz: QuizSchemaIn1):
    return QuizController.create_quiz(quiz.player1, quiz.player2)


@quiz_router.get("/id", response_model=QuizSchema)
def get_quiz_by_id(quiz_id: str):
    return QuizController.get_quiz_by_id(quiz_id)
