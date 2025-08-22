from pydantic import BaseModel
from src.shared.utils.case_converter import CaseConverter

class CamelMode(BaseModel):
    class Config:
        alias_generator = CaseConverter.to_camel
        validate_by_name = True  # Permite usar snake_case en el backend