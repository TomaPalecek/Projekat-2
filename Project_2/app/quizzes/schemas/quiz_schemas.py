

from pydantic import UUID4, BaseModel


class QuizSchema(BaseModel):
    id: UUID4
    player1: str
    player2: str
    player1_answers: str
    player2_answers: str
    player1_time: int
    player2_time: int
    status: str
    questions: str
    winner: str

    class Config:
        orm_mode = True


class QuizSchemaIn1(BaseModel):
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
