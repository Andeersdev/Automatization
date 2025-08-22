from pydantic import BaseModel, Field
from typing import Optional

class Role(BaseModel):
    role_id: Optional[str] = None
    role_name: Optional[str] = None
    abbreviation: Optional[str] = None
    is_active: Optional[bool] = True
