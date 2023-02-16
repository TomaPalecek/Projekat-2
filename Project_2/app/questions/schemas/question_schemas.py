from pydantic import UUID4, BaseModel


class QuestionSchema(BaseModel):
    id: UUID4
    text: str
    answer_a: str
    answer_b: str
    answer_c: str
    answer_d: str
    correct_answer: str
    category_id: str

    class Config:
        orm_mode = True


class QuestionSchemaIn(BaseModel):
    text: str
    answer_a: str
    answer_b: str
    answer_c: str
    answer_d: str
    correct_answer: str
    category_id: str

    class Config:
        orm_mode = True
