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
            "datefmt": "%d-%m-%Y %I:%M:%S"
        }
    },
}
TIME_TO_RESTART = 60

# PG_DSL = {
#     'dbname': os.environ.get('POSTGRES_DB'),
#     'user': os.environ.get('POSTGRES_USER'),
#     'password': os.environ.get('POSTGRES_PASSWORD'),
#     'host': os.environ.get('POSTGRES_HOST'),
#     'port': os.environ.get('POSTGRES_PORT'),
# }
PG_DSL = {
    'dbname': 'notification',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': 5432,
}