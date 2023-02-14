from fastapi import APIRouter
from app.users.controller import UserController, PlayerController
from app.users.schemas import UserSchema, UserSchemaIn
from app.users.schemas import PlayerSchema, PlayerSchemaIn

user_router = APIRouter(prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.get("/id/{user_id}", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.delete("/")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id, is_active)


player_router = APIRouter(prefix="/api/players")


@player_router.post("/add-new-player", response_model=PlayerSchema)
def create_player(player: PlayerSchemaIn):
    return PlayerController.create_player(username=player.username, user_id=player.user_id)


@player_router.get("/get-player-by-id", response_model=PlayerSchema)
def get_player_by_id(player_id: str):
    return PlayerController.get_player_by_id(player_id=player_id)
