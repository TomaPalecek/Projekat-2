from fastapi import HTTPException, Response, status

from app.users.exceptions import *
from app.users.services import AdminServices, AdminTypeServices


class AdminController:
    @staticmethod
    def create_admin(name, last_name, admin_type_id):
        try:
            AdminTypeServices.get_admin_type_by_id(admin_type_id)
            admin = AdminServices.create_admin(name, last_name, admin_type_id)
            return admin
        except AdminTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_admin_by_id(admin_id: str):
        admin = AdminServices.get_admin_by_id(admin_id)
        if admin:
            return admin
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Admin with provided id {admin_id} does not exist")

    @staticmethod
    def get_admins_by_characters(characters: str):
        admins = AdminServices.get_admins_by_characters(characters)
        if admins:
            return admins
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Admin with provided characters {characters} does not exist")

    @staticmethod
    def get_admins_by_admin_type_id(admin_type_id: str):
        admins = AdminServices.get_admins_by_admin_type_id(admin_type_id)
        if admins:
            return admins
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Admin with provided admin type id {admin_type_id} does not exist")

    @staticmethod
    def get_all_admins():
        admin = AdminServices.get_all_admins()
        return admin

    @staticmethod
    def delete_admin_by_id(admin_id: str):
        try:
            AdminServices.delete_admin_by_id(admin_id)
            return Response(content=f"Admin with id - {admin_id} is deleted")
        except AdminNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_admin(
        admin_id: str,
        name: str = None,
        last_name: str = None,
        admin_type_id: str = None,
    ):
        try:
            if admin_type_id is not None:
                AdminTypeServices.get_admin_type_by_id(admin_type_id)
            admin = AdminServices.update_admin(admin_id, name, last_name, admin_type_id)
            return admin
        except AdminTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
