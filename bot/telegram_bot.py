import requests
import json
from pathlib import Path

CONFIG_FILE = Path("config.json")

def get_telegram_config():
    with open(CONFIG_FILE) as f:
        data = json.load(f)
        return data["telegram_token"], data["chat_id"]

# Envía una alerta con un mensaje
def send_alert(message: str):
    token, chat_id = get_telegram_config()
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Contenido del mensaje
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    # Almacena la respuesta del post
    response = requests.post(url, data=payload)
    
    # En caso de presentar error, realizamos un debug
    if response.status_code != 200:
        raise Exception(f"Error al enviar: {response.text}")

    return response.json()
