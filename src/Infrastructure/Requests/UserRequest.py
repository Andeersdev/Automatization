from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class User(BaseModel):
    userId: Optional[UUID] = None
    enterpriseId: UUID
    roleId: UUID
    firstName: str
    lastName: str
    email: Optional[str] = None
    password: Optional[str] = None
    isActive: Optional[bool] = True