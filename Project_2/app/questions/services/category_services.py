from app.db.database import SessionLocal
from app.questions.exceptions import *
from app.questions.repository.category_repository import CategoryRepository


class CategoryServices:
    @staticmethod
    def create_category(category):
        try:
            with SessionLocal() as db:
                category_repository = CategoryRepository(db)
                a_type = category_repository.read_category_by_type(category)
                if a_type is None:
                    return category_repository.create_category(category)
                raise CategoryExistsException(message="Category already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_category_by_id(category_id: str):
        try:
            with SessionLocal() as db:
                category_repository = CategoryRepository(db)
                return category_repository.read_category_by_id(category_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_categories():
        with SessionLocal() as db:
            category_repository = CategoryRepository(db)
            return category_repository.read_all_categories()

    @staticmethod
    def delete_category_by_id(category_id: str):
        try:
            with SessionLocal() as db:
                category_repository = CategoryRepository(db)
                category_repository.delete_category_by_id(category_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_category(category_id: str, category: str):
        try:
            with SessionLocal() as db:
                category_repository = CategoryRepository(db)
                return category_repository.update_category(category_id, category)
        except Exception as e:
            raise e
