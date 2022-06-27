import json
from json import JSONEncoder

from aio_pika import Message, connect

from app.core.config import Settings
from app.utils.json_encoder import new_default

settings = Settings()

JSONEncoder.default = new_default


async def send_rabbitmq(msg=dict, queue=str):
    connection = await connect(f"amqp://{settings.rabbitmq_user}:{settings.rabbitmq_pass}@{settings.rabbitmq_host}/")

    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key=queue
    )

    await connection.close()
