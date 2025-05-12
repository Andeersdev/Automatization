import jwt
from typing import Dict

class JWT:

    def __init__(self):
        self.key = ''

    
    def encode(self, payload:Dict[str,str]) -> bytes:
        return jwt.encode(payload, self.key, algorithm='HS256')

    
    def decode(self, encoded:str) -> Dict[str,str]:
        return jwt.decode(encoded, self.key, algorithm='HS256')