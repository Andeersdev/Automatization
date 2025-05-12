from src.Application.UseCases.AuthUseCase import AuthUseCase

use_case = AuthUseCase()

class AuthResolver:

    @staticmethod
    async def resolve_login(_, info, data):
        response = await use_case.login(data)
        return {
            'status': 'DB_SUCCESS_001',
            'message': 'Login Success',
            'data': response
        }