import logging
from logging import config
from typing import List

import backoff
import psycopg2
from psycopg2.extras import RealDictCursor, RealDictRow

from config import PG_DSL, LOG_CONFIG

config.dictConfig(LOG_CONFIG)


class PGConnectorBase:
    def __init__(self, logging=logging):
        self.db = None
        self.cursor = None
        self._logging = logging
        self.connect()

    # @backoff.on_exception(backoff.expo, Exception)
    def connect(self) -> None:
        if not self.db:
            self.db = psycopg2.connect(**PG_DSL, cursor_factory=RealDictCursor)
        if not self.cursor:
            self.cursor = self.db.cursor()
        print('connect db')

    # @backoff.on_exception(backoff.expo, Exception)
    def query(self, sql: str) -> List[RealDictRow]:
        try:
            self.cursor.execute(sql)
        except psycopg2.OperationalError:
            self._logging.error('Ошибка подключения к базе postgres')
            self.connect()
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def set_query(self, sql: str):
        self.cursor.execute(sql)
        self.db.commit()

    def __del__(self) -> None:
        if self.db:
            self.db.close()


class PGNotification(PGConnectorBase):
    def get_notification(self):
        sql = (
            "select notification.id, context.template_id as template_id, context.params "
            "from notification_notification notification "
            "left join notification_notificationcontext context on context.id = notification.context_id "
            "WHERE notification.send_date <= CURRENT_TIMESTAMP and send_status = 'waiting'"
        )
        print('sql query')
        print(sql)
        result = self.query(sql)
        return result

    def set_status_processing(self, notification_id):
        sql_tmp = (
            "UPDATE notification_notification "
            "SET send_status=%(status)s "
            "WHERE id = %(notification_id)s"
        )
        sql = self.cursor.mogrify(sql_tmp, {
            'status': 'processing',
            'notification_id': notification_id
        })
        self.set_query(sql)

