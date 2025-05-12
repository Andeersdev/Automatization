import json
from uuid import UUID
from src.Domain.Ports.Secondary.UserOutput import UserOutput
from src.Infrastructure.Requests.UserRequest import User
from src.Shared.Helpers.Instances import db

class UserRepository(UserOutput):

    @staticmethod
    async def get_all_users() -> str:
        query = 'SELECT * FROM funcs_get_all_users()'
        return json.dumps(await db.execute_query_return_data(query), default=str)

    async def create_user(self, data:User) -> str:
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
            'enterpriseId': data.enterpriseId,
            'roleId': data.roleId,
            'firstName': data.firstName,
            'lastName': data.lastName,
            'email': data.email,
            'password': data.password
        }
        return await db.execute_query_return_message(query, params, 'DB_1100')
    
    @staticmethod
    async def get_user_by_id(user_id: str) -> str:
        query = 'SELECT * FROM funcs_get_user_by_id(:userId)'
        params = {'userId': user_id}
        return json.dumps(await db.execute_query_return_data(query, params, fetchone=True), default=str)

    @staticmethod
    async def update_user(user_id:UUID, data:User) -> str:
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
            'enterpriseId': data.enterpriseId,
            'roleId': data.roleId,
            'firstName': data.firstName,
            'lastName': data.lastName,
            'isActive': data.isActive
        }
        return await db.execute_query_return_message(query, params, 'DB_1101')

    @staticmethod
    async def delete_user(user_id:UUID) -> str:
        query = 'SELECT * FROM funcs_delete_user(:userId)'
        params = {'userId': user_id}
        return await db.execute_query_return_message(query, params, 'DB_1102')
    
    