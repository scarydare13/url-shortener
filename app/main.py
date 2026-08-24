from fastapi import FastAPI

from app.api.v1.auth import router as auth_router


app = FastAPI(
    title="URL Shortener API",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/documentation",
)


app.include_router(auth_router)