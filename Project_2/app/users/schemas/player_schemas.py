from pydantic import BaseModel
from pydantic import UUID4

from app.users.schemas import UserSchema


class PlayerSchema(BaseModel):
    id: UUID4
    username: str
    user_id: str
    user: UserSchema
    played_quizzes: int
    questions_taken: int
    correct_answers: int
    incorrect_answers: int

    class Config:
        orm_mode = True


class PlayerSchemaIn(BaseModel):

    username: str
    user_id: str

    class Config:
        orm_mode = True
