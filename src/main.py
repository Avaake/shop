from fastapi import FastAPI
import uvicorn
from core.config import settings

main_app = FastAPI()


@main_app.get("/")
async def hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run_config.host,
        port=settings.run_config.port,
        reload=True,
    )
