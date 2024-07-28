import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get the environment variable to check the environment (development/production)
environment = os.getenv("ENVIRONMENT", "development")

# Define the database URL based on the environment
if environment == "development":
    SQLALCHEMY_DATABASE_URL = "sqlite:///./can_project.db"
else:
    # Use an absolute path to the database file in production
    SQLALCHEMY_DATABASE_URL = "sqlite:////app/can_project.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
