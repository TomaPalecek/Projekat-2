from pydantic import UUID4, BaseModel


class CategorySchema(BaseModel):
    id: UUID4
    category: str

    class Config:
        orm_mode = True


class CategorySchemaIn(BaseModel):
    category: str

    class Config:
        orm_mode = True


class CategorySchemaUpdate(BaseModel):
    id: str
    category: str

    class Config:
        orm_mode = True
