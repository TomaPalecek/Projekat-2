
from pydantic.schema import Optional
from pydantic import UUID4, BaseModel, NonNegativeInt


class QuizSchema(BaseModel):
    id: UUID4
    player1: str
    player2: str
    player1_answers: str
    player2_answers: str
    player1_time: NonNegativeInt
    player2_time: NonNegativeInt
    status: str
    questions: str
    winner: str

    class Config:
        orm_mode = True


class QuizSchemaIn(BaseModel):
    player1: str
    player2: str

    class Config:
        orm_mode = True


class QuizSchemaIn2(BaseModel):
    player1: str

    player1_answers: str

    player1_time: int

    class Config:
        orm_mode = True
