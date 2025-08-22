import os
import json
from typing import List, Dict
from src.database import db
from src.interfaces.role import Role
from src.shared.enums.status_code import StatusCode

class RoleRepository:

    @staticmethod
    async def get_all_roles() -> List[str]:
        query = 'SELECT * FROM funcs_get_all_roles()'
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_active_roles() -> List[str]:
        query = 'SELECT * FROM funcs_get_active_roles()'
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_role_by_id(role_id:str) -> str:
        query = 'SELECT * FROM funcs_get_role_by_id(:roleId)'
        params = {'roleId': role_id}
        return await db.execute_query_return_data(query, params, fetchone=True)

    @staticmethod
    async def create_role(data:Role) -> str:
        query = '''
        SELECT * FROM funcs_create_role(
            :roleName,
            :abbreviation
        )
        '''
        params = {
            'roleName': data.role_name,
            'abbreviation': data.abbreviation
        }
        return await db.execute_query_return_message(query, params, StatusCode.CREATE_ROLE_CODE)

    @staticmethod
    async def update_role(role_id, data:Role) -> str:
        query = '''
        SELECT * FROM funcs_update_role(
            :roleId,
            :roleName,
            :status
        )
        '''
        params = {
            'roleId': role_id,
            'roleName': data.role_name,
            'status': data.is_active
        }
        return await db.execute_query_return_message(query, params, StatusCode.UPDATE_ROLE_CODE)

    @staticmethod
    async def delete_role(role_id:str) -> str:
        query = 'SELECT * FROM funcs_delete_role(:roleId)'
        params = {'roleId': role_id}
        return await db.execute_query_return_message(query, params, StatusCode.DELETE_ROLE_CODE)