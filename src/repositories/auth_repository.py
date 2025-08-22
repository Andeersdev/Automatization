import os
from datetime import datetime
from typing import Dict
from sqlalchemy.orm import Session
from sqlalchemy import text
from src.database import db
from src.shared.utils.data_utils import DataUtils

class AuthRepository:

    async def login(self, session: Session, email:str, password:str) -> Dict[str,str]:
        query = text(''' SELECT * FROM funcs_login(:email, :password) ''')
        params = {
            'email': email,
            'password': password
        }
        result = await session.execute(query, params)
        row = result.fetchone()
        keys = result.keys()
        if row.status_code != 'DB_SUCCESS_0001':
            session.commit()

        return DataUtils.normalize_uuids_dict(dict(zip(keys, row))) if row else {}
    
    async def insert_auth_token(self, session: Session, user_id: str, token: str, token_exp: datetime) -> None:
        query = text(''' SELECT * FROM funcs_insert_auth_token(:userId, :token, :tokenExp) ''')
        params = {
            'userId': user_id,
            'token': token,
            'tokenExp': token_exp
        }
        result = await session.execute(query, params)
        row = result.fetchone()
        if not row:
            raise ValueError('No se pudo almacenar el token')

    async def logout(self, user_id: str) -> str:
        return await db.execute_query_return_message(''' SELECT * FROM funcs_logout(:userId) ''', {'userId': user_id}, 'DB_0002')