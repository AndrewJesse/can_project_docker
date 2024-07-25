from .models import CANMessage

def read_can_message() -> CANMessage:
    return CANMessage(
        arbitration_id="123ABC",
        data="Some data",
        timestamp="2024-07-23 12:34:56"
    )
