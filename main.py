import time
from database.db import init_db, videos_exists, save_video
from monitor.tiktok_monitor import get_latest_videos
from bot.telegram_bot import send_alert
from config import TIKTOK_USERNAME # La cuenta a la que estamos monitoreando

def main():
    """Comprueba y avisa si se ha subido un nuevo video"""
    init_db()
    while True:
        videos = get_latest_videos()
        for video in videos:
            if not videos_exists(video):
                save_video(video)
                send_alert(f"Alerta! {TIKTOK_USERNAME} tiene nuevo video! id: {video}")
        time.sleep(20)

if __name__ == "__main__":
    main()

