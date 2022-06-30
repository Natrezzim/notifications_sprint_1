import json
import logging
from json import JSONEncoder

import aio_pika
from aio_pika import Message
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

    await channel.declare_queue("topic_priority", durable=True)
    await channel.declare_queue("topic_simplify", durable=True)

    await connection.close()
