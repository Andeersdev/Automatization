from abc import ABC, abstractmethod
from typing import Dict
from uuid import UUID

class EnterpriseOutput(ABC):

    @abstractmethod
    async def get_all_enterprises(self) -> str: ...

    @abstractmethod
    async def get_active_enterprises(self) -> str: ...

    @abstractmethod
    async def get_enterprise_by_id(self, enterprise_id:UUID) -> str: ...

    @abstractmethod
    async def create_enterprise(self, data:Dict[str,str]) -> str: ...

    @abstractmethod
    async def update_enterprise(self, enterprise_id:UUID, data:Dict[str,str]) -> str: ...

    @abstractmethod
    async def delete_enterprise(self, enterprise_id:UUID) -> str: ...
