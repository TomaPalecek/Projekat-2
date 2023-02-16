from uuid import uuid4

from sqlalchemy import Column, String

from app.db.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    category = Column(String(50), unique=True)

    def __init__(self, category):
        self.category = category
