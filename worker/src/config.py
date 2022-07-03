import logging.config
from enum import Enum

from pydantic import BaseSettings, Field


class RabbitSendEmailPriorityQueue(BaseSettings):
    exchange: str = Field('send_email_priority', env='RABBIT_SEND_EMAIL_PRIORITY_QUEUE_EXCHANGE')
    exchange_type: str = Field('direct', env='RABBIT_SEND_EMAIL_PRIORITY_QUEUE_EXCHANGE_TYPE')
    queue: str = Field('send_email_priority', env='RABBIT_SEND_EMAIL_PRIORITY_QUEUE')
    durable: str = Field('True', env='RABBIT_SEND_EMAIL_PRIORITY_QUEUE_DURABLE')


class RabbitSendEmailQueue(BaseSettings):
    exchange: str = Field('send_email', env='RABBIT_SEND_EMAIL_QUEUE_EXCHANGE')
    exchange_type: str = Field('direct', env='RABBIT_SEND_EMAIL_QUEUE_EXCHANGE_TYPE')
    queue: str = Field('send_email', env='RABBIT_SEND_EMAIL_QUEUE')
    durable: str = Field('True', env='RABBIT_SEND_EMAIL_QUEUE_DURABLE')


class RabbitChunkQueue(BaseSettings):
    exchange: str = Field('group_chunk', env='RABBIT_CHUNK_QUEUE_EXCHANGE')
    exchange_type: str = Field('direct', env='RABBIT_CHUNK_QUEUE_EXCHANGE_TYPE')
    queue: str = Field('group_chunk', env='RABBIT_CHUNK_QUEUE')
    durable: str = Field('True', env='RABBIT_CHUNK_QUEUE_DURABLE')


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
        'core.worker': {
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
    rabbit_host: str = Field('rabbitmq', env='RABBITMQ_HOST')
    rabbit_user: str = Field('user', env='RABBITMQ_DEFAULT_USER')
    rabbit_password: str = Field('pass', env='RABBITMQ_DEFAULT_PASS')
    rabbit_send_email_priority: RabbitSendEmailQueue = RabbitSendEmailPriorityQueue()
    rabbit_send_email: RabbitSendEmailQueue = RabbitSendEmailQueue()
    rabbit_chunk: RabbitChunkQueue = RabbitChunkQueue()

    notification_db_host: str = Field('db', env='BACKEND_DB_HOST')
    notification_db_port: int = Field(5432, env='BACKEND_DB_PORT')
    notification_db_user: str = Field('postgres', env='BACKEND_DB_USER')
    notification_db_password: str = Field('1234', env='BACKEND_DB_PASSWORD')
    notification_db_name: str = Field('notification', env='BACKEND_DB_NAME')

    url_service_user: str = Field('http://auth/user_info', env='API_USER_INFO')

    logging_config = LOGGING_CONFIG

    from_email: str = Field('Cinema INFO', env='FROM_EMAIL')
    chunk_size: int = 50

    mailhog_host = 'mailhog_notification'
    mailhog_port = 1025
    mailhog_user = ''
    mailhog_password = ''


class Config:
    env_file = ".env"
