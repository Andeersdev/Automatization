from fastapi import APIRouter, Request
from src.controllers.task_type_controller import TaskTypeController
from src.interfaces.task_type import TaskType

task_type_router = APIRouter(prefix='/task-types', tags=['task-types'])

controller = TaskTypeController()

@task_type_router.get('/')
async def get_all_tasks_type():
    return await controller.get_all_tasks_type()

@task_type_router.get('/actives')
async def get_active_tasks_type():
    return await controller.get_active_tasks_type()

@task_type_router.get('/{task_type_id}')
async def get_task_type_by_id(task_type_id: str):
    return await controller.get_task_type_by_id(task_type_id)

@task_type_router.post('/')
async def create_task_type(request:TaskType):
    return await controller.create_task_type(request)

@task_type_router.put('/{task_type_id}')
async def update_task_type(task_type_id:str, request:TaskType):
    return await controller.update_task_type(task_type_id, request)


@task_type_router.delete('/{task_type_id}')
async def delete_task_type(task_type_id:str):
    return await controller.delete_task_type(task_type_id)