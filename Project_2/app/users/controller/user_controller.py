from app.users.services import UserServices
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


class UserController:

    @staticmethod
    def create_user(email, password):
        try:
            user = UserServices.create_user(email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_id(user_id: str):
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"user with provided id {user_id} doesn't exist.")

    @staticmethod
    def get_all_users():
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserServices.delete_user_by_id(user_id)
            return {"message": f"User with provided id, {user_id}, is deleted."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            user = UserServices.update_user_is_active(user_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
