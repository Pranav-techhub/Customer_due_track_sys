import csv
from pathlib import Path
import uuid

DATA_PATH = Path(__file__).parent / "data"
CUSTOMERS_CSV = DATA_PATH / "customers.csv"

# Ensure CSV exists
if not CUSTOMERS_CSV.exists():
    DATA_PATH.mkdir(exist_ok=True)
    with open(CUSTOMERS_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "phone", "email", "address", "due_amount"])
        writer.writeheader()

def read_csv():
    with open(CUSTOMERS_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv(data):
    with open(CUSTOMERS_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "phone", "email", "address", "due_amount"])
        writer.writeheader()
        writer.writerows(data)

def add_customer(data):
    customers = read_csv()
    customers.append({
        "id": str(uuid.uuid4()),
        "name": data.get("name", ""),
        "phone": data.get("phone", ""),
        "email": data.get("email", ""),
        "address": data.get("address", ""),
        "due_amount": str(data.get("due_amount", 0))
    })
    write_csv(customers)

def get_all_customers():
    return read_csv()

def get_customer_by_id(customer_id):
    customers = read_csv()
    return next((c for c in customers if c["id"] == customer_id), None)

def update_customer(customer_id, new_data):
    customers = read_csv()
    updated = False
    for c in customers:
        if c["id"] == customer_id:
            c.update(new_data)
            updated = True
            break
    if updated:
        write_csv(customers)
    return updated

def delete_customer(customer_id):
    customers = read_csv()
    new_customers = [c for c in customers if c["id"] != customer_id]
    if len(new_customers) == len(customers):
        return False
    write_csv(new_customers)
    return True

def delete_all_customers():
    write_csv([])
