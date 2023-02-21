from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import *
from app.users.models import AdminType


class AdminTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_admin_type(self, admin_type, role, seniority):
        try:
            admin_type = AdminType(admin_type, role, seniority)
            self.db.add(admin_type)
            self.db.commit()
            self.db.refresh(admin_type)
            return admin_type
        except IntegrityError as e:
            raise e

    def read_admin_type_by_id(self, admin_type_id: str):
        admin_type = self.db.query(AdminType).filter(AdminType.id == admin_type_id).first()
        if admin_type is None:
            raise AdminTypeNotFoundException(f"Admin type with provided ID: {admin_type_id} not found.", 400)
        return admin_type

    def read_admin_type_by_type(self, admin_type: str):
        a_type = self.db.query(AdminType).filter(AdminType.admin_type == admin_type).first()
        return a_type

    def read_all_admin_types(self):
        admin_types = self.db.query(AdminType).all()
        return admin_types

    def delete_admin_type_by_id(self, admin_type_id: str):
        try:
            admin_type = self.db.query(AdminType).filter(AdminType.id == admin_type_id).first()
            if admin_type is None:
                raise AdminTypeNotFoundException(
                    f"Admin type with provided ID: {admin_type_id} not found.",
                    400,
                )
            self.db.delete(admin_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_admin_type(self, admin_type_id: str = None, admin_type: str = None, role: str = None,
                          seniority: str = None):
        try:
            a_type = self.db.query(AdminType).filter(AdminType.id == admin_type_id).first()
            if a_type is None:
                raise AdminTypeNotFoundException(
                    f"Admin type with provided ID: {admin_type_id} not found.", 400,)

            if admin_type is not None:
                a_type.admin_type = admin_type

            if role is not None:
                a_type.role = role

            if seniority is not None:
                a_type.seniority = seniority

            self.db.add(a_type)
            self.db.commit()
            self.db.refresh(a_type)
            return a_type
        except Exception as e:
            raise e
