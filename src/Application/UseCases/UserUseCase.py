import json
from typing import Dict
from src.Domain.Ports.Primary.UserInput import UserInput
from src.Infrastructure.Repositories.UserRepository import UserRepository
from src.Shared.Helpers.DecryptedRequest import process_encrypted_data
from src.Shared.Helpers.Sha512 import SHA512
from src.Shared.Helpers.Instances import aes
from src.Infrastructure.Requests.UserRequest import User

class UserUseCase(UserInput):

    def __init__(self):
        self.repository = UserRepository()

    @process_encrypted_data()
    async def get_all_users(self, **kwargs) -> str:
        return aes.encrypt(os.getenv('AES_KEY'), await self.repository.get_all_users())

    @process_encrypted_data()
    async def get_user_by_id(self, data:Dict[str,str], **kwargs) -> str:
        return aes.encrypt(os.getenv('AES_KEY'), await self.repository.get_user_by_id(data['id']))

    @process_encrypted_data(User)
    async def create_user(self, data:User, **kwargs) -> str:
        data.password = SHA512.hash_password(data.password)
        return await self.repository.create_user(data)

    @process_encrypted_data(User)
    async def update_user(self, data:User, **kwargs) -> str:
        return await self.repository.update_user(data)

    @process_encrypted_data()
    async def delete_user(self, data:Dict[str,str], **kwargs) -> str:
        return await self.repository.delete_user(data['id'])