from typing import Dict
from datetime import datetime
from jose import JWTError, jwt

class JWT:

    SECRET_KEY = '6UXxGjYuHPsIXD4DVr7zuw812468NPbX'
    ALGORITHM = 'HS256'

    def create_access_token(self, data: Dict[str,str], token_exp: datetime) -> str:
        to_encode = data.copy()
        to_encode.update({"exp": token_exp})
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)


    def verify_token(self, token: str) -> Dict[str,str] | None:
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except JWTError:
            return None
