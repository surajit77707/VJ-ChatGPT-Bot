import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "23967991"))
API_HASH = environ.get("API_HASH", "a2c3ccfaff4c2dbbff7d54981828d4f1")
BOT_TOKEN = environ.get("BOT_TOKEN", "7938895846:AAF-m2SpaSsyPewW2TQtST7FmfWIVBF8HOQ")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002491736059"))
ADMINS = int(environ.get("ADMINS", "7638575366"))
DB_URI = environ.get("DB_URI", "mongodb+srv://princekumarjat123:princekumarjat123@cluster0.kaj89.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "cluster0")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
