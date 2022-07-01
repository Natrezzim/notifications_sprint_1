import logging
from datetime import datetime
from enum import Enum
from logging import config
from typing import List

import backoff
import psycopg2
from psycopg2.extras import RealDictCursor, RealDictRow

from config import PG_DSL, LOG_CONFIG

config.dictConfig(LOG_CONFIG)


class NotificationStatus(Enum):
    waiting = 'waiting'
    processing = 'processing'
    done = 'done'


class PGConnectorBase:
    def __init__(self, logging=logging):
        self.db = None
        self.cursor = None
        self._logging = logging
        self.connect()

    @backoff.on_exception(backoff.expo, Exception)
    def connect(self) -> None:
        self.db = psycopg2.connect(**PG_DSL, cursor_factory=RealDictCursor)
        self.cursor = self.db.cursor()
        logging.info('connect db')

    @backoff.on_exception(backoff.expo, Exception)
    def query(self, sql: str) -> List[RealDictRow]:
        try:
            self.cursor.execute(sql)
        except psycopg2.OperationalError:
            self._logging.error('Ошибка подключения к базе postgres')
            self.connect()
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    @backoff.on_exception(backoff.expo, Exception)
    def set_query(self, sql: str):
        try:
            self.cursor.execute(sql)
        except psycopg2.OperationalError:
            self._logging.error('Ошибка подключения к базе postgres')
            self.connect()
            self.cursor.execute(sql)
        self.db.commit()

    def close(self):
        if self.db:
            self.db.close()
            self.db = None
            self.cursor = None

    def __del__(self) -> None:
        self.close()


class PGNotification(PGConnectorBase):
    def get_notification(self):
        sql_tmp = (
            "select notification.id, context.template_id as template_id, context.params, type.title "
            "from notification_notification notification "
            "left join notification_notificationcontext context on context.id = notification.context_id "
            "left join notification_template template on context.template_id = template.id "
            "left join notification_notificationtype type on type.id = template.notification_type_id "
            "WHERE notification.send_date <= %(timestamp)s and send_status = %(notification_status)s"
        )
        sql = self.cursor.mogrify(sql_tmp, {
            'timestamp': datetime.now(),
            'notification_status': NotificationStatus.waiting.value
        })
        logging.debug(sql)
        result = self.query(sql)
        logging.debug(result)
        return result

    def set_status_processing(self, notification_id):
        sql_tmp = (
            "UPDATE notification_notification "
            "SET send_status=%(status)s "
            "WHERE id = %(notification_id)s"
        )
        sql = self.cursor.mogrify(sql_tmp, {
            'status': NotificationStatus.processing.value,
            'notification_id': notification_id
        })
        self.set_query(sql)
