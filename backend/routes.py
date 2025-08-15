from flask import request, jsonify
from .data_handler import (
    add_customer, get_all_customers, get_customer_by_id,
    update_customer, delete_customer, delete_all_customers
)

def register_routes(app):

    @app.route("/customers", methods=["POST"])
    def create_customer():
        data = request.json
        if not data or "name" not in data or "phone" not in data or "due_amount" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        add_customer(data)
        return jsonify({"message": "Customer added successfully"}), 201

    @app.route("/customers", methods=["GET"])
    def list_customers():
        customers = get_all_customers()
        return jsonify(customers), 200

    @app.route("/customers/<customer_id>", methods=["GET"])
    def get_customer(customer_id):
        customer = get_customer_by_id(customer_id)
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify(customer), 200

    @app.route("/customers/<customer_id>", methods=["PUT"])
    def edit_customer(customer_id):
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        updated = update_customer(customer_id, data)
        if not updated:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify({"message": "Customer updated successfully"}), 200

    @app.route("/customers/<customer_id>", methods=["DELETE"])
    def remove_customer(customer_id):
        deleted = delete_customer(customer_id)
        if not deleted:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify({"message": "Customer deleted successfully"}), 200

    @app.route("/customers", methods=["DELETE"])
    def remove_all_customers():
        delete_all_customers()
        return jsonify({"message": "All customers deleted successfully"}), 200
