"""
설정 파일 (Configuration)
개발/프로덕션 환경을 분리하여 관리합니다.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """기본 설정 (모든 환경 공통)"""
    
    # SQLAlchemy 설정
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JSON 한글 깨짐 방지
    JSON_AS_ASCII = False
    
    # DB 접속 정보
    DB_USER = os.getenv("DB_USER", "todo_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "todo_password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "todo_db")
    
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        "?charset=utf8mb4"  # 이모지 지원
    )


class DevelopmentConfig(Config):
    """개발 환경 설정"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """프로덕션 환경 설정"""
    DEBUG = False
    TESTING = False
    
    # 프로덕션에서는 반드시 환경변수 설정 필수
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


# 환경변수 FLASK_ENV 값에 따라 설정 선택
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}


def get_config():
    """현재 환경에 맞는 설정 반환"""
    env = os.getenv("FLASK_ENV", "development")
    return config.get(env, config["default"])
