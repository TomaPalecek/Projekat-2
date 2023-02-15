from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import *
from app.users.models import Admin


class AdminRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_admin(self, name, last_name, admin_type_id):
        try:
            admin = Admin(name, last_name, admin_type_id)
            self.db.add(admin)
            self.db.commit()
            self.db.refresh(admin)
            return admin
        except IntegrityError as e:
            raise e

    def get_admin_by_id(self, admin_id: str):
        admin = self.db.query(Admin).filter(Admin.id == admin_id).first()
        if admin is None:
            raise AdminNotFoundException(f"Admin with provided ID: {admin_id} not found.", 400)
        return admin

    def get_admins_by_characters(self, characters: str):
        admin = self.db.query(Admin).filter(Admin.name.like(characters + "%")).all()
        if admin is None:
            raise AdminNotFoundException(f"Admin with provided characters: {characters} not found.", 400)
        return admin

    def get_admins_by_admin_type_id(self, admin_type_id: str):
        admin = self.db.query(Admin).filter(Admin.admin_type_id == admin_type_id).first()
        if admin is None:
            raise AdminNotFoundException(
                f"Admin with provided admin type id: {admin_type_id} not found.",
                400,
            )
        return admin

    def get_all_admins(self):
        admin = self.db.query(Admin).all()
        return admin

    def delete_admin_by_id(self, admin_id: str):
        try:
            admin = self.db.query(Admin).filter(Admin.id == admin_id).first()
            if admin is None:
                raise AdminNotFoundException(f"Admin with provided ID: {admin_id} not found.", 400)
            self.db.delete(admin)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_admin(
        self,
        admin_id: str,
        name: str = None,
        last_name: str = None,
        admin_type_id: str = None,
    ):
        try:
            admin = self.db.query(Admin).filter(Admin.id == admin_id).first()
            if admin is None:
                raise AdminNotFoundException(f"Admin with provided ID: {admin_id} not found.", 400)
            if name is not None:
                admin.name = name
            if last_name is not None:
                admin.last_name = last_name
            if admin_type_id is not None:
                admin.admin_type_id = admin_type_id
            self.db.add(admin)
            self.db.commit()
            self.db.refresh(admin)
            return admin
        except Exception as e:
            raise e
