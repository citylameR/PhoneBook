from fastapi import FastAPI

from db.db import engine
from controllers.routers import router
from controllers.download_data import router as download_router
from db.models import contacts

app = FastAPI()

contacts.Base.metadata.create_all(bind=engine)
app.include_router(router)
app.include_router(download_router)


def start_app():
    """Запуск приложения"""
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, )


if __name__ == "__main__":
    start_app()
