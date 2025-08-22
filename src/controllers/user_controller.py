import json
from typing import Dict
from src.repositories.user_repository import UserRepository
from src.shared.helpers.sha512 import SHA512
from src.interfaces.user import User

class UserController:

    async def get_all_users(self) -> str:
        return await UserRepository.get_all_users()

    async def get_active_users(self) -> str:
        return await UserRepository.get_active_users()

    async def get_user_by_id(self, user_id: str) -> str:
        return await UserRepository.get_user_by_id(user_id)

    async def create_user(self, data: User) -> str:
        print(f'data user: {data}')
        data.password = SHA512.hash_password(data.password)
        return await UserRepository.create_user(data)

    async def update_user(self, user_id: str, data: User) -> str:
        return await UserRepository.update_user(user_id, data)

    async def delete_user(self, user_id: str) -> str:
        return await UserRepository.delete_user(user_id)