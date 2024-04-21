from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:12345@localhost:5432/zadanie11"
engine=create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
sesionlocal=sessionmaker(autocommit=False, autoflush=False, bind=engine )
def get_db():
    """A generator function to ingest a database session.

    This function creates a new local database session, returns it in the 'yield' block,
    and then closes the session in a 'finally' block to ensure that the
    Termination of the database connection. Used as a dependency in FastAPI
    to forward sessions to endpoints.

    Yields:
    Session: A new instance of the local database session."""
    db=sesionlocal()
    try:
        yield db
    finally:
        db.close()
