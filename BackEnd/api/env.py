from dotenv import load_dotenv
import os
import sys

load_dotenv(override=True)
try:
    API_SECRET_KEY = os.environ["API_SECRET_KEY"]
    API_SALT = os.environ["API_SALT"]
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"]
    DB_NAME = os.environ["DB_NAME"]
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]

except KeyError as e:
    print(f"Environment variable {e} not found. Check .env file.")
    sys.exit(1)
