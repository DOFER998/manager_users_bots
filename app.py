import asyncio

import uvicorn
from beanie import init_beanie
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src import is_admin_router, info_router, db_client, SelfBotModal, InfoModel, UserModel

app = FastAPI(title='API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(is_admin_router)
app.include_router(info_router)


@app.on_event('startup')
async def on_startup():
    await init_beanie(
        database=db_client.Bot,
        document_models=[
            SelfBotModal,
            InfoModel,
            UserModel
        ]
    )
