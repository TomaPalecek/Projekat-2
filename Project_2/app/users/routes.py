from fastapi import APIRouter, Depends
from app.users.controller import UserController, PlayerController, AdminController, AdminTypeController
from app.users.controller.user_auth_controller import JWTBearer
from app.users.schemas import *

user_router = APIRouter(tags=["User"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema)
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.email, user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user(user: UserSchemaUpdate):
    return UserController.update_user_is_active(user.id, user.is_active)


player_router = APIRouter(tags=["Player"], prefix="/api/players")


@player_router.post("/add-new-player", response_model=PlayerSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_player(player: PlayerSchemaIn):
    return PlayerController.create_player(username=player.username, user_id=player.user_id)


@player_router.get("/get-player-by-id", response_model=PlayerSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_player_by_id(player_id: str):
    return PlayerController.get_player_by_id(player_id=player_id)


@player_router.get("/get-player-by-username", response_model=PlayerSchema,
                   dependencies=[Depends(JWTBearer("super_user"))])
def get_player_by_username(username: str):
    return PlayerController.get_player_by_username(username=username)


@player_router.get("/get-all-players", response_model=list[PlayerSchema])
def get_all_players():
    return PlayerController.get_all_players()


@player_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_player_by_id(player_id: str):
    return PlayerController.delete_player_by_id(player_id)


@player_router.put("/update-player-by-id", response_model=PlayerSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_player(player: PlayerSchemaUpdate):
    return PlayerController.update_player(player.player_id, player.username, player.played_quizzes, player.questions_taken,
                                          player.correct_answers, player.incorrect_answers)


admin_router = APIRouter(tags=["Admin"], prefix="/api/admins")


@admin_router.post("/add-new-admin", response_model=AdminSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_admin(admin: AdminSchemaIn):
    return AdminController.create_admin(admin.name, admin.last_name, admin.admin_type_id, admin.user_id)


@admin_router.get("/id", response_model=AdminSchema)
def get_admin_by_id(admin_id: str):
    return AdminController.get_admin_by_id(admin_id)


@admin_router.get("/get-all-admins", response_model=list[AdminSchema])
def get_all_admins():
    return AdminController.get_all_admins()


@admin_router.get("/get-admins-by-characters", response_model=list[AdminSchema])
def get_admins_by_characters(characters):
    return AdminController.get_admins_by_characters(characters)


@admin_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_admin_by_id(admin_id: str):
    return AdminController.delete_admin_by_id(admin_id)


@admin_router.put("/update-admin-by-id", response_model=AdminSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_admin(admin: AdminSchemaUpdate):
    return AdminController.update_admin(admin.id, admin.name, admin.last_name, admin.admin_type_id)


admin_type_router = APIRouter(tags=["Admin Type"], prefix="/api/admin-type")


@admin_type_router.post("/add-new-admin-type", response_model=AdminTypeSchema,
                        dependencies=[Depends(JWTBearer("super_user"))])
def create_admin_type(admin_type: AdminTypeSchemaIn):
    return AdminTypeController.create_admin_type(admin_type.admin_type, admin_type.role, admin_type.seniority)


@admin_type_router.get("/id", response_model=AdminTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_admin_type_by_id(admin_type_id: str):
    return AdminTypeController.get_admin_type_by_id(admin_type_id)


@admin_type_router.get("/get-all-admin-types", response_model=list[AdminTypeSchema],
                       dependencies=[Depends(JWTBearer("super_user"))])
def get_all_admin_types():
    return AdminTypeController.get_all_admin_types()


@admin_type_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_admin_type_by_id(admin_type_id: str):
    return AdminTypeController.delete_admin_type_by_id(admin_type_id)


@admin_type_router.put("/update", response_model=AdminTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_admin_type(admin_type: AdminTypeSchemaUpdate):
    return AdminTypeController.update_admin_type(admin_type.id, admin_type.admin_type, admin_type.role,
                                                 admin_type.seniority)
