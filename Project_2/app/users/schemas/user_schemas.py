from pydantic import UUID4, BaseModel, EmailStr


class UserSchema(BaseModel):
    id: UUID4
    email: str
    password: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaUpdate(BaseModel):
    id: str
    is_active: bool

    class Config:
        orm_mode = True
