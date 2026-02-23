import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TIKTOK_USERNAME = os.getenv("TIKTOK_USERNAME")
DB_NAME = os.getenv("DB_NAME")
CHECK_INTERVAL = 300
