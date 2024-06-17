from fastapi import FastAPI
import uvicorn

main_app = FastAPI()


@main_app.get("/")
async def hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        reload=True,
    )
