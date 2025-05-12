from src.Application.UseCases.EnterpriseUseCase import EnterpriseUseCase

use_case = EnterpriseUseCase()

class EnterpriseResolver:

    @staticmethod
    async def resolve_get_all_enterprises(_, info):
        response = await use_case.get_all_enterprises()
        return {
            'status': 'DB_SUCCESS_001',
            'message': 'Proccess Success',
            'data': response
        }