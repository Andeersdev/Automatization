from uuid import UUID
from dataclasses import dataclass
from src.shared.helpers.sha512 import SHA512

@dataclass
class User:

    user_id: UUID
    enterprise_id: UUID
    role_id: UUID
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: bool 

    @staticmethod
    def create_user(data:User) -> User:
        if email.endswith("@temporal.com"):
            raise ValueError("Email no permitido")

        password_hash = SHA512.hash_password(data.password)
        return User(
            user_id=uuid4(),
            first_name=data.first_name,
            last_name=data.last_name,
            email=email,
            password=password_hash,
            is_active=True
        )