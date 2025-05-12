from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from ariadne.asgi import GraphQL
from src.Infrastructure.Graphql.Resolvers import schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"]
)

async def get_context(request: Request, _: dict):
    authorization = request.headers.get('Authorization')
    user_token = None
    if authorization and authorization.startswith('Bearer '):
        user_token = authorization.split(' ')[1]

    headers: dict = request.headers
    return {'request': request, 'headers': headers, 'user_token': user_token}

graphql_app = GraphQL(schema, context_value=get_context, introspection=True)
app.add_route('/graphql', graphql_app)


# for /d /r . %d in (__pycache__) do @if exist "%d" rd /s /q "%d"
# uvicorn app:app --host 0.0.0.0 --port 8000 --reload 