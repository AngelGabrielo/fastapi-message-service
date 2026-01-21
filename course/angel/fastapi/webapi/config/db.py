from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:password#1@localhost:3306/db_crud_fastapi"
engine = create_engine(DATABASE_URL, echo=True, pool_size=20)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()