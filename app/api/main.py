from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.email import router as email_router
from app.api.routes.auth import router as auth_router


app = FastAPI(
    title="Email Agent API",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://autocompose.lovable.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(email_router)
app.include_router(auth_router)