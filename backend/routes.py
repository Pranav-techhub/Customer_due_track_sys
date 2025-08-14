from flask import Blueprint, request, jsonify
from . import data_handler as dh

bp = Blueprint("routes", __name__)

@bp.route("/customers", methods=["POST"])
def add_customer():
    data = request.json
    return jsonify(dh.add_customer(**data))

@bp.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(dh.get_all_customers())

@bp.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    cust = dh.get_customer_by_id(customer_id)
    return jsonify(cust) if cust else ({"error": "Not found"}, 404)

@bp.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    updates = request.json
    return jsonify(dh.update_customer(customer_id, updates))

@bp.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    return jsonify(dh.delete_customer(customer_id))

@bp.route("/customers", methods=["DELETE"])
def delete_all():
    return jsonify(dh.delete_all_customers())

@bp.route("/customers/sort", methods=["GET"])
def sort_customers():
    order = request.args.get("order", "asc") == "asc"
    return jsonify(dh.sort_customers_by_due(order))
