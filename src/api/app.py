from fastapi import FastAPI

from src.api.routes import is_admin_router, info_router

app = FastAPI(title='API')
app.include_router(is_admin_router)
app.include_router(info_router)
