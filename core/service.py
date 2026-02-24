import threading
from monitor.runner import run_monitor
from monitor.session_manager import setup_session

class MonitorService:
    def __init__(self):
        self.thread = None
        self.running = False

    def start(self):
        if not self.running:
            self.thread = threading.Thread(target=run_monitor, daemon=True)
            self.thread.start()
            self.running = True

    def stop(self):
        self.running = False  # hay que mejorar esto

    def setup(self):
        setup_session()
