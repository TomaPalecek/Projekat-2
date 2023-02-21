
from pydantic import NonNegativeInt
from sqlalchemy import and_

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.quizzes.exceptions import *
from app.quizzes.models import Quiz

from app.questions.services import QuestionServices
from app.users.exceptions import *


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
        quizzes = self.db.query(Quiz).where(and_(Quiz.player2 == player, Quiz.status == "Pending")).all()

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

    def calculate_player_score(
            self,
            quiz_id: str,
            player_username: str,
            q_and_as: list
    ):
        try:
            quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()
            if quiz is None:
                raise QuizNotFoundException(f"Quiz with provided ID: {quiz_id} not found.", 400)

            score = 0
            if quiz.player1 == player_username:
                for q in q_and_as:
                    question = QuestionServices.get_question_by_id(q.question_id)
                    if q.player1_answer == question.correct_answer:
                        score += 1
                quiz.player1_score = score

            elif quiz.player2 == player_username:
                for q in q_and_as:
                    question = QuestionServices.get_question_by_id(q.question_id)
                    if q.player2_answer == question.correct_answer:
                        score += 1
                quiz.player2_score = score
            else:
                raise PlayerNotFoundException(f"Player with provided username {player_username} does not exist.", 400)

            self.db.add(quiz)
            self.db.commit()
            self.db.refresh(quiz)
            return quiz

        except Exception as e:
            raise e

    def declare_winner(
            self,
            quiz_id: str,
            q_and_as: list
    ):
        try:
            quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()
            if quiz is None:
                raise QuizNotFoundException(f"Quiz with provided ID: {quiz_id} not found.", 400)

            if len(q_and_as) != 10:
                raise QuizHasntTenQuestionsException(f"Quiz with provided id {quiz_id} is doesn't have 10 questions."
                                                     , 400)

            for q in q_and_as:
                if q.player1_answer == "" or q.player2_answer == "":
                    raise QuizNotFinishedException(f"Quiz with provided id {quiz_id} is not finished.", 400)

            self.calculate_player_score(quiz_id, quiz.player1, q_and_as)
            self.calculate_player_score(quiz_id, quiz.player2, q_and_as)

            if quiz.player1_score > quiz.player2_score:
                quiz.winner = quiz.player1

            elif quiz.player1_score < quiz.player2_score:
                quiz.winner = quiz.player2

            elif quiz.player1_score == quiz.player2_score:

                if quiz.player1_time > quiz.player2_time:
                    quiz.winner = quiz.player1

                elif quiz.player1_time < quiz.player2_time:
                    quiz.winner = quiz.player2

                else:
                    quiz.winner = "Draw"

            self.db.add(quiz)
            self.db.commit()
            self.db.refresh(quiz)
            return quiz

        except Exception as e:
            raise e
