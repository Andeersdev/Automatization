import os
import json
from typing import List, Dict
from uuid import UUID
from src.Domain.Ports.Secondary.RoleOutput import RoleOutput
from src.Infrastructure.Requests.RoleRequest import Role
from src.Domain.Entities.Role import Role
from src.Shared.Helpers.Instances import db

class RoleRepository(RoleOutput):
    
    @staticmethod
    async def get_all_roles() -> List[Role]:
        query = 'SELECT * FROM funcs_get_all_roles()'
        data = await db.execute_query_return_data(query)
        return [Role(**item).model_dump() for item in data]

    @staticmethod
    async def get_active_roles() -> List[Role]:
        query = 'SELECT * FROM funcs_get_active_roles()'
        data = await db.execute_query_return_data(query)
        return [Role(**item).model_dump() for item in data]

    @staticmethod
    async def get_role_by_id(role_id:UUID) -> Role:
        query = 'SELECT * FROM funcs_get_role_by_id(:roleId)'
        params = {'roleId': role_id}
        data = await db.execute_query_return_data(query, params, fetchone=True)
        return Role(**data).model_dump() if data else None

    @staticmethod
    async def create_role(data:Role) -> str:
        query = '''
        SELECT * FROM funcs_create_role(
            :roleName,
            :abbreviation
        )
        '''
        params = {
            'roleName': data.roleName,
            'abbreviation': data.abbreviation
        }
        return await db.execute_query_return_message(query, params, 'DB_1103')

    @staticmethod
    async def update_role(role_id:UUID, data:Role) -> str:
        query = '''
        SELECT * FROM funcs_update_role(
            :roleId,
            :roleName,
            :abbreviation,
            :status
        )
        '''
        params = {
            'roleId': role_id,
            'roleName': data.roleName,
            'abbreviation': data.abbreviation,
            'status': data.status
        }
        return await db.execute_query_return_message(query, params, 'DB_1104')

    @staticmethod
    async def delete_role(role_id:UUID) -> str:
        query = 'SELECT * FROM funcs_delete_role(:roleId)'
        params = {'roleId': role_id}
        return await db.execute_query_return_message(query, params, 'DB_1105')