import os
import logging
import json
import base64
from typing import Dict, List
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class AES:

    def __init__(self):
        self.iv_length = 32
        self.tag_length = 16

    @staticmethod
    def generate_key() -> str:
        """Generates a random 256-bit AES key and returns it Base64 encoded."""
        key = os.urandom(32)
        return base64.b64encode(key).decode('utf-8')
    
    def encrypt(self, aes_key:str, data:Dict[str,str] | str | List[Dict[str,str]]) -> str:
        if not isinstance(data, (dict, str, list)):
            raise ValueError('The data to be encrypted must be a dictionary, list, or string')

        try:
            key = base64.b64decode(aes_key)
            iv = os.urandom(self.iv_length)
            if isinstance(data, (dict, list)):
                json_data = json.dumps(data)
            else:
                json_data = data

            cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(json_data.encode('utf-8')) + encryptor.finalize()
            tag = encryptor.tag
            encrypted_data = iv + ciphertext + tag

            return base64.b64encode(encrypted_data).decode('utf-8')

        except Exception as e:
            logging.error(f'Unexpected AES encryption error: {str(e)}')
            # raise AESEncryptException(message=UNEXPECTED_ERROR, error=str(e), status_code=APP_ERROR)
 

    def decrypt(self, aes_key:str, encrypted_data:str):
        try:
            key = base64.b64decode(aes_key)
            encrypted_data = base64.b64decode(encrypted_data)
            iv = encrypted_data[:self.iv_length]
            tag = encrypted_data[-self.tag_length:]
            ciphertext = encrypted_data[self.iv_length:-self.tag_length]
            cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            try:
                decrypted_data = json.loads(plaintext.decode('utf-8'))
                return decrypted_data
            except json.JSONDecodeError:
                return plaintext.decode('utf-8')

        except Exception as e:
            logging.error(f'Unexpected AES decryption error: {str(e)}')
            # raise AESEncryptException(message=UNEXPECTED_ERROR, error=str(e), status_code=APP_ERROR)