
import logging
from pathlib import Path

import uvicorn
from app.amqp.pika_client import declare_queues
from app.api.v1 import send_notification
from app.core.config import Settings
from app.costum_logging import CustomizeLogger
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

settings = Settings()

logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")


def create_app() -> FastAPI:
    """

    :return: app
    """
    app = FastAPI(
        title=f'{settings.project_name}',
        docs_url='/app/openapi',
        openapi_url='/app/openapi.json',
        default_response_class=ORJSONResponse,
        description='Сбор и редактирование лайков, рецензий и закладок фильмов',
        version='1.0.0',
    )
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app


app = create_app()


@app.on_event('startup')
async def startup():
    await declare_queues()


@app.on_event('shutdown')
async def shutdown() -> None:
    logger.info("Shutdown app")


app.include_router(send_notification.router, prefix='/app/v1/send_notification')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)  # noqa S104
