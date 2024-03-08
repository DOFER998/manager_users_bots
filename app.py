import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src import is_admin_router, info_router

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
