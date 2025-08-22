import os
from dotenv import load_dotenv
from .connection import Connection

load_dotenv(dotenv_path='.env', override=True)

db = Connection(os.getenv('DATABASE_URL'))