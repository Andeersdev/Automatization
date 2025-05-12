import os
from functools import wraps
from pydantic import BaseModel, ValidationError
from dotenv import load_dotenv
from .Aes import AES
load_dotenv(dotenv_path='.env', override=True)

aes = AES()
def process_encrypted_data(model:BaseModel = None):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs): 
            #legacy = await db_security_query.get_data_legacy()
            if 'user_token' in kwargs:                
                kwargs['user_token_id'] = payload.get('tokenId')
                kwargs['user_id'] = payload.get('userId')
                kwargs['external_enterprise_id'] = payload.get('externalEnterpriseId')
                kwargs['profile_id'] = payload.get('profileId')
                kwargs['legacy_id'] = payload.get('legacyId')
                kwargs['enterprise_id'] = payload.get('enterpriseId')
                kwargs['user_full_name'] = payload.get('userFullName')
                kwargs['abbreviation'] = payload.get('abbreviation')
                kwargs['aes_auth'] = payload.get('aesAuth')
                del kwargs['user_token']

            if 'aes_data' in kwargs:
                aes_data = kwargs.get('aes_data')
                decrypted_data = aes.decrypt(os.getenv('AES_KEY'), aes_data)
                if model:
                    try:
                        kwargs['data'] = model(**decrypted_data)
                    except ValidationError as e:
                        raise ValueError(f'Invalid data format: {str(e)}')
                else:
                    kwargs['data'] = decrypted_data
                
                del kwargs['aes_data']

            # kwargs['legacy'] = legacy
            # kwargs['jwt_user_key'] = jwt_user_key
            return await func(self, **kwargs)  
        
        return wrapper
    return decorator