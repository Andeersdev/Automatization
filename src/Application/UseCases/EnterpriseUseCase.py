import os
import json
from dotenv import load_dotenv
from src.Domain.Ports.Primary.EnterpriseInput import EnterpriseInput
from src.Infrastructure.Repositories.EnterpriseRepository import EnterpriseRepository
from src.Shared.Helpers.Aes import AES

load_dotenv(dotenv_path='.env', override=True)

class EnterpriseUseCase(EnterpriseInput):

    def __init__(self):
        self.repository = EnterpriseRepository()
        self.aes = AES()

    async def get_all_enterprises(self):
        return self.aes.encrypt(os.getenv('AES_KEY'), await self.repository.get_all_enterprises())

    async def get_active_enterprises(self): ...

    async def get_enterprise_by_id(self, enterprise_id): ...

    async def create_enterprise(self, data): ...

    async def update_enterprise(self, enterprise_id, data): ...


    async def delete_enterprise(self, enterprise_id): ...