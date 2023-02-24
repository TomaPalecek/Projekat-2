from app.db.database import SessionLocal
from app.users.repository.admin_repository import AdminRepository


class AdminServices:
    @staticmethod
    def create_admin(name: str, last_name: str, admin_type_id: str, user_id: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.create_admin(name, last_name, admin_type_id, user_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_admin_by_id(admin_id: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.get_admin_by_id(admin_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_admins_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.get_admins_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_admins_by_admin_type_id(admin_type_id: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.get_admins_by_admin_type_id(admin_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_admins():
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.get_all_admins()
        except Exception as e:
            raise e

    @staticmethod
    def delete_admin_by_id(admin_id: str):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                admin_repository.delete_admin_by_id(admin_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_admin(
        admin_id: str,
        name: str = None,
        last_name: str = None,
        admin_type_id: str = None,
    ):
        try:
            with SessionLocal() as db:
                admin_repository = AdminRepository(db)
                return admin_repository.update_admin(admin_id, name, last_name, admin_type_id)
        except Exception as e:
            raise e
