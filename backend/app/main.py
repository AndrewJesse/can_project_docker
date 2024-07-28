import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.sql import text

# Ensure the tables are created
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

logging.basicConfig(level=logging.INFO)

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

@app.get("/messages")
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logging.info("GET /messages called")
    messages = db.query(models.CANMessage).offset(skip).limit(limit).all()
    return messages

@app.post("/messages", response_model=CANMessageCreate)
def create_message(message: CANMessageCreate, db: Session = Depends(get_db)):
    logging.info("POST /messages called")
    db_message = models.CANMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/db-check")
def read_root(db: Session = Depends(get_db)):
    logging.info("GET /db-check called")
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        return {"status": "Database is connected", "result": result[0]}
    except Exception as e:
        return {"status": "Database is not connected", "error": str(e)}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://can-project-docker.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
