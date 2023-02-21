from uuid import uuid4

from sqlalchemy import Column, String

from app.db.database import Base


class AdminType(Base):
    __tablename__ = "admin_types"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    admin_type = Column(String(50), unique=True)
    role = Column(String(50))
    seniority = Column(String(50))

    def __init__(self, admin_type, role, seniority):
        self.admin_type = admin_type
        self.role = role
        self.seniority = seniority
        