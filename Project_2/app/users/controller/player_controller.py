from app.users.services import PlayerServices
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.users.exceptions import *


class PlayerController:

    @staticmethod
    def create_player(username, user_id):
        try:
            player = PlayerServices.create_player(username, user_id)
            return player
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"Player with provided username - {username} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_player_by_id(player_id: str):
        try:
            return PlayerServices.get_player_by_id(player_id=player_id)
        except PlayerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
