from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(
    title="My API",
    description="This is a sample API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

app.include_router(router)

