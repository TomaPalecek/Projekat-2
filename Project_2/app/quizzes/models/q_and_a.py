from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String

from app.db.database import Base


class QandA(Base):
    __tablename__ = "q_and_as"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    quiz_id = Column(String(50), ForeignKey("quizzes.id"), nullable=False)
    question_id = Column(String(50), ForeignKey("questions.id"), nullable=False)
    player1_answers = Column(String(50))
    player2_answers = Column(String(50))

    def __init__(self, quiz_id, question_id, player1_answers="", player2_answers=""):
        self.quiz_id = quiz_id
        self.question_id = question_id
        self.player1_answers = player1_answers
        self.player2_answers = player2_answers

    def __str__(self):
        return f"{self.quiz_id}, {self.question_id}"
