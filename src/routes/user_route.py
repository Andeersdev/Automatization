from fastapi import APIRouter
from src.controllers.user_controller import UserController
from src.interfaces.user import User

user_router = APIRouter(prefix='/users', tags=['users'])

controller = UserController()

@user_router.get('/')
async def get_all_users():
    return await controller.get_all_users()

@user_router.get('/actives')
async def get_active_users():
    return await controller.get_active_users()

@user_router.get('/{user_id}')
async def get_user_by_id(user_id: str):
    return await controller.get_user_by_id(user_id)

@user_router.post('/')
async def create_user(request:User):
    return await controller.create_user(request)

@user_router.put('/{user_id}')
async def update_user(user_id:str, request:User):
    return await controller.update_user(user_id, request)

@user_router.delete('/{user_id}')
async def delete_user(user_id:str):
    return await controller.delete_user(user_id)