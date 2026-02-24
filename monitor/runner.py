import time
from playwright.sync_api import sync_playwright
from monitor.tiktok_monitor import get_latest_videos
from monitor.session_manager import SESSION_FILE
from database.db import init_db, videos_exists, save_video
from bot.telegram_bot import send_alert
from config import TIKTOK_USERNAME, URL_VIDEO
from pathlib import Path
import json

CONFIG_FILE = Path("config.json")
init_db() # Inicializar la db 
def get_username(): # Update: Ahora necesitamos el username digitado por el usuario
    with open(CONFIG_FILE) as f:
        return json.load(f)["tiktok_username"]

def run_monitor():
    TIKTOK_USERNAME = get_username()
    if not SESSION_FILE.exists():
        raise RuntimeError("No existe sesión. Ejecuta primero: python main.py setup")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=str(SESSION_FILE))
        while True:
            videos = get_latest_videos(context)

            for video in videos:
                if not videos_exists(video):
                    save_video(video)
                    send_alert(f"Alerta! se ha encontrado un video nuevo de {TIKTOK_USERNAME}, video: {URL_VIDEO + video}")
            time.sleep(10)

