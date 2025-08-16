from flask import jsonify, request
from . import data_handler


def register_routes(app):

    @app.route("/customers", methods=["GET"])
    def get_customers():
        customers = data_handler.get_all_customers()
        return jsonify(customers)

    @app.route("/customers/<int:customer_id>", methods=["GET"])
    def get_single_customer(customer_id):
        customer = data_handler.get_customer(customer_id)
        if customer:
            return jsonify(customer)
        return jsonify({"error": "Customer not found"}), 404

    @app.route("/customers", methods=["POST"])
    def add_customer():
        data = request.json
        required = ["name", "phone", "due_amount"]
        if not all(field in data for field in required):
            return jsonify({"error": "Missing required fields"}), 400
        customer = data_handler.add_customer(data)
        return jsonify({"message": "Customer added successfully", "customer": customer})

    @app.route("/customers/<int:customer_id>", methods=["PUT"])
    def update_customer(customer_id):
        data = request.json
        customer = data_handler.update_customer(customer_id, data)
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify({"message": "Customer updated successfully", "customer": customer})

    @app.route("/customers/<int:customer_id>", methods=["DELETE"])
    def delete_customer(customer_id):
        deleted = data_handler.delete_customer(customer_id)
        if not deleted:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify({"message": "Customer deleted successfully"})

    @app.route("/customers", methods=["DELETE"])
    def delete_all():
        data_handler.delete_all_customers()
        return jsonify({"message": "All customers deleted successfully"})
