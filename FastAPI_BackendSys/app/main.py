from fastapi import FastAPI
from app.controllers.user_controller import router
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI(
    title="Clean Architecture FastAPI",
    version="0.1.0",
    description="Example Clean Architecture backend with controller routers",
)

app.add_middleware(LoggingMiddleware)

@app.get("/", tags=["health"])
def home():
    return {"message": "API is running"}

app.include_router(router)
