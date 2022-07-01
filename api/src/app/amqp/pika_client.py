import json
import logging
from json import JSONEncoder

import aio_pika
from aio_pika import Message, ExchangeType
from app.core.config import Settings
from app.utils.json_encoder import new_default

settings = Settings()

JSONEncoder.default = new_default

logger = logging.getLogger(__name__)


async def get_connection():
    """

    :return: aio_pika.connection
    """
    return await aio_pika.connect_robust(
        f"amqp://{settings.rabbitmq_user}:{settings.rabbitmq_pass}@{settings.rabbitmq_host}/")


async def send_rabbitmq(msg=dict, queue=str):
    connection = await get_connection()
    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key=queue
    )
    logger.info(json.dumps(msg))
    await connection.close()


async def declare_queues():
    connection = await get_connection()
    channel = await connection.channel()

    email_exchange = await channel.declare_exchange(settings.email_exchange, ExchangeType.DIRECT, durable=True)
    group_chunk_exchange = await channel.declare_exchange(settings.group_exchange, ExchangeType.DIRECT, durable=True)

    send_email_priority_queue = await channel.declare_queue(settings.email_queue, durable=True)
    group_chunk_queue = await channel.declare_queue(settings.group_queue, durable=True)

    await send_email_priority_queue.bind(email_exchange)
    await group_chunk_queue.bind(group_chunk_exchange)

    await connection.close()
