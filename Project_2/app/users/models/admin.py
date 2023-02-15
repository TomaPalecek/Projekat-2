from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String

from app.db.database import Base


class Admin(Base):
    __tablename__ = "admins"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    last_name = Column(String(50))

    admin_type_id = Column(String(50), ForeignKey("admin_types.id"), nullable=False)

    def __init__(self, name, last_name, admin_type_id):
        self.name = name
        self.last_name = last_name
        self.admin_type_id = admin_type_id
