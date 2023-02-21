from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.questions.exceptions import *
from app.questions.models import Question


class QuestionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_question(self, text, answer_a, answer_b, answer_c, answer_d, correct_answer, category_id):
        try:
            question = Question(text, answer_a, answer_b, answer_c, answer_d, correct_answer, category_id)
            self.db.add(question)
            self.db.commit()
            self.db.refresh(question)
            return question
        except IntegrityError as e:
            raise e

    def get_question_by_id(self, question_id: str):
        question = self.db.query(Question).filter(Question.id == question_id).first()
        print(question)
        if question is None:
            raise QuestionNotFoundException(f"Question with provided ID: {question_id} not found.", 400)
        return question

    def get_questions_by_category_id(self, category_id: str):
        question = self.db.query(Question).filter(Question.category_id == category_id).all()
        if question is None:
            raise QuestionNotFoundException(
                f"Questions with provided category id: {category_id} not found.",
                400,
            )
        return question

    def get_all_questions(self):
        question = self.db.query(Question).all()
        return question

    def delete_question_by_id(self, question_id: str):
        try:
            question = self.db.query(Question).filter(Question.id == question_id).first()
            if question is None:
                raise QuestionNotFoundException(f"Question with provided ID: {question_id} not found.", 400)
            self.db.delete(question)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_question(
        self,
        question_id: str,
        text: str = None,
        answer_a: str = None,
        answer_b: str = None,
        answer_c: str = None,
        answer_d: str = None,
        correct_answer: str = None,
        category_id: str = None
    ):
        try:
            question = self.db.query(Question).filter(Question.id == question_id).first()

            if question is None:
                raise QuestionNotFoundException(f"Question with provided ID: {question_id} not found.", 400)
            if text is not None:
                question.text = text
            if answer_a is not None:
                question.answer_a = answer_a
            if answer_b is not None:
                question.answer_b = answer_b
            if answer_c is not None:
                question.answer_c = answer_c
            if answer_d is not None:
                question.answer_d = answer_d
            if correct_answer is not None:
                question.correct_answer = correct_answer
            if category_id is not None:
                question.category_id = category_id

            self.db.add(question)
            self.db.commit()
            self.db.refresh(question)
            return question
        except Exception as e:
            raise e
