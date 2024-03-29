from pydantic import UUID4, BaseModel


class AdminSchema(BaseModel):
    id: UUID4
    name: str
    last_name: str
    admin_type_id: str
    user_id: str

    class Config:
        orm_mode = True


class AdminSchemaIn(BaseModel):
    name: str
    last_name: str
    user_id: str
    admin_type_id: str

    class Config:
        orm_mode = True


class AdminSchemaUpdate(BaseModel):
    id: str
    name: str
    last_name: str
    admin_type_id: str

    class Config:
        orm_mode = True
