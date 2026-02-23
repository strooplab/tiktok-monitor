import time
from playwright.sync_api import sync_playwright
from monitor.tiktok_monitor import get_latest_videos
from monitor.session_manager import SESSION_FILE
from database.db import init_db, videos_exists, save_video
from bot.telegram_bot import send_alert
from config import TIKTOK_USERNAME

def run_monitor():
    if not SESSION_FILE.exists():
        raise RuntimeError("No existe sesión. Ejecuta primero: python main.py setup")
    init_db()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=str(SESSION_FILE))
        while True:
            videos = get_latest_videos(context)

            for video in videos:
                if not videos_exists(video):
                    save_video(video)
                    send_alert(f"Alerta! se ha encontrado un video nuevo de {TIKTOK_USERNAME}, id: {video}")
            time.sleep(10)
        browser.close()

