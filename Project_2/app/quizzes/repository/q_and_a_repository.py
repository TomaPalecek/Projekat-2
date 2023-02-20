from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.quizzes.exceptions import *
from app.quizzes.models import QandA
from app.questions.models import Question


class QandARepository:
    def __init__(self, db: Session):
        self.db = db

    def get_random_question_id(self, quiz_id):
        subquery = self.db.query(QandA.question_id).filter_by(quiz_id=quiz_id).subquery()

        question_id = self.db.query(Question.id).filter(~Question.id.in_(subquery)).order_by(func.rand()).limit(1).\
            scalar()
        if question_id:
            return question_id
        return None

    def num_of_questions_for_quiz(self, quiz_id):
        count = self.db.query(func.count(QandA.quiz_id)).filter_by(quiz_id=quiz_id).scalar()
        print(count)
        if count >= 10:
            raise QuizHasTenQuestionsException(f"Quiz with provided ID: {quiz_id} already has {count} questions.", 400)
        return True

    def generate_question_for_quiz(self, quiz_id):
        try:
            if self.num_of_questions_for_quiz(quiz_id):

                question_id = self.get_random_question_id(quiz_id)

                if not question_id:
                    raise NoMoreQuestionsException("No more questions available for this quizz", 400)

                q_and_a = QandA(quiz_id=quiz_id, question_id=question_id)
                print(q_and_a)
                self.db.add(q_and_a)
                self.db.commit()
                self.db.refresh(q_and_a)
                return q_and_a

        except IntegrityError as e:
            raise e

    def get_q_and_a_by_id(self, q_and_a_id: str):
        q_and_a = self.db.query(QandA).filter(QandA.id == q_and_a_id).first()
        if q_and_a is None:
            raise QandANotFoundException(f"Q and A with provided ID: {q_and_a_id} not found.", 400)
        return q_and_a

    def get_all_q_and_as_by_quiz_id(self, quiz_id: str):
        q_and_as = self.db.query(QandA).filter(QandA.quiz_id == quiz_id).all()
        print(q_and_as)
        return q_and_as

    def delete_q_and_a_by_id(self, q_and_a_id: str):
        try:
            q_and_a = self.db.query(QandA).filter(QandA.id == q_and_a_id).first()
            if q_and_a is None:
                raise QandANotFoundException(f"Q and A with provided ID: {q_and_a_id} not found.", 400)
            self.db.delete(q_and_a)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_q_and_a(
        self,
        q_and_a_id: str,
        name: str = None,
        last_name: str = None,
        q_and_a_type_id: str = None,
    ):
        try:
            q_and_a = self.db.query(QandA).filter(QandA.id == q_and_a_id).first()
            if q_and_a is None:
                raise QandANotFoundException(f"Q and A with provided ID: {q_and_a_id} not found.", 400)
            if name is not None:
                q_and_a.name = name
            if last_name is not None:
                q_and_a.last_name = last_name
            if q_and_a_type_id is not None:
                q_and_a.q_and_a_type_id = q_and_a_type_id
            self.db.add(q_and_a)
            self.db.commit()
            self.db.refresh(q_and_a)
            return q_and_a
        except Exception as e:
            raise e
