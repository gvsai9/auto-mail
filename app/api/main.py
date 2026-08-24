from fastapi import FastAPI

from app.api.routes.email import router as email_router
from app.api.routes.auth import router as auth_router


app = FastAPI(
    title="Email Agent API",
)


app.include_router(email_router)
app.include_router(auth_router)