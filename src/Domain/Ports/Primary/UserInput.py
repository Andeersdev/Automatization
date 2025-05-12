from abc import ABC, abstractmethod
from typing import Dict
from uuid import UUID

class UserInput(ABC):

    @abstractmethod
    async def get_all_users(self) -> str: ...

    @abstractmethod
    async def create_user(self, data:Dict[str,str]) -> str: ...

    @abstractmethod
    async def get_user_by_id(self, user_id:UUID) -> str: ...

    @abstractmethod
    async def update_user(self, user_id:UUID, data:Dict[str,str]) -> str: ...

    @abstractmethod
    async def delete_user(self, user_id:UUID) -> str: ...

