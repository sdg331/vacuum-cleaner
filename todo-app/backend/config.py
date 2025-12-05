import os

# 기본값 (로컬 개발용)
DEFAULT_DB_USER = "todo_user"
DEFAULT_DB_PASSWORD = "todo_password"
DEFAULT_DB_HOST = "localhost"
DEFAULT_DB_PORT = "3306"
DEFAULT_DB_NAME = "todo_db"


def get_database_uri() -> str:
    """
    환경변수 또는 기본값으로부터 SQLAlchemy용 DB URI 생성.
    형식: mysql+pymysql://user:password@host:port/database
    """
    user = os.getenv("DB_USER", DEFAULT_DB_USER)
    password = os.getenv("DB_PASSWORD", DEFAULT_DB_PASSWORD)
    host = os.getenv("DB_HOST", DEFAULT_DB_HOST)
    port = os.getenv("DB_PORT", DEFAULT_DB_PORT)
    name = os.getenv("DB_NAME", DEFAULT_DB_NAME)

    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"
