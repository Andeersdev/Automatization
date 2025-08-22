from fastapi import APIRouter, Request
from src.controllers.auth_controller import AuthController
from src.interfaces.auth import Login, Logout

auth_router = APIRouter(prefix='/auth', tags=['auth'])

controller = AuthController()

@auth_router.post('/login')
async def login(request: Login):
    return await controller.login(request)


@auth_router.post('/logout')
async def logout(request: Logout):
    return await controller.logout(request)