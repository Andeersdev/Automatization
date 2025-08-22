
import os
import json
from typing import List, Dict
from src.database import db
from src.interfaces.task import Task, TaskCreate
from src.shared.enums.status_code import StatusCode

class TaskRepository:

    @staticmethod
    async def get_all_tasks() -> List[str]:
        query = ''' SELECT * FROM funcs_get_all_tasks() '''
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_active_tasks() -> List[str]:
        query = ''' SELECT * FROM funcs_get_active_tasks() '''
        return await db.execute_query_return_data(query)

    @staticmethod
    async def get_task_by_id(task_id: str) -> str:
        query = ''' SELECT * FROM funcs_get_task_by_id(:taskId) '''
        params = {'taskId': task_id}
        return await db.execute_query_return_data(query, params, fetchone=True)

    @staticmethod
    async def create_task(data: TaskCreate) -> str:
        query = ' SELECT * FROM funcs_create_task( :userId, :taskTypeId, :name, :description, :status '
        params = {
            'userId': data.user_id, 
            'taskTypeId': data.task_type_id, 
            'name': data.name, 
            'description': data.description, 
            'status': data.status
        }
        if data.email_task and data.email_task.email_task_id:
            query += ', :emailTaskId, :subject, :body, :recipientEmail, :scheduledTime, :emailTaskStatus'
            params.update({
                'emailTaskId': data.email_task.email_task_id, 
                'subject': data.email_task.subject, 
                'body': data.email_task.body, 
                'recipientEmail': data.email_task.recipient_email, 
                'scheduledTime': data.email_task.scheduled_time,
                'emailTaskStatus': data.email_task.status
            })
        if data.scraping_task and data.scraping_task.scraping_config_id:
            # query += ', :scrapingConfigId, :url, :method, :headers, :payload, :selectors'
            query += ', :scrapingConfigId, :url, :method::scrapingmethodenum, :headers::json, :payload::json, :selectors::json'

            params.update({
                'scrapingConfigId': data.scraping_task.scraping_config_id,
                'url': data.scraping_task.url,
                'method': data.scraping_task.method,
                'headers': json.dumps(data.scraping_task.headers),
                'payload': json.dumps(data.scraping_task.payload),
                'selectors': json.dumps(data.scraping_task.selectors)
            })
        query += ')'
        print(f'query: {query}')
        print(f'params: {params}')
        return await db.execute_query_return_message(query, params, StatusCode.CREATE_TASK_CODE)

    @staticmethod
    async def update_task(task_id: str, data: Task) -> str:
        query = ''' SELECT * FROM funcs_update_task(:taskTypeId, :name, :description, :status, :isActive) '''
        params = {
            'taskId': task_id,
            'taskTypeId': task_type_id,
            'type': data.type,
            'status': data.status,
            'isActive': data.is_active
        }
        return await db.execute_query_return_message(query, params, StatusCode.UPDATE_TASK_CODE)

    @staticmethod
    async def delete_task(task_id: str) -> str:
        query = ''' SELECT * FROM funcs_delete_task(:taskId) '''
        params = {'taskId': task_id}
        return await db.execute_query_return_message(query, params, StatusCode.DELETE_TASK_CODE)