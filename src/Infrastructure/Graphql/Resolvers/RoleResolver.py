from src.Application.UseCases.RoleUseCase import RoleUseCase

use_case = RoleUseCase()

class RoleResolver:

    @staticmethod
    async def resolve_get_all_roles(_, info):
        response = await use_case.get_all_roles()
        return {
            'status': 'DB_SUCCESS_001',
            'message': 'Proccess Success',
            'data': response
        }

    
    @staticmethod
    async def resolve_get_role_by_id(_, info, data):
        params = {'aes_data': data}
        response = await use_case.get_role_by_id(**params)
        return {
            'status': 'DB_SUCCESS_001',
            'message': 'Proccess Success',
            'data': response
        }