import sys
from monitor.session_manager import setup_session
from monitor.runner import run_monitor

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "setup":
        setup_session()
    else:
        run_monitor()

if __name__ == "__main__":
    main()
