from pydantic import BaseModel
from uuid import UUID

class Login(BaseModel):
    email: str
    password: str

class ForgotPassword(BaseModel):
    email: str

class ChangePassword(BaseModel):
    email: str
    password: str
    new_password: str

class Logout(BaseModel):
    userId: UUID