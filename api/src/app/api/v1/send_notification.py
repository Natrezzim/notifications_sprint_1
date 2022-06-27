from uuid import UUID

from app.amqp.pika_client import send_rabbitmq
from app.models.models_db import Notification, NotificationCreate
from app.models.models_notifications import NewSeries, EmailConfirmation, Recommendations, Likes
from app.service.auth import Auth
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.pg_db import get_session

security = HTTPBearer()
auth_handler = Auth()
router = APIRouter()


# @router.get(
#     '/',
#     summary='Добавление лайка',
#     description='Добавление лайка к фильму для последующей рассылки',
#     response_description='200 OK, 400 BAD RESPONSE',
#     tags=['likes'],
# )
# async def add_likes(
#         session: AsyncSession = Depends(get_session),
#         credentials: HTTPBasicCredentials = Depends(security),
# ) -> dict[str, UUID]:
#     token = credentials.credentials  # type: ignore[attr-defined]
#     result = await session.execute(select(Notification))
#     res = result.scalars().all()
#     return [*res]
#
#
# @router.post(
#     '/',
#     summary='Добавление лайка',
#     description='Добавление лайка к фильму для последующей рассылки',
#     response_description='200 OK, 400 BAD RESPONSE',
#     tags=['likes'],
# )
# async def add_likes(
#         notification: NotificationCreate,
#         session: AsyncSession = Depends(get_session),
#         credentials: HTTPBasicCredentials = Depends(security),
# ) -> dict[str, UUID]:
#     token = credentials.credentials  # type: ignore[attr-defined]
#     ntf = Notification(**notification.dict())
#     session.add(ntf)
#     await session.commit()
#     await session.refresh(ntf)
#     return ntf

@router.post(
    '/new_series',
    summary='Новая серия',
    description='Отправка уведомления о новой серии',
    tags=['new_series'],
)
async def new_series(
        series: NewSeries,
        credentials: HTTPBasicCredentials = Depends(security),
):
    await send_rabbitmq(series.dict(), "topic_priority")
    return series


@router.post(
    '/email_confirmations',
    summary='Подтверждение регистрации',
    description='Отправка письма с ссылкой подтверждения регистрации',
    tags=['email_confirmation'],
)
async def email_confirmation(
        email: EmailConfirmation,
        credentials: HTTPBasicCredentials = Depends(security),
):
    await send_rabbitmq(email.dict(), "topic_priority")
    return email


@router.post(
    '/recommendations',
    summary='Рекоммендации',
    description='Отправка письма с реккомендоваными фильмами для группы пользователей',
    tags=['email_confirmation'],
)
async def recommendations(
        recommendation: Recommendations,
        credentials: HTTPBasicCredentials = Depends(security),
):
    await send_rabbitmq(recommendation.dict(), "topic_simplify")
    return recommendation

@router.post(
    '/likes',
    summary='Лайки',
    description='Сбор лайков',
    tags=['likes'],
)
async def recommendations(
        likes: Likes,
        session: AsyncSession = Depends(get_session),
        credentials: HTTPBasicCredentials = Depends(security),
):
    statement = select(Notification).where(Notification.id == "Deadpond")
    results = await session.exec(statement)
    return likes