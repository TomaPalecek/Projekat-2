from fastapi import APIRouter, Depends
from app.questions.controller import CategoryController
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
