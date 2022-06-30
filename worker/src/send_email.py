from config import Settings
from core.db import NotificationsDb
from core.get_user import ApiUserInfoFake
from core.mail import EmailSMTPFake
from core.rabbit import Rabbit
from core.worker import WorkerSendMessage

settings = Settings()


def init_channel(cls):
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

    email = EmailSMTPFake(host='', port=1, user='', password='', from_email=settings.from_email)

    rabbit = Rabbit(
        settings.rabbit_host,
        queue=settings.rabbit_send_email.queue,
        exchange=settings.rabbit_send_email.exchange,
        init_channel=init_channel
    )

    api = ApiUserInfoFake('url_fake')

    w = WorkerSendMessage(rabbit, db, email, api)
    w.run()
