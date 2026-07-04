import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Khala Nosa")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0-alpha")

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///khala_nosa.db"
    )

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    DEBUG = os.getenv("DEBUG", "True") == "True"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "ar")
    DEFAULT_PERSONALITY = os.getenv(
        "DEFAULT_PERSONALITY",
        "khala_nosa"
    )

settings = Settings()
