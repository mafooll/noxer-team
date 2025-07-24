import os
from dotenv import load_dotenv


load_dotenv()


def build_database_url():
    user = os.getenv("POSTGRES_USER", "user")
    password = os.getenv("POSTGRES_PASS", "pass")
    host = os.getenv("POSTGRES_HOST", "db")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "db")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


class Config:
    SQLALCHEMY_DATABASE_URI = build_database_url()

    API_MAIN_TRUE = "https://bot-igor.ru/api/products?on_main=true"
    API_MAIN_FALSE = "https://bot-igor.ru/api/products?on_main=false"

    LOAD_INTERVAL_SECONDS = int(os.getenv("LOAD_INTERVAL_SECONDS", 3600))
    EXECUTOR_TYPE = "thread"

    INFO_ROUTE = os.getenv("INFO_ROUTE", "/info")

    HOST = os.getenv("WEB_HOST", "0.0.0.0")
    PORT = int(os.getenv("WEB_PORT", 5555))
