from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data"

CUSTOMERS_CSV = DATA_PATH / "customers.csv"
LOGS_CSV = DATA_PATH / "logs.csv"

# Ensure data folder exists
DATA_PATH.mkdir(exist_ok=True)
