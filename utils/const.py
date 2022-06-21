from os import getenv
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".", ".env")
load_dotenv(dotenv_path=env_path)


JWT_SECRET_KEY = getenv("SECRET_KEY")
JWT_ALGORITH = getenv("ALGORITH")
JWT_EXPIRATION_TIME_MINUTES = 60 * 24 * 5


# local DB Host
DB_HOST = getenv("db_host")
DB_USER = getenv("db_user")
DB_PASSWORD = getenv("db_pass")
DB_NAME = getenv("db_name")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"