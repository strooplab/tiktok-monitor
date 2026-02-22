# test simple
from bot.telegram_bot import send_alert
#from database.db import init.db

def main():
#    init_db()
    send_alert("Monitoreo Completado")

if __name__ == "__main__":
    main()
