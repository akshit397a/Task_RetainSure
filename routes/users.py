from flask import Blueprint, request, jsonify
from services import user_services

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "User API is running"}), 200

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = user_services.get_all_users()
    return jsonify(users), 200

@user_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_services.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    response, status = user_services.create_user(data)
    return jsonify(response), status

@user_bp.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    response, status = user_services.update_user(user_id, data)
    return jsonify(response), status

@user_bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    response, status = user_services.delete_user(user_id)
    return jsonify(response), status

@user_bp.route("/search", methods=["GET"])
def search_user():
    name = request.args.get("name", "")
    results = user_services.search_user_by_name(name)
    return jsonify(results), 200

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response, status = user_services.login_user(data)
    return jsonify(response), status
