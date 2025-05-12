from src.Application.UseCases.UserUseCase import UserUseCase

use_case = UserUseCase()

class UserResolver:

    @staticmethod
    async def resolve_get_all_users(_, info):
        response = await use_case.get_all_users()
        return {
            'status': 'DB_SUCCESS_001',
            'message': 'Proccess Success',
            'data': response
        }

    @staticmethod
    async def resolve_create_user(_, info, data):
        response = await use_case.create_user(data)
        return {
            'status': 'DB_1100',
            'message': response,
            'data': None
        }