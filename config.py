import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "ai_logistics_control_tower_secret_key_2026")
    DATABASE_PATH = os.path.join(BASE_DIR, "database", "logistics.db")
    ML_MODEL_DIR = os.path.join(BASE_DIR, "ml_engine")
    DEBUG = True
    PORT = 5000
    HOST = "127.0.0.1"

    # GPS Map & Routing Engine Configuration (OSRM & OpenRouteService)
    ORS_API_KEY = os.environ.get("ORS_API_KEY", "")
    OSRM_API_KEY = os.environ.get("OSRM_API_KEY", "")
    OSRM_BASE_URL = os.environ.get("OSRM_BASE_URL", "https://router.project-osrm.org")
    DEFAULT_ROUTING_PROVIDER = os.environ.get("DEFAULT_ROUTING_PROVIDER", "osrm") # "osrm" or "openrouteservice"
