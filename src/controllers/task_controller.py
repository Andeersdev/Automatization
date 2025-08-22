import json
from typing import Dict
from src.repositories.task_repository import TaskRepository
from src.interfaces.task import Task, TaskCreate

class TaskController:

    async def get_all_tasks(self) -> str:
        return await TaskRepository.get_all_tasks()

    async def get_active_tasks(self) -> str:
        return await TaskRepository.get_active_tasks()

    async def get_task_by_id(self, task_type_id: str) -> str:
        return await TaskRepository.get_task_by_id(task_type_id)

    async def create_task(self, data: TaskCreate) -> str:
        return await TaskRepository.create_task(data)

    async def update_task(self, task_type_id: str, data: Task) -> str:
        return await TaskRepository.update_task(task_type_id, data)

    async def delete_task(self, task_type_id: str) -> str:
        return await TaskRepository.delete_task(task_type_id)

    