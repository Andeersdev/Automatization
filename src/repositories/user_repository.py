from typing import List, Dict
from src.interfaces.user import User
from src.database import db
from src.shared.enums.status_code import StatusCode

class UserRepository:

    @staticmethod
    async def get_all_users() -> List[Dict[str,str]]:
        query = 'SELECT * FROM funcs_get_all_users()'
        return await db.execute_query_return_data(query)


    @staticmethod
    async def get_active_users() -> List[Dict[str,str]]:
        query = 'SELECT * FROM funcs_get_active_users()'
        return await db.execute_query_return_data(query)


    @staticmethod
    async def get_user_by_id(user_id: str) -> Dict[str,str]:
        query = 'SELECT * FROM funcs_get_user_by_id(:userId)'
        params = {'userId': user_id}
        return await db.execute_query_return_data(query, params, fetchone=True)


    @staticmethod
    async def create_user(data: User) -> str:
        query = '''
        SELECT * FROM funcs_create_user(
            :enterpriseId,
            :roleId,
            :firstName, 
            :lastName, 
            :email,
            :password
        )
        '''
        params = {
            'enterpriseId': data.enterprise_id,
            'roleId': data.role_id,
            'firstName': data.first_name,
            'lastName': data.last_name,
            'email': data.email,
            'password': data.password
        }
        return await db.execute_query_return_message(query, params, StatusCode.CREATE_USER_CODE)
    
    
    @staticmethod
    async def update_user(user_id: str, data: User) -> str:
        query = '''
        SELECT * FROM funcs_update_user(
            :userId,
            :enterpriseId,
            :roleId,
            :firstName, 
            :lastName,
            :isActive
        )
        '''
        params = {
            'userId': user_id,
            'enterpriseId': data.enterprise_id,
            'roleId': data.role_id,
            'firstName': data.first_name,
            'lastName': data.last_name,
            'isActive': data.is_active
        }
        return await db.execute_query_return_message(query, params, StatusCode.UPDATE_USER_CODE)

    @staticmethod
    async def delete_user(user_id: str) -> str:
        print(f'user_id: {user_id}')
        query = 'SELECT * FROM funcs_delete_user(:userId)'
        params = {'userId': user_id}
        return await db.execute_query_return_message(query, params, StatusCode.DELETE_USER_CODE)
    
    