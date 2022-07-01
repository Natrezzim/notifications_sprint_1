import os

from dotenv import load_dotenv

load_dotenv()
LEVEL_LOG = 'INFO'

LOG_CONFIG = {
    "version": 1,
    "root": {
        "handlers": ["console"],
        "level": LEVEL_LOG
    },
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": LEVEL_LOG
        }
    },
    "formatters": {
        "std_out": {
            "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S"
        }
    },
}
TIME_TO_RESTART = 60

PG_DSL = {
    'host': os.environ.get('BACKEND_DB_HOST'),
    'port': os.environ.get('BACKEND_DB_PORT'),
    'user': os.environ.get('BACKEND_DB_USER'),
    'password': os.environ.get('BACKEND_DB_PASSWORD'),
    'dbname': os.environ.get('BACKEND_DB_NAME'),
}
