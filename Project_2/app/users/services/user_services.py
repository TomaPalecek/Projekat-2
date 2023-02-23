"""User Services module"""
import hashlib
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword
from app.users.repository.user_repository import UserRepository


class UserServices:
    """User Service class"""
    @staticmethod
    def create_user(email, password: str):
        """

        :param email: EmailStr of user
        :param password: password of user
        :return: user
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def create_super_user(email, password):
        """

        :param email: EmailStr
        :param password: this mans password which is hashed might i add
        :return: a super user
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        """

        :param user_id: a uuid4 for the usre in string form
        :return: a user whit that id
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_user_by_id(user_id)

    @staticmethod
    def get_all_users():
        """

        :return: list of users
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def delete_user_by_id(user_id: str):
        """

        :param user_id: a uuid4 for the usre in string form
        :return: Nothing hopefully
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """

        :param user_id: a uuid4 for the usre in string form
        :param is_active: is he active??
        :return: updated user
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
        """

        :param email: EmailStr of user
        :param password: Hashed password of user
        :return: token
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
