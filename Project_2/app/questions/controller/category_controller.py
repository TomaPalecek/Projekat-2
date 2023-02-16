from fastapi import HTTPException, Response

from app.questions.exceptions import *
from app.questions.services import CategoryServices


class CategoryController:
    @staticmethod
    def create_category(category):
        try:
            a_type = CategoryServices.create_category(category)
            return a_type

        except CategoryExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_category_by_id(category_id: str):
        try:
            category = CategoryServices.get_category_by_id(category_id)
            if category:
                return category
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_category_by_type_name(category_name: str):
        try:
            category = CategoryServices.get_category_by_id(category_name)
            if category:
                return category
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_categories():
        categories = CategoryServices.get_all_categories()
        return categories

    @staticmethod
    def delete_category_by_id(category_id: str):
        try:
            CategoryServices.delete_category_by_id(category_id)
            return Response(content=f"Category with id - {category_id} is deleted")
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_category(category_id: str, category: str):
        try:
            a_type = CategoryServices.update_category(category_id, category)
            return a_type
        except CategoryNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
