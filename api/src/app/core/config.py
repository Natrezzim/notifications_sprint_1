
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    project_name: str = Field('app kafka', env='PROJECT_NAME')

    jwt_secret_key: str = Field('test', env='JWT_SECRET_KEY')

    db_url: str = Field('localhost:5432', env='DB_URL')
    db_user: str = Field('app', env='DB_USER')
    db_password: str = Field('qwe123', env='DB_PASSWORD')
    db_name: str = Field('notification_database', env='DB_NAME')

    rabbitmq_host: str = Field('localhost', env='RABBITMQ_HOST')
    rabbitmq_user: str = Field('user', env='RABBITMQ_DEFAULT_USER')
    rabbitmq_pass: str = Field('pass', env='RABBITMQ_DEFAULT_PASS')

    class Config:
        env_file = ".env"
