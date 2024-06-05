from fastapi import FastAPI, Request, HTTPException
from schemas import Notification
from notification_handler import handle_notification

app = FastAPI()

@app.post("/notifications")
async def receive_notification(notification: Notification):
    handle_notification(notification)
    return {"message": "Notification received successfully"}
