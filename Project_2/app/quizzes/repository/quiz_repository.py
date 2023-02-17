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
        if quiz is None:
            raise QuizNotFoundException(f"Quiz with provided ID: {quiz_id} not found.", 400)
        return quiz

"""
    def player1_results(self, player1, player1_answers, player1_time):
        try:
            quiz = Quiz(player1, player1_answers, player1_time)
            self.db.add(quiz)
            self.db.commit()
            self.db.refresh(quiz)
            return quiz
        except IntegrityError as e:
            raise e
"""