from flask import Blueprint, request, jsonify
from data_handler import read_customers, write_customers

customer_bp = Blueprint("customers", __name__)

# ---------- View Customers ----------
@customer_bp.route("/customers", methods=["GET"])
def get_customers():
    customers = read_customers()
    return jsonify(customers), 200

# ---------- Add Customer ----------
@customer_bp.route("/customers", methods=["POST"])
def add_customer():
    data = request.json
    if not data or "name" not in data or "phone" not in data:
        return jsonify({"error": "Name and Phone are required"}), 400

    customers = read_customers()

    # Assign ID serially
    existing_ids = [c["id"] for c in customers]
    new_id = 1
    while new_id in existing_ids:
        new_id += 1

    data["id"] = new_id
    customers.append(data)
    write_customers(customers)

    return jsonify({"message": "Customer added successfully", "id": new_id}), 201

# ---------- Update Customer ----------
@customer_bp.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    customers = read_customers()
    customer = next((c for c in customers if c["id"] == customer_id), None)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    updates = request.json
    if not updates:
        return jsonify({"error": "No updates provided"}), 400

    customer.update(updates)
    write_customers(customers)
    return jsonify({"message": "Customer updated successfully"}), 200

# ---------- Delete Customer ----------
@customer_bp.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customers = read_customers()
    updated_customers = [c for c in customers if c["id"] != customer_id]

    if len(customers) == len(updated_customers):
        return jsonify({"error": "Customer not found"}), 404

    write_customers(updated_customers)
    return jsonify({"message": "Customer deleted successfully"}), 200

# ---------- Delete All ----------
@customer_bp.route("/customers", methods=["DELETE"])
def delete_all_customers():
    write_customers([])
    return jsonify({"message": "All customers deleted"}), 200
