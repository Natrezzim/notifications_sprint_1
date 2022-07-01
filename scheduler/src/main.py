import json
import logging
from logging import config
from pprint import pprint
from time import sleep
from typing import Optional

from config import TIME_TO_RESTART, LOG_CONFIG
from utils.posgres_db import PGNotification

config.dictConfig(LOG_CONFIG)

# logging.error("скрипт уже запущен!!!")

from pydantic import BaseModel, Field

class Context(BaseModel):
    users_id: Optional[list]
    group_id: Optional[str]
    payload: dict


class Message(BaseModel):
    notification_id: str
    template_id: str
    context: Context



def process():
    try:
        pg.connect()
        result = pg.get_notification()
        data = [{key: value for key, value in item.items()} for item in result]

        for item in data:
            pprint(item)
            params = item.get('params')
            context = Context(
                group_id=params.get('group_id', None),
                users_id=params.get('users_id', None),
                payload=params.get('payload', {})
            )
            message = Message(
                context=context,
                template_id=item.get('template_id'),
                notification_id=item.get('id')
            )
            pprint(message.dict())
            pg.set_status_processing(item.get('id'))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pg = PGNotification()
    while True:
        process()
        sleep(TIME_TO_RESTART)
