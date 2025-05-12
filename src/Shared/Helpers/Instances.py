import os
from dotenv import load_dotenv
from src.Infrastructure.Database.Connection import Connection
from src.Shared.Helpers.Aes import AES

load_dotenv(dotenv_path='.env', override=True)

db = Connection(os.getenv('DATABASE_URL'))
aes = AES()