from pydantic import UUID4, BaseModel
from pydantic.schema import Optional


class QandASchema(BaseModel):
    id: UUID4
    quiz_id: str
    question_id: str
    player1_answer: Optional[str]
    player2_answer: Optional[str]

    class Config:
        orm_mode = True


class QandASchemaIn(BaseModel):
    quiz_id: str

    class Config:
        orm_mode = True
