import pandas as pd
from .utils import load_customers, save_customers
from .decorators import log_action

@log_action("ADD")
def add_customer(name, phone, email, address, due_amount):
    df = load_customers()
    new_id = df["id"].max() + 1 if not df.empty else 1
    df = pd.concat([df, pd.DataFrame([{
        "id": new_id,
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "due_amount": float(due_amount)
    }])], ignore_index=True)
    save_customers(df)
    return {"message": "Customer added successfully", "id": new_id}

@log_action("DELETE")
def delete_customer(customer_id):
    df = load_customers()
    df = df[df["id"] != customer_id]
    save_customers(df)
    return {"message": "Customer deleted"}

@log_action("DELETE_ALL")
def delete_all_customers():
    save_customers(pd.DataFrame(columns=["id", "name", "phone", "email", "address", "due_amount"]))
    return {"message": "All customers deleted"}

def get_all_customers():
    return load_customers().to_dict(orient="records")

def get_customer_by_id(customer_id):
    df = load_customers()
    customer = df[df["id"] == customer_id]
    return customer.to_dict(orient="records")[0] if not customer.empty else None

@log_action("UPDATE")
def update_customer(customer_id, updates):
    df = load_customers()
    idx = df[df["id"] == customer_id].index
    if idx.empty:
        return {"message": "Customer not found"}
    for key, value in updates.items():
        df.at[idx[0], key] = value
    save_customers(df)
    return {"message": "Customer updated"}

def sort_customers_by_due(ascending=True):
    df = load_customers()
    return df.sort_values(by="due_amount", ascending=ascending).to_dict(orient="records")
