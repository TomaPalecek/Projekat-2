
from pydantic import NonNegativeInt
from sqlalchemy import func, and_, or_

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.quizzes.exceptions import *
from app.quizzes.models import Quiz



class QuizRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_quiz(self, player1, player2):
        try:

            quiz = Quiz(player1, player2)

            self.db.add(quiz)
            self.db.commit()
            self.db.refresh(quiz)
            return quiz
        except IntegrityError as e:
            raise e

    def get_quiz_by_id(self, quiz_id: str):
        quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()
        return quiz

    def get_players_challenges(self, player: str):
        quizzes = self.db.query(Quiz).where(and_(or_(Quiz.player1 == player, Quiz.player2 == player),
                                                 Quiz.status == "Pending")).all()

        return quizzes

    def get_all_quizzes(self):
        quiz = self.db.query(Quiz).all()
        return quiz

    def delete_quiz_by_id(self, quiz_id: str):
        try:
            quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()
            if quiz is None:
                raise QuizNotFoundException(f"Quiz with provided ID: {quiz_id} not found.", 400)
            self.db.delete(quiz)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def answer_challenge_request(
            self,
            quiz_id: str,
            player_decision: bool = None
    ):
        try:
            quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()

            if quiz is None:
                raise QuizNotFoundException(f"Quiz with provided ID: {quiz_id} not found.", 400)
            if player_decision is True:
                quiz.status = "Accepted"
            if player_decision is False:
                quiz.status = "Declined"
                quiz.winner = quiz.player1

            self.db.add(quiz)
            self.db.commit()
            self.db.refresh(quiz)
            return quiz
        except Exception as e:
            raise e

    def record_players_times(
            self, 
            quiz_id: str,
            player1_time: NonNegativeInt = None, 
            player2_time: NonNegativeInt = None
    ):
        try:
            quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()
            
            if quiz is None:
                raise QuizNotFoundException(f"Quiz with provided ID: {quiz_id} not found.", 400)
            if player1_time is not None:
                quiz.player1_time = player1_time
            if player2_time is not None:
                quiz.player2_time = player2_time
                
            self.db.add(quiz)
            self.db.commit()
            self.db.refresh(quiz)
            return quiz
        except Exception as e:
            raise e
