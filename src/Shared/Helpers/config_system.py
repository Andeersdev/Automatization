from typing import List, Dict
from src.database import db

class ConfigSystem:

    @staticmethod
    async def get_config_system(enterprise_id: str) -> List[Dict[str,str]]:
        query = ''' SELECT * FROM funcs_get_config_sytem(:enterpriseId) '''
        return await db.execute_query_return_data(query, {'enterpriseId': enterprise_id}, fetchone=True)

