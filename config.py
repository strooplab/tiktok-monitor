import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
CONFIG_FILE = Path("config.json")
def get_username(): # Update: Ahora necesitamos el username digitado por el usuario
    if not CONFIG_FILE.exists():
        return None
    with open(CONFIG_FILE) as f:
        return json.load(f)["tiktok_username"]
TIKTOK_USERNAME = get_username()
URL_VIDEO = f"https://www.tiktok.com/@{TIKTOK_USERNAME}/video/"
DB_NAME = "videos.db" 
CHECK_INTERVAL = 300
