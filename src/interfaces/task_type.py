from pydantic import BaseModel
from typing import Optional

class TaskType(BaseModel):
    type: str
    is_active: Optional[bool] = True