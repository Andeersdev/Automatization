import json
from datetime import datetime
from src.repositories.auth_repository import AuthRepository
from src.interfaces.auth import Login, Logout
from src.shared.helpers.config_system import ConfigSystem
from src.shared.helpers.jwt import JWT
from src.shared.helpers.sha512 import SHA512
from src.database import db

class AuthController:

    def __init__(self):
        self.repository = AuthRepository()
        self.jwt = JWT()

    async def login(self, data: Login) :
        async with (await db.get_session()) as session:
            async with session.begin():
                data = await self.repository.login(session, data.email, SHA512.hash_password(data.password))
                config = await ConfigSystem.get_config_system(data.get('enterpriseId'))
                token_exp = datetime.now() + config.get('tokenExpirationInterval')
                token = self.jwt.create_access_token(data, token_exp)
                await self.repository.insert_auth_token(session, data.get('userId'), token, token_exp)
                return {
                    'token': token,
                    'tokenExp': token_exp
                }
        
    async def logout(self, data: Logout):
        await self.repository.logout(data.userId)