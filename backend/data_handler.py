import pandas as pd
from pathlib import Path

# Path to store CSV data
DATA_PATH = Path(__file__).parent / "data"
CUSTOMERS_CSV = DATA_PATH / "customers.csv"

# Create data folder and file if not exist
DATA_PATH.mkdir(parents=True, exist_ok=True)
if not CUSTOMERS_CSV.exists():
    df = pd.DataFrame(columns=["id", "name", "phone", "email", "address", "due_amount"])
    df.to_csv(CUSTOMERS_CSV, index=False)


# ---------- Helper Functions ----------

def _read_csv():
    """Read customers from CSV file"""
    return pd.read_csv(CUSTOMERS_CSV)


def _write_csv(df):
    """Write customers to CSV file"""
    df.to_csv(CUSTOMERS_CSV, index=False)


def _get_next_id(customers_df):
    """Find the next available ID (start from 1, reuse deleted IDs)"""
    if customers_df.empty:
        return 1
    existing_ids = set(customers_df["id"].astype(int))
    new_id = 1
    while new_id in existing_ids:
        new_id += 1
    return new_id


# ---------- CRUD Operations ----------

def add_customer(customer):
    """Add a new customer"""
    customers_df = _read_csv()
    customer["id"] = _get_next_id(customers_df)  # assign simple ID
    new_df = pd.DataFrame([customer])
    customers_df = pd.concat([customers_df, new_df], ignore_index=True)
    _write_csv(customers_df)
    return customer


def get_all_customers():
    """Return all customers"""
    return _read_csv().to_dict(orient="records")


def get_customer(customer_id):
    """Get customer by ID"""
    customers_df = _read_csv()
    result = customers_df[customers_df["id"].astype(int) == int(customer_id)]
    if result.empty:
        return None
    return result.to_dict(orient="records")[0]


def update_customer(customer_id, updates):
    """Update details of a customer"""
    customers_df = _read_csv()
    mask = customers_df["id"].astype(int) == int(customer_id)
    if not mask.any():
        return None
    for key, value in updates.items():
        if key in customers_df.columns:
            customers_df.loc[mask, key] = value
    _write_csv(customers_df)
    return get_customer(customer_id)


def delete_customer(customer_id):
    """Delete a customer by ID"""
    customers_df = _read_csv()
    mask = customers_df["id"].astype(int) != int(customer_id)
    new_df = customers_df[mask]
    if len(new_df) == len(customers_df):  # no deletion happened
        return False
    _write_csv(new_df)
    return True


def delete_all_customers():
    """Delete all customers"""
    empty_df = pd.DataFrame(columns=["id", "name", "phone", "email", "address", "due_amount"])
    _write_csv(empty_df)
    return True
