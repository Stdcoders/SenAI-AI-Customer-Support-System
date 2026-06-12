from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.db.database import Base, engine
import app.models
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION,

    docs_url="/docs",

    redoc_url="/redoc",

)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(api_router)


@app.get("/health")

def health():

    return {

        "status": "healthy",

        "service": settings.APP_NAME,

        "version": settings.APP_VERSION,

    }