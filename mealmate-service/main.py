from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import meal, user
import os

app = FastAPI()
app.include_router(meal.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
