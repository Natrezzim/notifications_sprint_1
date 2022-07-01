from config import Settings
from core.db import NotificationsDb
from core.rabbit import Rabbit
from core.worker import WorkerChunkUserFromGroup

settings = Settings()


def init_channel_consumer(cls):
    cls.channel.exchange_declare(
        exchange=settings.rabbit_chunk.exchange,
        exchange_type=settings.rabbit_chunk.exchange_type,
        durable=settings.rabbit_chunk.durable,
    )

    cls.channel.queue_declare(queue=settings.rabbit_chunk.queue, durable=settings.rabbit_chunk.durable)
    cls.channel.queue_bind(exchange=settings.rabbit_chunk.exchange, queue=settings.rabbit_chunk.queue)


def init_channel_publish(cls):
    cls.channel.exchange_declare(
        exchange=settings.rabbit_send_email.exchange,
        exchange_type=settings.rabbit_send_email.exchange_type,
        durable=settings.rabbit_send_email.durable,
    )

    cls.channel.queue_declare(queue=settings.rabbit_send_email.queue, durable=settings.rabbit_send_email.durable)
    cls.channel.queue_bind(exchange=settings.rabbit_send_email.exchange, queue=settings.rabbit_send_email.queue)


if __name__ == '__main__':
    db = NotificationsDb(
        user=settings.notification_db_user,
        password=settings.notification_db_password,
        host=settings.notification_db_host,
        port=settings.notification_db_port,
        db_name=settings.notification_db_name
    )

    rabbit_chunk = Rabbit(
        settings.rabbit_host,
        settings.rabbit_user,
        settings.rabbit_password,
        queue=settings.rabbit_chunk.queue,
        exchange=settings.rabbit_chunk.exchange,
        init_channel=init_channel_consumer
    )
    rabbit_send_email = Rabbit(
        settings.rabbit_host,
        settings.rabbit_user,
        settings.rabbit_password,
        queue=settings.rabbit_send_email.queue,
        exchange=settings.rabbit_send_email.exchange,
        init_channel=init_channel_publish
    )

    w = WorkerChunkUserFromGroup(rabbit_chunk, rabbit_send_email, db)
    w.run()
