from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import meals, meal_details, boxes
import datetime
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/date-details")
def date_details():
    now = datetime.datetime.now()
    return {
        "date_details": {
            "year": now.year,
            "month": now.month,
            "day": now.day,
            "hour": now.hour,
            "min": now.minute,
            "tz": str(now.astimezone().tzinfo),
        }
    }


app.include_router(meals.router, prefix="/api", tags=["meals"])
app.include_router(meal_details.router, prefix="/api", tags=["meals"])
app.include_router(boxes.router, prefix="/api", tags=["boxes"])
