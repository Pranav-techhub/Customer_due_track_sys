import pandas as pd
from .config import CUSTOMERS_CSV

def load_customers():
    try:
        return pd.read_csv(CUSTOMERS_CSV)
    except FileNotFoundError:
        return pd.DataFrame(columns=["id", "name", "phone", "email", "address", "due_amount"])

def save_customers(df):
    df.to_csv(CUSTOMERS_CSV, index=False)
