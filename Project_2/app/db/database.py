# sluzi za konekciju sa bazom
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

MYSQL_URL = f"{settings.DB_HOST}://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOSTNAME}:" \
            f"{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(MYSQL_URL, echo=True)

# databases = engine.execute("SHOW DATABASES;")
# existing_db = [d[0] for d in databases]

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()



