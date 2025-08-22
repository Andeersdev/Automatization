from fastapi import APIRouter
from src.controllers.enterprise_controller import EnterpriseController
from src.interfaces.enterprise import Enterprise

enterprise_router = APIRouter(prefix='/enterprises', tags=['enterprises'])

controller = EnterpriseController()

@enterprise_router.get('/')
async def get_all_enterprises():
    return await controller.get_all_enterprises()

@enterprise_router.get('/actives')
async def get_active_enterprises():
    return await controller.get_active_enterprises()

@enterprise_router.get('/{enterprise_id}')
async def get_enterprise_by_id(enterprise_id: str):
    return await controller.get_enterprise_by_id(enterprise_id)

@enterprise_router.post('/')
async def create_enterprise(request:Enterprise):
    return await controller.create_enterprise(role)

@enterprise_router.put('/{enterprise_id}')
async def update_enterprise(enterprise_id:str, request:Enterprise):
    return await controller.update_enterprise(enterprise_id, request)

@enterprise_router.delete('/{enterprise_id}')
async def delete_enterprise(enterprise_id:str):
    return await controller.delete_enterprise(enterprise_id)