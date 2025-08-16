import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"
CUSTOMERS_CSV = DATA_PATH / "customers.csv"

# Ensure data folder exists
DATA_PATH.mkdir(exist_ok=True)

# ---------- Read Customers ----------
def read_customers():
    if not CUSTOMERS_CSV.exists():
        return []
    with open(CUSTOMERS_CSV, newline="", encoding="utf-8") as f:
        return [ { "id": int(row["id"]), "name": row["name"], "phone": row["phone"],
                   "email": row["email"], "address": row["address"], "due_amount": float(row["due_amount"]) }
                 for row in csv.DictReader(f) ]

# ---------- Write Customers ----------
def write_customers(customers):
    with open(CUSTOMERS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "phone", "email", "address", "due_amount"])
        writer.writeheader()
        for c in customers:
            writer.writerow(c)
