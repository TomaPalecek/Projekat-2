from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String

from app.db.database import Base


class Question(Base):

    __tablename__ = "questions"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    text = Column(String(100))
    answer_a = Column(String(100))
    answer_b = Column(String(100))
    answer_c = Column(String(100))
    answer_d = Column(String(100))
    # mozda veci broj karaktera da dopustim pa posle da hvatam gresku ako upisu vise
    correct_answer = Column(String(1))

    category_id = Column(String(50), ForeignKey("categories.id"), nullable=False)

    def __init__(self, text, answer_a, answer_b, answer_c, answer_d, correct_answer, category_id):
        self.text = text
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.answer_c = answer_c
        self.answer_d = answer_d
        self.correct_answer = correct_answer
        self.category_id = category_id
