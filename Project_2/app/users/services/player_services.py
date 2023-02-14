from app.db.database import SessionLocal
from app.users.repository.player_repository import PlayerRepository


class PlayerServices:

    @staticmethod
    def create_player(username: str, user_id: str):
        with SessionLocal() as db:
            try:
                player_repository = PlayerRepository(db)
                return player_repository.create_player(username, user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_player_by_id(player_id: str):
        with SessionLocal() as db:
            try:
                player_repository = PlayerRepository(db)
                return player_repository.get_player_by_id(player_id=player_id)
            except Exception as e:
                raise e
