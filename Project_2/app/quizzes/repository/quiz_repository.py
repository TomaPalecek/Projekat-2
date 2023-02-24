from pydantic import NonNegativeInt
from sqlalchemy import and_

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.quizzes.exceptions import *
from app.quizzes.models import Quiz

from app.questions.services import QuestionServices
from app.users.exceptions import *
from app.users.services import PlayerServices, UserServices
from app.users.services.email_services import EmailServices


class QuizRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_quiz(self, player1, player2):
        try:
            if player2 == player1:
                raise SelfChallengeException("Cannot challenge yourself!", 400)

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
            raise QuizNotFoundException(f"quiz with id {quiz_id} doesn't exist!", 400)
        return quiz

    def get_players_challenges(self, player: str):
        quizzes = self.db.query(Quiz).where(and_(Quiz.player2 == player, Quiz.status == "Pending")).all()
        if quizzes is None:
            quizzes = ["No challenges"]

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
                quiz.winner = "Not Played"

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
                raise PlayerNotInQuizException(f"Player with provided username {player_username} is not in quiz.", 400)

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
                raise QuizHasntTenQuestionsException(f"Quiz with provided id {quiz_id} doesn't have 10 questions.", 500)

            for q in q_and_as:
                if q.player1_answer == "" or q.player2_answer == "":
                    raise QuizNotFinishedException(f"Quiz with provided id {quiz_id} is not finished.", 400)

            self.calculate_player_score(quiz_id, quiz.player1, q_and_as)
            self.calculate_player_score(quiz_id, quiz.player2, q_and_as)

            player_updater1 = PlayerServices.get_player_by_username(quiz.player1)
            player_updater2 = PlayerServices.get_player_by_username(quiz.player2)
            player1_user = UserServices.get_user_by_id(player_updater1.user_id)
            player2_user = UserServices.get_user_by_id(player_updater2.user_id)

            player_updater1.played_quizzes += 1
            player_updater2.played_quizzes += 1
            player_updater1.questions_taken += 10
            player_updater2.questions_taken += 10
            player_updater1.correct_answers += quiz.player1_score
            player_updater2.correct_answers += quiz.player2_score
            player_updater1.incorrect_answers += (10 - quiz.player1_score)
            player_updater2.incorrect_answers += (10 - quiz.player2_score)

            PlayerServices.update_player(player_updater1.id, played_quizzes=player_updater1.played_quizzes,
                                         questions_taken=player_updater1.questions_taken,
                                         correct_answers=player_updater1.correct_answers,
                                         incorrect_answers=player_updater1.incorrect_answers)
            PlayerServices.update_player(player_updater2.id, played_quizzes=player_updater2.played_quizzes,
                                         questions_taken=player_updater2.questions_taken,
                                         correct_answers=player_updater2.correct_answers,
                                         incorrect_answers=player_updater2.incorrect_answers)

            if quiz.player1_score > quiz.player2_score:
                quiz.winner = quiz.player1
                print("HEREEE")
                EmailServices.send_email_win(player1_user.email)
                EmailServices.send_email_lose(player2_user.email)

            elif quiz.player1_score < quiz.player2_score:
                quiz.winner = quiz.player2
                EmailServices.send_email_win(player2_user.email)
                EmailServices.send_email_lose(player1_user.email)

            elif quiz.player1_score == quiz.player2_score:

                if quiz.player1_time > quiz.player2_time:
                    quiz.winner = quiz.player1
                    EmailServices.send_email_win(player1_user.email)
                    EmailServices.send_email_lose(player2_user.email)

                elif quiz.player1_time < quiz.player2_time:
                    quiz.winner = quiz.player2
                    EmailServices.send_email_win(player2_user.email)
                    EmailServices.send_email_lose(player1_user.email)

                else:
                    quiz.winner = "Draw"
                    EmailServices.send_email_draw(player2_user.email)
                    EmailServices.send_email_draw(player1_user.email)

            self.db.add(quiz)
            self.db.commit()
            self.db.refresh(quiz)
            return quiz

        except Exception as e:
            raise e
