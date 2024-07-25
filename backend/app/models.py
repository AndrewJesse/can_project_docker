from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class CANMessage(Base):
    __tablename__ = "can_messages"

    id = Column(Integer, primary_key=True, index=True)
    arbitration_id = Column(String, index=True)
    data = Column(String)
    timestamp = Column(DateTime)
