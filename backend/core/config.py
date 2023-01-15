import os
from typing import Dict
from typing import List
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Language Detection"
    PROJECT_VERSION: str = "1.0.0"
    CONTACT: Dict = {'name': 'Gregor Liedtke', 'email': 'gregor.liedtke@protonmail.com'}
    METADATA: List[Dict] = [
            {'name': 'detect',
             'description': 'The endpoint is accepting a string of text and is returning the detected language of it'},
            {'name': 'users',
             'description': 'User registration operation'},
            {'name': 'login',
             'description': 'User loging operation'}]

    USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins
    TEST_USER_EMAIL = "test@example.com"


settings = Settings()
