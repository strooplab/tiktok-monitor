import requests
from config import TELEGRAM_TOKEN, CHAT_ID

# Envía una alerta con un mensaje
def send_alert(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    # Contenido del mensaje
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    # Almacena la respuesta del post
    response = requests.post(url, data=payload)
    
    # En caso de presentar error, realizamos un debug
    if response.status_code != 200:
        raise Exception(f"Error al enviar: {response.text}")

    return response.json()
