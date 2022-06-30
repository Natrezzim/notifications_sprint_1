
from app.amqp.pika_client import send_rabbitmq
from app.models.models_notifications import NotificationsExt
from app.service.auth import Auth
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer

security = HTTPBearer()
auth_handler = Auth()
router = APIRouter()


@router.post(
    '/notifications',
    summary='Уведомления',
    description='Отправка уведомления в очередь RebbitMQ',
    tags=['notifications'],
)
async def new_series(
        notification: NotificationsExt,
        credentials: HTTPBasicCredentials = Depends(security),
):
    """

    :param notification: Notification
    :param credentials: Auth
    :return:
    """
    if notification.type_send == notification.type_send.new_series or \
            notification.type_send == notification.type_send.email_confirmation:
        await send_rabbitmq(notification.dict(), "topic_priority")
    else:
        await send_rabbitmq(notification.dict(), "topic_simplify")
    return notification
