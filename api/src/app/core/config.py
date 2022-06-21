from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    project_name: str = Field('app kafka', env='PROJECT_NAME')


    class Config:
        env_file = ".env"
