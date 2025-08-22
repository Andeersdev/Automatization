from fastapi import APIRouter, Request
from src.controllers.role_controller import RoleController
from src.interfaces.role import Role

role_router = APIRouter(prefix='/roles', tags=['roles'])

controller = RoleController()

@role_router.get('/')
async def get_all_roles():
    return await controller.get_all_roles()

@role_router.get('/actives')
async def get_active_roles():
    return await controller.get_active_roles()

@role_router.get('/{role_id}')
async def get_role_by_id(role_id: str):
    return await controller.get_role_by_id(role_id)

@role_router.post('/')
async def create_role(request:Role):
    return await controller.create_role(role)

@role_router.put('/{role_id}')
async def update_role(role_id:str, request:Role):
    return await controller.update_role(role_id, request)


@role_router.delete('/{role_id}')
async def delete_role(role_id:str):
    return await controller.delete_role(role_id)