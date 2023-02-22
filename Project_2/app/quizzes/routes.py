from fastapi import APIRouter, Depends
from app.quizzes.controller import QuizController, QandAController
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
def get_players_challenges(player: str):
    return QuizController.get_players_challenges(player)


@quiz_router.get("/get-all-quizzes", response_model=list[QuizSchema])
def get_all_quizzes():
    return QuizController.get_all_quizzes()


@quiz_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_quiz_by_id(quiz_id: str):
    return QuizController.delete_quiz_by_id(quiz_id)


@quiz_router.put("/answer_challenge-request", response_model=QuizSchema)
def answer_challenge_request(
        quiz_id: str,
        player_decision: bool = None
):
    return QuizController.answer_challenge_request(quiz_id, player_decision)


@quiz_router.put("/record-times-by-quiz-id", response_model=QuizSchema)
def record_players_times(
        quiz_id: str,
        player1_time: NonNegativeInt = None,
        player2_time: NonNegativeInt = None
):
    return QuizController.record_players_times(quiz_id, player1_time, player2_time)


@quiz_router.put("/calculate-player-score", response_model=QuizSchema)
def calculate_player_score(
        quiz_id: str,
        player_username: str
):
    return QuizController.calculate_player_score(quiz_id, player_username)


@quiz_router.put("/declare-winner", response_model=QuizSchema)
def declare_winner(
        quiz_id: str
):
    return QuizController.declare_winner(quiz_id)


q_and_a_router = APIRouter(tags=["Q and A"], prefix="/api/q_and_a")


@q_and_a_router.post("/generate-question-for-quiz", response_model=QandASchema)
def generate_question_for_quiz(q_and_a: QandASchemaIn):
    return QandAController.generate_question_for_quiz(q_and_a.quiz_id)


@q_and_a_router.get("/id", response_model=QandASchema)
def get_q_and_a_by_id(q_and_a_id: str):
    return QandAController.get_q_and_a_by_id(q_and_a_id)


@q_and_a_router.get("/get-all-q-and-as-by-quiz-id", response_model=list[QandASchema])
def get_all_q_and_as_by_quiz_id(quiz_id: str):
    return QandAController.get_all_q_and_as_by_quiz_id(quiz_id)


@q_and_a_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_q_and_a_by_id(q_and_a_id: str):
    return QandAController.delete_q_and_a_by_id(q_and_a_id)


@q_and_a_router.put("/update-answers-by-q-and-a-id", response_model=QandASchema)
def players_answers(
            q_and_a_id: str,
            player1_answer: str = None,
            player2_answer: str = None
):
    return QandAController.players_answers(q_and_a_id, player1_answer, player2_answer)
