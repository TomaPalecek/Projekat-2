from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.questions.exceptions import *
from app.questions.models import Category


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category):
        try:
            category = Category(category)
            self.db.add(category)
            self.db.commit()
            self.db.refresh(category)
            return category
        except IntegrityError as e:
            raise e

    def read_category_by_id(self, category_id: str):
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if category is None:
            raise CategoryNotFoundException(f"Category with provided ID: {category_id} not found.", 400)
        return category

    def read_category_by_type(self, category: str):
        a_type = self.db.query(Category).filter(Category.category == category).first()
        return a_type

    def read_all_categories(self):
        categories = self.db.query(Category).all()
        return categories

    def delete_category_by_id(self, category_id: str):
        try:
            category = self.db.query(Category).filter(Category.id == category_id).first()
            if category is None:
                raise CategoryNotFoundException(
                    f"Category with provided ID: {category_id} not found.",
                    400,
                )
            self.db.delete(category)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_category(self, category_id: str, category: str = None):
        try:
            a_type = self.db.query(Category).filter(Category.id == category_id).first()
            if a_type is None:
                raise CategoryNotFoundException(
                    f"Category with provided ID: {category_id} not found.",
                    400,
                )
            a_type.category = category
            self.db.add(a_type)
            self.db.commit()
            self.db.refresh(a_type)
            return a_type
        except Exception as e:
            raise e
