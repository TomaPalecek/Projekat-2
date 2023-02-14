from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.db.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    username = Column(String(100), unique=True)
    played_quizzes = Column(Integer)
    questions_taken = Column(Integer)
    correct_answers = Column(Integer)
    incorrect_answers = Column(Integer)
    win_rate = Column(Float)
    num_of_achievements = Column(Integer)

    user_id = Column(String(50), ForeignKey("users.id"))
    user = relationship("User", lazy="subquery")

    def __init__(self, username, user_id, played_quizzes=0, questions_taken=0, correct_answers=0, incorrect_answers=0,
                 win_rate=0, num_of_achievements=0):
        self.username = username
        self.user_id = user_id
        self.played_quizzes = played_quizzes
        self.questions_taken = questions_taken
        self.correct_answers = correct_answers
        self.incorrect_answers = incorrect_answers
        self.win_rate = win_rate
        self.num_of_achievements = num_of_achievements
