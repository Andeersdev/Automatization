import os
import json
from typing import Dict
from dotenv import load_dotenv
from src.Shared.Helpers.Aes import AES
from src.Domain.Ports.Primary.RoleInput import RoleInput
from src.Infrastructure.Repositories.RoleRepository import RoleRepository
from src.Shared.Helpers.DecryptedRequest import process_encrypted_data
from src.Infrastructure.Requests.RoleRequest import Role

load_dotenv(dotenv_path='.env', override=True)

class RoleUseCase(RoleInput):

    def __init__(self):
        self.repository = RoleRepository()
        self.aes = AES()

    @process_encrypted_data()
    async def get_all_roles(self, **kwargs) -> str:
        roles = await self.repository.get_all_roles()
        return self.aes.encrypt(os.getenv('AES_KEY'), json.dumps(roles, default=str))

    @process_encrypted_data()
    async def get_active_roles(self, **kwargs) -> str:
        roles = await self.repository.get_active_roles()
        return self.aes.encrypt(os.getenv('AES_KEY'), json.dumps(roles, default=str))

    @process_encrypted_data()
    async def get_role_by_id(self, data:Dict[str,str], **kwargs) -> str:
        role_found = await self.repository.get_role_by_id(data.get('roleId'))
        return self.aes.encrypt(os.getenv('AES_KEY'), json.dumps(role_found, default=str))

    @process_encrypted_data(Role)
    async def create_role(self, data:Dict[str,str], **kwargs) -> str:
        return await self.repository.create_role(data)

    @process_encrypted_data(Role)
    async def update_role(self, data:Dict[str,str], **kwargs) -> str:
        return await self.repository.update_role(data)

    @process_encrypted_data()
    async def delete_role(self, data:Dict[str,str], **kwargs) -> str:
        return await self.repository.delete_role(data['roleId'])

    