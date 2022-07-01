
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    project_name: str = Field('notification', env='PROJECT_NAME')

    jwt_secret_key: str = Field('test', env='JWT_SECRET_KEY')

    rabbitmq_host: str = Field('localhost', env='RABBITMQ_HOST')
    rabbitmq_user: str = Field('user', env='RABBITMQ_DEFAULT_USER')
    rabbitmq_pass: str = Field('pass', env='RABBITMQ_DEFAULT_PASS')

    class Config:
        env_file = ".env"
