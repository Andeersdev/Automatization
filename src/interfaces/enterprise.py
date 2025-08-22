from pydantic import BaseModel, Field
from typing import Optional

class Enterprise(BaseModel):
    enteprise_id: Optional[str] = None
    enterprise_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = True
