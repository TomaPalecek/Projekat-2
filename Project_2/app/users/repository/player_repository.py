from sqlalchemy.exc import IntegrityError

from app.users.models import Player
from sqlalchemy.orm import Session


class PlayerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_player(self, username, user_id):
        try:
            player = Player(username, user_id)
            self.db.add(player)
            self.db.commit()
            self.db.refresh(player)
            return player

        except IntegrityError as e:
            raise e

    def get_player_by_id(self, player_id: str):
        player = self.db.query(Player).filter(Player.id == player_id).first()
        return player
