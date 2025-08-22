from .base import CamelMode
from typing import Optional

class User(CamelMode):
    user_id: Optional[str] = None
    enterprise_id: Optional[str] = None
    role_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = True
