import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv()


class Settings:

    PROJECT_NAME: str = "MLUVIJO"
    PROJECT_VERSION: str = "0.0.1"
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


settings = Settings()
