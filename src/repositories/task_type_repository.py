import os
import json
from typing import List, Dict
from src.database import db
from src.interfaces.task_type import TaskType
from src.shared.enums.status_code import StatusCode

class TaskTypeRepository:

    @staticmethod
    async def get_all_tasks_type() -> List[str]:
        query = ''' SELECT * FROM funcs_get_all_tasks_type() '''
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_active_tasks_type() -> List[str]:
        query = ''' SELECT * FROM funcs_get_active_tasks_type() '''
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_task_type_by_id(task_type_id:str) -> str:
        query = ''' SELECT * FROM funcs_get_task_type_by_id(:taskTypeId) '''
        params = {'taskTypeId': task_type_id}
        return await db.execute_query_return_data(query, params, fetchone=True)

    @staticmethod
    async def create_task_type(data:TaskType) -> str:
        query = ''' SELECT * FROM funcs_create_task_type(:type) '''
        params = {
            'type': data.type
        }
        return await db.execute_query_return_message(query, params, StatusCode.CREATE_TASK_TYPE_CODE)

    @staticmethod
    async def update_task_type(task_type_id, data:TaskType) -> str:
        query = '''
        SELECT * FROM funcs_update_task_type(
            :taskTypeId,
            :type,
            :status
        )
        '''
        params = {
            'taskTypeId': task_type_id,
            'type': data.type,
            'status': data.is_active
        }
        return await db.execute_query_return_message(query, params, StatusCode.UPDATE_TASK_TYPE_CODE)

    @staticmethod
    async def delete_task_type(task_type_id:str) -> str:
        query = ''' SELECT * FROM funcs_delete_task_type(:taskTypeId) '''
        params = {'taskTypeId': task_type_id}
        return await db.execute_query_return_message(query, params, StatusCode.DELETE_TASK_TYPE_CODE)