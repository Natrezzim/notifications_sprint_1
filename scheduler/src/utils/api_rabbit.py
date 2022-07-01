import logging
from logging import config

from config import LOG_CONFIG

config.dictConfig(LOG_CONFIG)


def api_send_message(message):
    logging.info(message)