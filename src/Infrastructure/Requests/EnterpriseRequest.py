from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Enterprise(BaseModel):
    entepriseId: Optional[UUID] = None
    enterpriseName: str
    email: Optional[str] = None
    phone: str
    address: str
    isActive: Optional[bool] = True