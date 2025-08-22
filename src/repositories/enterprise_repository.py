from typing import List, Dict
from src.database import db
from src.interfaces.enterprise import Enterprise
from src.shared.enums.status_code import StatusCode

class EnterpriseRepository:

    @staticmethod
    async def get_all_enterprises() -> List[Dict[str,str]]:
        query = 'SELECT * FROM funcs_get_all_enterprises()'
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_active_enterprises() -> List[Dict[str,str]]:
        query = 'SELECT * FROM funcs_get_active_enterprises()'
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_enterprise_by_id(enterprise_id: str) -> Dict[str,str]:
        query = 'SELECT * FROM funcs_get_enterprise_by_id(:enterpriseId)'
        params = {'enterpriseId': enterprise_id}
        return await db.execute_query_return_data(query, params)

    @staticmethod
    async def create_enterprise(data: Enterprise) -> str:
        query = 'SELECT * FROM funcs_create_enterprise(:enterpriseName, :email, :phone, :address)'
        params = {
            'enterpriseName': data.enterprise_name,
            'email': data.email,
            'phone': data.phone,
            'address': data.address
        }
        return await db.execute_query_return_message(query, params, StatusCode.CREATE_ENTERPRISE_CODE)

    @staticmethod
    async def update_enterprise(enterprise_id: str, data: Enterprise) -> str:
        query = '''SELECT * FROM funcs_update_enterprise
        (
            :enterpriseId, :enterpriseName, :phone, :address, :status
        )
        '''
        params = {
            'enterpriseId': enterprise_id,
            'enterpriseName': data.enterprise_name,
            'phone': data.phone,
            'address': data.address,
            'status': data.is_active
        }
        return await db.execute_query_return_message(query, params, StatusCode.UPDATE_ENTERPRISE_CODE)
    
    @staticmethod
    async def delete_enterprise(enterprise_id: str) -> str:
        query = 'SELECT * FROM funcs_delete_enterprise(:enterpriseId)'
        params = {'enterpriseId': enterprise_id}
        return await db.execute_query_return_message(query, params, StatusCode.DELETE_ENTERPRISE_CODE)