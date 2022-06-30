import asyncio
import logging
import os
from pathlib import Path

import aio_pika.exceptions
import backoff
from aio_pika import connect
from dotenv import load_dotenv

load_dotenv(f"{Path(os.getcwd())}/.env")

logging.getLogger('backoff').addHandler(logging.StreamHandler())


@backoff.on_exception(wait_gen=backoff.expo,
                      exception=aio_pika.exceptions.CONNECTION_EXCEPTIONS)
async def rabbit_conn():
    connection = await connect(
            f"amqp://{os.getenv('RABBITMQ_DEFAULT_USER')}:{os.getenv('RABBITMQ_DEFAULT_PASS')}@{os.getenv('RABBITMQ_HOST')}/")

    channel = await connection.channel()
    print(channel.default_exchange.name.title())
    await connection.close()


if __name__ == '__main__':
    asyncio.run(rabbit_conn())
