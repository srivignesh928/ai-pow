from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent.parent

load_dotenv(PROJECT_ROOT / ".env")

DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "vehicle_master.db"
JSON_PATH = DATA_DIR / "vehicle_master.json"
UPLOAD_DIR = DATA_DIR / "uploads"

FRONTEND_DIR = PROJECT_ROOT / "frontend"

MODEL_VERSION = "v2.0"

ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/jpg",
}

MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024
MAX_IMAGE_DIMENSIONS = (1024, 1024)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")