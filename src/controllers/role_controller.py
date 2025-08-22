import json
from typing import Dict
from src.repositories.role_repository import RoleRepository
from src.interfaces.role import Role

class RoleController:


    async def get_all_roles(self) -> str:
        return await RoleRepository.get_all_roles()

    async def get_active_roles(self) -> str:
        return await RoleRepository.get_active_roles()

    async def get_role_by_id(self, role_id: str) -> str:
        return await RoleRepository.get_role_by_id(role_id)

    async def create_role(self, data: Role) -> str:
        return await RoleRepository.create_role(data)

    async def update_role(self, role_id: str, data:Role) -> str:
        return await RoleRepository.update_role(role_id, data)

    async def delete_role(self, role_id: str) -> str:
        return await RoleRepository.delete_role(role_id)

    