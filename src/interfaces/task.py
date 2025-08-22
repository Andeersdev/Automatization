from enum import StrEnum
from datetime import datetime
from uuid import uuid4
from typing import Optional, Any
from pydantic import Json
from .base import CamelMode

class TaskStatusEnum(StrEnum):
    pending = 'pending'
    in_progress = 'in_progress' 
    completed = 'completed'
    failed = 'failed'

class EmailTaskStatusEnum(StrEnum):
    pending = 'pending' 
    sent = 'sent' 
    failed = 'failed'

class ScrapingMethodEnum(StrEnum):
    post = 'POST'
    get = 'GET'

class EmailTask(CamelMode):
    subject: str
    body: str
    recipient_email: str
    scheduled_time: datetime
    status: Optional[EmailTaskStatusEnum] = EmailTaskStatusEnum.pending
    email_task_id: Optional[str] = str(uuid4())

class ScrapingTask(CamelMode):
    url: str
    headers: Json[Any]
    payload: Json[Any]
    selectors: Json[Any]
    method: Optional[ScrapingMethodEnum] = ScrapingMethodEnum.get
    scraping_config_id: Optional[str] = str(uuid4())

class Task(CamelMode):
    task_id: Optional[str] = None
    task_type_id: str
    user_id: str
    name: str
    description: str
    status: Optional[TaskStatusEnum] = TaskStatusEnum.pending

class TaskCreate(Task):
    email_task: Optional[EmailTask] = None
    scraping_task: Optional[ScrapingTask] = None
    is_active: Optional[bool] = True