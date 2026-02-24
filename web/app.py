""" Controlador de interfaz gráfica """
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request  
import threading
import json 
from pathlib import Path

#from monitor.runner import run_monitor 
from database.db import get_all_videos
from core.service import MonitorService

CONFIG_FILE = Path("config.json")

app = FastAPI() # Inicializámos la API Web
templates = Jinja2Templates(directory="web/templates") # Carga de templates
service = MonitorService()
monitor_thread = None
monitor_running = False

# Necesario guardar la configuración para recuperarla más tarde
def save_config(username: str):
    with open(CONFIG_FILE, "w") as f:
    # En nuestro CONFIG_FILE debe estar esta información
        json.dump({"tiktok_username": username}, f)

def load_config():
    if not CONFIG_FILE.exists():
        return None # Devuelve nulo si no existe un CONFIG_FILE
    with open(CONFIG_FILE) as f:
        return json.load(f) # Cargamos si existe

"""
    ENDPOINTS
"""
# Ruta Home (inicio)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    config = load_config()
    videos = get_all_videos() # Obtenemos todos los videos en db
    return templates.TemplateResponse("index.html", {
        "request": request, # Rellenamos los campos con info
        "config": config,
        "videos": videos,
        "running": monitor_running
    })
# Guardar username de tiktok en la db para procesamiento posterior (Persistencia)
@app.post("/save")
def save(
    username: str = Form(...),
    telegram_token: str = Form(...),
    chat_id: str = Form(...)
):
    with open(CONFIG_FILE, "w") as f:
        json.dump({
            "tiktok_username": username,
            "telegram_token": telegram_token,
            "chat_id": chat_id
        }, f)

    return RedirectResponse("/", status_code=303)

@app.post("/start")
def start():
    service.start()
    return RedirectResponse("/", status_code=303)

@app.post("/setup")
def setup():
    service.setup()
    return RedirectResponse("/", status_code=303)
