from uuid import uuid4
from sqlalchemy import Column, String, Integer, ForeignKey
from app.db.database import Base


class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    player1 = Column(String(50), ForeignKey("players.username"), nullable=False)
    player2 = Column(String(50), ForeignKey("players.username"), nullable=False)
    player1_time = Column(Integer)
    player2_time = Column(Integer)
    player1_score = Column(Integer)
    player2_score = Column(Integer)
    winner = Column(String(100))
    status = Column(String(100), default="Pending")

    def __init__(self, player1, player2, player1_time=0, player2_time=0, player1_score=None, player2_score=None, winner="", status="Pending"):
        self.player1 = player1
        self.player2 = player2
        self.player1_time = player1_time
        self.player2_time = player2_time
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.winner = winner
        self.status = status
