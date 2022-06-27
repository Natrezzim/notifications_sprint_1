import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.api.v1 import send_notification
from app.core.config import Settings

settings = Settings()

app = FastAPI(
    title=f'{settings.project_name}',
    docs_url='/app/openapi',
    openapi_url='/app/openapi.json',
    default_response_class=ORJSONResponse,
    description='Сбор и редактирование лайков, рецензий и закладок фильмов',
    version='1.0.0',
)

@app.on_event('startup')
async def startup():
    print('hi')


@app.on_event('shutdown')
async def shutdown() -> None:
    print('Bye')


app.include_router(send_notification.router, prefix='/app/v1/send_notification')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)  # noqa S104
