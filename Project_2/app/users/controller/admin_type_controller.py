from fastapi import HTTPException, Response

from app.users.exceptions import *
from app.users.services import AdminTypeServices


class AdminTypeController:
    @staticmethod
    def create_admin_type(admin_type):
        try:
            a_type = AdminTypeServices.create_admin_type(admin_type)
            return a_type

        except AdminTypeExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_admin_type_by_id(admin_type_id: str):
        try:
            admin_type = AdminTypeServices.get_admin_type_by_id(admin_type_id)
            if admin_type:
                return admin_type
        except AdminTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_admin_type_by_type_name(admin_type_name: str):
        try:
            admin_type = AdminTypeServices.get_admin_type_by_id(admin_type_name)
            if admin_type:
                return admin_type
        except AdminTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_admin_types():
        admin_types = AdminTypeServices.get_all_admin_types()
        return admin_types

    @staticmethod
    def delete_admin_type_by_id(admin_type_id: str):
        try:
            AdminTypeServices.delete_admin_type_by_id(admin_type_id)
            return Response(content=f"Admin type with id - {admin_type_id} is deleted")
        except AdminTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_admin_type(admin_type_id: str, admin_type: str):
        try:
            a_type = AdminTypeServices.update_admin_type(admin_type_id, admin_type)
            return a_type
        except AdminTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
