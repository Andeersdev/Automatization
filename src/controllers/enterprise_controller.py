import json
from typing import Dict
from src.repositories.enterprise_repository import EnterpriseRepository
from src.interfaces.enterprise import Enterprise

class EnterpriseController:

    async def get_all_enterprises(self) -> str:
        return await EnterpriseRepository.get_all_enterprises()

    async def get_active_enterprises(self) -> str:
        return await EnterpriseRepository.get_active_enterprises()

    async def get_enterprise_by_id(self, enterprise_id: str) -> str:
        return await EnterpriseRepository.get_enterprise_by_id(enterprise_id)

    async def create_enterprise(self, data: Enterprise) -> str:
        return await EnterpriseRepository.create_enterprise(data)

    async def update_enterprise(self, data: Enterprise) -> str:
        return await EnterpriseRepository.update_enterprise(data)

    async def delete_enterprise(self, enterprise_id: str) -> str:
        return await EnterpriseRepository.delete_enterprise(enterprise_id)