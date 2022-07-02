
from app.amqp.pika_client import send_rabbitmq
from app.core.config import Settings
from app.models.models_notifications import NotificationsExt
from fastapi import APIRouter

router = APIRouter()
settings = Settings()


@router.post(
    '/send',
    summary='Уведомления',
    description='Отправка уведомления в очередь RebbitMQ',
    tags=['notifications'],
)
async def new_series(
        notification: NotificationsExt,
):
    """

    :param notification: Notification
    :param credentials: Auth
    :return:
    """
    if notification.type_send == notification.type_send.new_series or \
            notification.type_send == notification.type_send.email_confirmation:
        notification.last_chunk = True
        await send_rabbitmq(notification.dict(), settings.email_queue)
    else:
        await send_rabbitmq(notification.dict(), settings.group_queue)
    return notification
