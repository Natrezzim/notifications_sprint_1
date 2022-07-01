import logging.config

import backoff
import pika

from config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class Rabbit:
    def __init__(self, host, user, password, queue, exchange, init_channel=None):
        self.host = host
        self.user = user
        self.password = password
        credentials = pika.PlainCredentials(self.user, self.password)

        self.parameters = pika.ConnectionParameters(host=self.host, credentials=credentials)
        self.connection = None
        self.channel = None
        self.queue = queue
        self.exchange = exchange
        self.init_channel = init_channel

    @backoff.on_exception(backoff.expo, pika.exceptions.AMQPConnectionError)
    def connect(self):
        if not self.connection:
            logger.info('start_connection rabbit')
            self.connection = pika.BlockingConnection(self.parameters)
            self.channel = self.connection.channel()
        if self.init_channel:
            self.init_channel(self)

    def listen_channel(self, message_callback, auto_ack=True):
        self.channel.basic_consume(queue=self.queue, on_message_callback=message_callback, auto_ack=auto_ack)

        logger.debug(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def publish(self, message):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.queue,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        logger.debug(" [x] Sent %r" % message)