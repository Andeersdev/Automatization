from fastapi import APIRouter, Request
from src.controllers.task_controller import TaskController
from src.interfaces.task import Task, TaskCreate

task_router = APIRouter(prefix='/tasks', tags=['tasks'])

controller = TaskController()

@task_router.get('/')
async def get_all_tasks():
    return await controller.get_all_tasks()

@task_router.get('/actives')
async def get_active_tasks():
    return await controller.get_active_tasks()

@task_router.get('/{task_id}')
async def get_task_by_id(task_id: str):
    return await controller.get_task_by_id(task_id)

@task_router.post('/')
async def create_task(request:TaskCreate):
    return await controller.create_task(request)

@task_router.put('/{task_id}')
async def update_task(task_id:str, request:Task):
    return await controller.update_task(task_id, request)


@task_router.delete('/{task_id}')
async def delete_task(task_id:str):
    return await controller.delete_task(task_type_id)