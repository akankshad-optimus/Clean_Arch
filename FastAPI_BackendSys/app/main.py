from fastapi import FastAPI
from app.controllers.user_controller import router
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

app.add_middleware(LoggingMiddleware)
app.include_router(router)