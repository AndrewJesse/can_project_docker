import os
import logging
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.sql import text
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)

# Ensure the tables are created
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

environment = os.getenv("ENVIRONMENT")
logging.info(f"Running in {environment} environment")

if environment == "production":
    origins = [
        "https://can-project-docker.vercel.app",
    ]
else:
    origins = [
        "http://localhost:8080",
    ]

logging.info(f"Configured CORS for origins: {origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CANMessageCreate(BaseModel):
    arbitration_id: str
    data: str
    timestamp: datetime

@app.get("/api/messages")
def read_messages(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    logging.info("Fetching messages from the database")
    messages = db.query(models.CANMessage).offset(skip).limit(limit).all()
    logging.info(f"Fetched {len(messages)} messages")
    return messages

@app.post("/api/messages", response_model=CANMessageCreate)
def create_message(message: CANMessageCreate, db: Session = Depends(get_db)):
    logging.info(f"Creating message: {message}")
    db_message = models.CANMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    logging.info(f"Created message: {db_message}")
    return db_message

@app.get("/api/db-check")
def read_root(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        logging.info("Database connection successful")
        return {"status": "Database is connected", "result": result[0]}
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        return {"status": "Database is not connected", "error": str(e)}
