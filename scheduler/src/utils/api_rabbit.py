import json
import logging
from logging import config

import backoff
import requests

from config import LOG_CONFIG

config.dictConfig(LOG_CONFIG)


@backoff.on_exception(backoff.expo, Exception)
def api_send_message(message):
    logging.info(message)
    url = 'http://notification_api:8010/app/v1/notification/send'
    resp = requests.post(url, data=json.dumps(message))
    return resp
