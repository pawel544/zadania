from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:12345@localhost:5432/zadanie11"
engine=create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
sesionlocal=sessionmaker(autocommit=False, autoflush=False, bind=engine )
def get_db():
    db=sesionlocal()
    try:
        yield db
    finally:
        db.close()
