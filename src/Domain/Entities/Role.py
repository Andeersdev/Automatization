from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Role(BaseModel):
    roleId: Optional[UUID] = None
    roleName: str
    abbreviation: Optional[str] = None
    status: Optional[bool | str] = True
    createdAt: Optional[str] = None