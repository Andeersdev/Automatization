import json
from typing import Dict
from src.repositories.task_type_repository import TaskTypeRepository
from src.interfaces.task_type import TaskType

class TaskTypeController:

    async def get_all_tasks_type(self) -> str:
        return await TaskTypeRepository.get_all_tasks_type()

    async def get_active_tasks_type(self) -> str:
        return await TaskTypeRepository.get_active_tasks_type()

    async def get_task_type_by_id(self, task_type_id: str) -> str:
        return await TaskTypeRepository.get_task_type_by_id(task_type_id)

    async def create_task_type(self, data: TaskType) -> str:
        return await TaskTypeRepository.create_task_type(data)

    async def update_task_type(self, task_type_id: str, data: TaskType) -> str:
        return await TaskTypeRepository.update_task_type(task_type_id, data)

    async def delete_task_type(self, task_type_id: str) -> str:
        return await TaskTypeRepository.delete_task_type(task_type_id)

    