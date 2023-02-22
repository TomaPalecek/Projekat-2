from sqlalchemy.exc import IntegrityError
from app.users.services import PlayerServices
from fastapi import HTTPException, Response
from app.users.exceptions import *


class PlayerController:

    @staticmethod
    def create_player(username, user_id):
        try:
            player = PlayerServices.create_player(username, user_id)
            return player
        except PlayerExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"Provided User ID {user_id} does not exist.")
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

    @staticmethod
    def get_player_by_username(username: str):
        try:
            player = PlayerServices.get_player_by_username(username=username)
            if player:
                return player
            else:
                raise HTTPException(status_code=400, detail=f"Player with provided username {username} doesn't exist.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_all_players():
        player = PlayerServices.get_all_players()
        return player

    @staticmethod
    def delete_player_by_id(player_id: str):
        try:
            PlayerServices.delete_player_by_id(player_id)
            return Response(content=f"Player with id - {player_id} is deleted")
        except PlayerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_player(
        player_id: str,
        username: str = None,
        played_quizzes: str = None,
        questions_taken: str = None,
        correct_answers: str = None,
        incorrect_answers: str = None
    ):
        try:
            player = PlayerServices.update_player(player_id, username, played_quizzes, questions_taken,
                                                  correct_answers, incorrect_answers)
            return player
        except PlayerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
