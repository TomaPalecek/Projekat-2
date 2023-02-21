from app.db.database import SessionLocal
from app.users.exceptions import *
from app.users.repository.admin_type_repository import AdminTypeRepository


class AdminTypeServices:
    @staticmethod
    def create_admin_type(admin_type, role, seniority):
        try:
            with SessionLocal() as db:
                admin_type_repository = AdminTypeRepository(db)
                a_type = admin_type_repository.read_admin_type_by_type(admin_type)
                if a_type is None:
                    return admin_type_repository.create_admin_type(admin_type, role, seniority)
                raise AdminTypeExistsException(message="Type already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_admin_type_by_id(admin_type_id: str):
        try:
            with SessionLocal() as db:
                admin_type_repository = AdminTypeRepository(db)
                return admin_type_repository.read_admin_type_by_id(admin_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_admin_types():
        with SessionLocal() as db:
            admin_type_repository = AdminTypeRepository(db)
            return admin_type_repository.read_all_admin_types()

    @staticmethod
    def delete_admin_type_by_id(admin_type_id: str):
        try:
            with SessionLocal() as db:
                admin_type_repository = AdminTypeRepository(db)
                admin_type_repository.delete_admin_type_by_id(admin_type_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_admin_type(admin_type_id: str, admin_type: str, role: str, seniority: str):
        try:
            with SessionLocal() as db:
                admin_type_repository = AdminTypeRepository(db)
                return admin_type_repository.update_admin_type(admin_type_id, admin_type, role, seniority)
        except Exception as e:
            raise e
