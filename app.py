from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.routes.auth_route import auth_router
from src.routes.role_route import role_router
from src.routes.user_route import user_router
from src.routes.enterprise_route import enterprise_router
from src.routes.task_type_route import task_type_router
from src.routes.task_routes import task_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(role_router)
app.include_router(user_router)
app.include_router(enterprise_router)
app.include_router(task_type_router)
app.include_router(task_router)


# for /d /r . %d in (__pycache__) do @if exist "%d" rd /s /q "%d"
# uvicorn app:app --host 0.0.0.0 --port 8000 --reload 