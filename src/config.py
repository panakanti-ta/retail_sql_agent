import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "retail_agent.db"

GATEWAY_URL = os.getenv("TIGER_AI_GATEWAY_URL", "")
GATEWAY_KEY = os.getenv("TIGER_AI_GATEWAY_API_KEY", "")
GATEWAY_MODEL = os.getenv("TIGER_AI_GATEWAY_MODEL", "gpt-4o-mini")
