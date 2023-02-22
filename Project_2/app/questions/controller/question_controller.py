from fastapi import HTTPException, Response, status

from app.questions.exceptions import *
from app.questions.services import QuestionServices, CategoryServices


class QuestionController:
    @staticmethod
    def create_question(text, answer_a, answer_b, answer_c, answer_d, correct_answer, category_id):
        try:
            CategoryServices.get_category_by_id(category_id)
            question = QuestionServices.create_question(text, answer_a, answer_b, answer_c, answer_d, correct_answer,
                                                        category_id)
            return question
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_question_by_id(question_id: str):
        try:
            question = QuestionServices.get_question_by_id(question_id)
            if question:
                return question
        except QuestionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_questions_by_category_id(category_id: str):
        questions = QuestionServices.get_questions_by_category_id(category_id)
        if questions:
            return questions
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Question with provided question type id {category_id} does not exist",
        )

    @staticmethod
    def get_all_questions():
        question = QuestionServices.get_all_questions()
        return question

    @staticmethod
    def delete_question_by_id(question_id: str):
        try:
            QuestionServices.delete_question_by_id(question_id)
            return Response(content=f"Question with id - {question_id} is deleted")
        except QuestionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_question(
            question_id: str,
            text: str = None,
            answer_a: str = None,
            answer_b: str = None,
            answer_c: str = None,
            answer_d: str = None,
            correct_answer: str = None,
            category_id: str = None,
    ):
        try:
            question = QuestionServices.update_question(question_id, text, answer_a, answer_b, answer_c, answer_d,
                                                        correct_answer, category_id)
            return question
        except QuestionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
