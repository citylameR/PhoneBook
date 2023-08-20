from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import db.config
from db.models import contacts

engine = create_engine(db.config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Инициализировать БД через модели 
contacts.Base.metadata.create_all(bind=engine)


# Функции для запросов к БД
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
