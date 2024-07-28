import os
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.sql import text
from fastapi.middleware.cors import CORSMiddleware

# Ensure the tables are created
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

if os.getenv("ENVIRONMENT") == "production":
    origins = [
        "https://can-project-docker.vercel.app",
    ]
else:
    origins = [
        "http://localhost:8080",
    ]


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
    messages = db.query(models.CANMessage).offset(skip).limit(limit).all()
    return messages

@app.post("/api/messages", response_model=CANMessageCreate)
def create_message(message: CANMessageCreate, db: Session = Depends(get_db)):
    db_message = models.CANMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/api/db-check")
def read_root(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        return {"status": "Database is connected", "result": result[0]}
    except Exception as e:
        return {"status": "Database is not connected", "error": str(e)}
