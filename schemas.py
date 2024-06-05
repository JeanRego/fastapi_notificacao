from pydantic import BaseModel

class Notification(BaseModel):
    _id: str
    resource: str
    user_id: int
    topic: str
    application_id: int
    attempts: int
    sent: str
    received: str
