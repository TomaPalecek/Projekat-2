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

    @staticmethod
    def get_player_by_username(username: str):
        with SessionLocal() as db:
            try:
                player_repository = PlayerRepository(db)
                return player_repository.get_player_by_username(username=username)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_players():
        try:
            with SessionLocal() as db:
                player_repository = PlayerRepository(db)
                return player_repository.get_all_players()
        except Exception as e:
            raise e

    @staticmethod
    def delete_player_by_id(player_id: str):
        try:
            with SessionLocal() as db:
                player_repository = PlayerRepository(db)
                player_repository.delete_player_by_id(player_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_player(
        player_id: str,
        username: str = None,
        played_quizzes: str = None,
        questions_taken: str = None,
        correct_answers: str = None,
        incorrect_answers: str = None,
        win_rate: str = None
    ):
        try:
            with SessionLocal() as db:
                player_repository = PlayerRepository(db)
                return player_repository.update_player(player_id, username, played_quizzes, questions_taken,
                                                       correct_answers, incorrect_answers, win_rate)
        except Exception as e:
            raise e
