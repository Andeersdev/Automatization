import os
from typing import Dict
from src.Domain.Ports.Secondary.AuthOutput import AuthOutput
from src.Infrastructure.Database.Connection import Connection

class AuthRepository(AuthOutput):

    def __init__(self):
        self.db = Connection(os.getenv('DATABASE_URL'))


    async def login(self, email:str, password:str) -> Dict[str,str]:
        query = 'SELECT * FROM funcs_login(:email, :password)'
        params = {
            'email': email,
            'password': password
        }
        return await self.db.execute_query_return_data(query, params, fetchone=True)

