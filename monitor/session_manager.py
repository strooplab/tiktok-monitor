from pathlib import Path
from playwright.sync_api import Browser, sync_playwright
from config import TIKTOK_USERNAME

SESSION_FILE = Path("tiktok_session.json")

def setup_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(f"https://www.tiktok.com/@{TIKTOK_USERNAME}")
        input("Resuelve captcha y presiona ENTER...")

        context.storage_state(path=str(SESSION_FILE))
        print("Sesión guardada")

        return context
