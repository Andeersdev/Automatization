import os
import json
from uuid import UUID
from src.Domain.Ports.Secondary.EnterpriseOutput import EnterpriseOutput
from src.Infrastructure.Database.Connection import Connection
from src.Infrastructure.Requests.EnterpriseRequest import Enterprise

class EnterpriseRepository(EnterpriseOutput):

    def __init__(self):
        self.db = Connection(os.getenv('DATABASE_URL'))

    async def get_all_enterprises(self) -> str:
        query = 'SELECT * FROM funcs_get_enterprises()'
        return json.dumps(await self.db.execute_query_return_data(query), default=str)

    async def get_active_enterprises(self) -> str:
        query = 'SELECT * FROM funcs_get_active_enterprises()'
        return json.dumps(await self.db.execute_query_return_data(query), default=str)

    async def get_enterprise_by_id(self, enterprise_id:UUID) -> str:
        query = 'SELECT * FROM funcs_get_enterprise_by_id(:enterpriseId)'
        params = {'enterpriseId': enterprise_id}
        return json.dumps(await self.db.execute_query_return_data(query, params), default=str)

    async def create_enterprise(self, data:Enterprise) -> str:
        query = 'SELECT * FROM funcs_create_enterprise(:name, :description, :address, :phone, :email)'
        params = {
            'name': data.name,
            'description': data.description,
            'address': data.address,
            'phone': data.phone,
            'email': data.email
        }
        return await self.db.execute_query_return_message(query, params, 'DB_1006')

    async def update_enterprise(self, data:Enterprise) -> str:
        query = 'SELECT * FROM funcs_update_enterprise(:enterpriseId, :name, :description, :address, :phone, :email)'
        params = {
            'enterpriseId': data.enterprise_id,
            'name': data.name,
            'description': data.description,
            'address': data.address,
            'phone': data.phone,
            'email': data.email
        }
        return await self.db.execute_query_return_message(query, params, 'DB_1007')
    
    async def delete_enterprise(self, enterprise_id:UUID) -> str:
        query = 'SELECT * FROM funcs_delete_enterprise(:enterpriseId)'
        params = {'enterpriseId': enterprise_id}
        return await self.db.execute_query_return_message(query, params, 'DB_1008')