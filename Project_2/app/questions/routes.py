from fastapi import APIRouter, Depends
from app.questions.controller import CategoryController, QuestionController
from app.users.controller.user_auth_controller import JWTBearer
from app.questions.schemas import *

category_router = APIRouter(tags=["Category"], prefix="/api/category")


@category_router.post("/add-new-category", response_model=CategorySchema,
                      dependencies=[Depends(JWTBearer("super_user"))])
def create_category(category: CategorySchemaIn):
    return CategoryController.create_category(category.category)


@category_router.get("/id", response_model=CategorySchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_category_by_id(category_id: str):
    return CategoryController.get_category_by_id(category_id)


@category_router.get("/get-all-categories", response_model=list[CategorySchema],
                     dependencies=[Depends(JWTBearer("super_user"))])
def get_all_categories():
    return CategoryController.get_all_categories()


@category_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_category_by_id(category_id: str):
    return CategoryController.delete_category_by_id(category_id)


@category_router.put("/update", response_model=CategorySchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_category(category_id, category):
    return CategoryController.update_category(category_id, category)


question_router = APIRouter(tags=["Question"], prefix="/api/questions")


@question_router.post("/add-new-question", response_model=QuestionSchema,
                      dependencies=[Depends(JWTBearer("super_user"))])
def create_question(question: QuestionSchemaIn):
    return QuestionController.create_question(question.text, question.answer_a, question.answer_b, question.answer_c,
                                              question.answer_d, question.correct_answer, question.category_id)


@question_router.get("/id", response_model=QuestionSchema)
def get_question_by_id(question_id: str):
    return QuestionController.get_question_by_id(question_id)


@question_router.get("/get-all-questions", response_model=list[QuestionSchema])
def get_all_questions():
    return QuestionController.get_all_questions()


@question_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_question_by_id(question_id: str):
    return QuestionController.delete_question_by_id(question_id)


@question_router.put("/update-question-by-id", response_model=QuestionSchema,
                     dependencies=[Depends(JWTBearer("super_user"))])
def update_question(
    question_id: str,
    text: str = None,
    answer_a: str = None,
    answer_b: str = None,
    answer_c: str = None,
    answer_d: str = None,
    correct_answer: str = None,
    category_id: str = None
):
    return QuestionController.update_question(question_id, text, answer_a, answer_b, answer_c, answer_d, correct_answer,
                                              category_id)


