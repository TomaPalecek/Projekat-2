from pydantic import UUID4, BaseModel


class AdminTypeSchema(BaseModel):
    id: UUID4
    admin_type: str

    class Config:
        orm_mode = True


class AdminTypeSchemaIn(BaseModel):
    admin_type: str

    class Config:
        orm_mode = True
