from abc import ABC, abstractmethod
from typing import Dict

class AuthOutput(ABC):

    @abstractmethod
    async def login(self) -> Dict[str,str]: ...