import os
from dotenv import load_dotenv
from pathlib import Path

# load_dotenv() 

base_path = Path(__file__).parent

env_path = base_path / ".env"
load_dotenv(dotenv_path=env_path)

DOC_PATH = os.getenv("AA_DOC_DOWNLOAD_PATH")
UPDATED_PATH = os.getenv("AA_DOC_SAVE_PATH")

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")