import requests
from fastapi import HTTPException
from schemas import Notification

def handle_notification(notification: Notification):
    # Lógica para processar a notificação
    resource_url = f"https://api.mercadolibre.com{notification.resource}"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    response = requests.get(resource_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Processar os dados recebidos da API
        print(data)
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching resource from Mercado Libre API")
