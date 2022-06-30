import logging.config
from enum import Enum

from pydantic import BaseSettings, Field


class RabbitSendEmailQueue(BaseSettings):
    exchange = 'email'
    exchange_type = 'direct'
    queue = 'send_email'
    durable = True


class RabbitChunkQueue(BaseSettings):
    exchange = 'group_chunk'
    exchange_type = 'direct'
    queue = 'group_chunk'
    durable = True


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    # 'root': {
    #     'handlers': ['stream_handler'],
    #     'level': 'ERROR'
    # },
    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
        },
    },

    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
    },

    'loggers': {
        'core.rabbit': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'core.mail': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'core.db': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'worker': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
            'propagate': True
        },
    }
}


class NotificationStatus(Enum):
    waiting = 'waiting'
    processing = 'processing'
    done = 'done'


class Settings(BaseSettings):
    rabbit_host: str = Field('localhost', env='my_api_key')
    rabbit_send_email: RabbitSendEmailQueue = RabbitSendEmailQueue()
    rabbit_chunk: RabbitChunkQueue = RabbitChunkQueue()

    notification_db_host: str = Field('localhost', env='DB_HOST')
    notification_db_port: int = Field(5432, env='DB_PORT')
    notification_db_name: str = Field('notification', env='DB_NAME')
    notification_db_user: str = Field('app', env='DB_USER')
    notification_db_password: str = Field('123qwe', env='DB_PASSWORD')

    url_service_user: str = Field('http://auth/user_info', env='API_USER_INFO')

    logging_config = LOGGING_CONFIG

    from_email: str = 'Sinema INFO'
    chunk_size: int = 5
