# TikTok Monitor Bot

Sistema de monitoreo automatizado para perfiles de TikTok que alerta vía Telegram cuando se detectan nuevos videos en el feed.

## Descripción

Este programa monitorea continuamente un perfil específico de TikTok y envía alertas a través de un bot de Telegram cuando se publican nuevos videos. Utiliza Playwright para automatizar la navegación y mantener una sesión persistente.

## Entorno Virtual

`python -m venv .venv`
`source .venv/bin/activate`  # Linux/Mac
# o
`.venv\Scripts\activate`  # Windows`

## Instala dependencias
`pip install -r requirements.txt`
`playwright install chromium`

## Instalación

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd nequi-monitor

## Setup
1. Ejecutar:
`python main.py setup`
Resolver el captcha de la página emergente
Presionar enter en el cli para almacenar la sesión autorizada

## Uso
1. Ejecutar:
`python main.py`
El runner comenzará a buscar videos, en caso de encontrar uno nuevo 
su bot de telegram enviará una alerta indicandole el id del video

# Proyecto en desarrollo, fases de producción:
- Estructura inicial ✅
- Telegram bot ✅
- IU Básica
# Copyright (c) 2026 Author. All Rights Reserved.
