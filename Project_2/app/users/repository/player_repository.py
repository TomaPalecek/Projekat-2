from sqlalchemy.exc import IntegrityError

from app.users.models import Player
from app.users.exceptions import *
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
        if player is None:
            raise PlayerNotFoundException(f"Player with provided ID: {player_id} not found.", 400)
        return player

    def get_player_by_username(self, username: str):
        player = self.db.query(Player).filter(Player.username == username).first()
        if player is None:
            raise PlayerNotFoundException(f"Player with provided ID: {username} not found.", 400)
        return player

    def get_all_players(self):
        player = self.db.query(Player).all()
        return player
    
    def delete_player_by_id(self, player_id: str):
        try:
            player = self.db.query(Player).filter(Player.id == player_id).first()
            if player is None:
                raise PlayerNotFoundException(f"Player with provided ID: {player_id} not found.", 400)
            self.db.delete(player)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_player(
        self,
        player_id: str,
        username: str = None,
        played_quizzes: str = None,
        questions_taken: str = None,
        correct_answers: str = None,
        incorrect_answers: str = None
    ):
        try:
            player = self.db.query(Player).filter(Player.id == player_id).first()
            if player is None:
                raise PlayerNotFoundException(f"Player with provided ID: {player_id} not found.", 400)

            if username is not None:
                player.username = username
            if played_quizzes is not None:
                player.played_quizzes = played_quizzes
            if questions_taken is not None:
                player.questions_taken = questions_taken
            if correct_answers is not None:
                player.correct_answers = correct_answers
            if incorrect_answers is not None:
                player.incorrect_answers = incorrect_answers

            self.db.add(player)
            self.db.commit()
            self.db.refresh(player)
            return player
        except Exception as e:
            raise e
