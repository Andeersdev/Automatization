from abc import ABC, abstractmethod
from typing import Dict
from uuid import UUID

class RoleOutput(ABC):

    @abstractmethod
    async def get_all_roles(self) -> str: ...

    @abstractmethod
    async def get_active_roles(self) -> str: ...

    @abstractmethod
    async def get_role_by_id(self, role_id:UUID) -> str: ...

    @abstractmethod
    async def create_role(self, data:Dict[str,str]) -> str: ...

    @abstractmethod
    async def update_role(self, role_id:UUID, data:Dict[str,str]) -> str: ...

    @abstractmethod
    async def delete_role(self, role_id:UUID) -> str: ...