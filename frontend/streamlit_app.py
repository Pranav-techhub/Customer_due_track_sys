import streamlit as st
import requests
from charts import plot_top_dues

API_URL = "http://localhost:5000"

st.set_page_config(page_title="Customer Due Tracking", layout="wide")

menu = ["Add Customer", "View All", "Sort by Due", "Update Customer", "Delete Customer", "Charts"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Customer":
    st.header("Add Customer")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    address = st.text_area("Address")
    due_amount = st.number_input("Due Amount", min_value=0.0)
    if st.button("Add"):
        res = requests.post(f"{API_URL}/customers", json={
            "name": name, "phone": phone, "email": email,
            "address": address, "due_amount": due_amount
        })
        st.success(res.json().get("message"))

elif choice == "View All":
    st.header("All Customers")
    res = requests.get(f"{API_URL}/customers")
    st.dataframe(res.json())

elif choice == "Sort by Due":
    st.header("Sort Customers by Due Amount")
    order = st.radio("Order", ["Ascending", "Descending"])
    res = requests.get(f"{API_URL}/customers/sort", params={"order": "asc" if order=="Ascending" else "desc"})
    st.dataframe(res.json())

elif choice == "Update Customer":
    st.header("Update Customer")
    cust_id = st.number_input("Customer ID", min_value=1)
    updates = {}
    if st.checkbox("Update Name"): updates["name"] = st.text_input("New Name")
    if st.checkbox("Update Phone"): updates["phone"] = st.text_input("New Phone")
    if st.checkbox("Update Email"): updates["email"] = st.text_input("New Email")
    if st.checkbox("Update Address"): updates["address"] = st.text_area("New Address")
    if st.checkbox("Update Due Amount"): updates["due_amount"] = st.number_input("New Due", min_value=0.0)
    if st.button("Update"):
        res = requests.put(f"{API_URL}/customers/{cust_id}", json=updates)
        st.success(res.json().get("message"))

elif choice == "Delete Customer":
    st.header("Delete Customer")
    mode = st.radio("Delete Mode", ["Single", "All"])
    if mode == "Single":
        cust_id = st.number_input("Customer ID", min_value=1)
        if st.button("Delete"):
            res = requests.delete(f"{API_URL}/customers/{cust_id}")
            st.success(res.json().get("message"))
    else:
        if st.button("Delete All Customers"):
            res = requests.delete(f"{API_URL}/customers")
            st.success(res.json().get("message"))

elif choice == "Charts":
    st.header("Top Dues Chart")
    res = requests.get(f"{API_URL}/customers")
    plt = plot_top_dues(res.json(), top_n=5)
    st.pyplot(plt)
