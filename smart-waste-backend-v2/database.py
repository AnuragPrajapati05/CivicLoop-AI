from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./waste_management.db")

# For SQLite, connect_args contains check_same_thread=False
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def initialize_database():
    """Create any missing tables using the application's registered models.

    ``create_all`` is additive: it preserves existing tables and rows while
    creating tables that do not yet exist. Importing models here ensures all
    SQLAlchemy model metadata is registered before the operation runs.
    """
    import models  # noqa: F401  (registers the model classes with Base.metadata)

    Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
