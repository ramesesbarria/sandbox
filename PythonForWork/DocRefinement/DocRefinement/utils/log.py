from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

HELPER_DIR = os.path.dirname(os.path.abspath(__file__))

WORKING_DIR = os.path.dirname(HELPER_DIR)

LOG_PATH = os.getenv("AA_LOG_PATH", os.path.join(WORKING_DIR, "logs", "logs.txt"))
DEBUG_MODE = os.getenv("AA_DEBUG", "False").lower() == "true"

log_dir = os.path.dirname(LOG_PATH)

if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def log_message(message):
    """Append a timestamped message to logs.txt"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    if DEBUG_MODE:
        print(f"[DEBUG] {message}")