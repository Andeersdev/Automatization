import json
from src.Infrastructure.Repositories.AuthRepository import AuthRepository
from src.Shared.Helpers.Sha512 import SHA512

class AuthUseCase:

    def __init__(self):
        self.repository = AuthRepository()

    async def login(self, data):
        response = await self.repository.login(data.email, SHA512.hash_password(data.password))
        print(f'response: {response}')
        return json.dumps(response)