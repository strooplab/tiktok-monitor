import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TIKTOK_USERNAME = os.getenv("TIKTOK_USERNAME")
CHECK_INTERVAL = 300
