from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from utils.db import db

auth_bp = Blueprint("auth", __name__)
admins = db.admins

@auth_bp.route("/login", methods=["POST"])
def admin_login():
    data = request.json
    admin = admins.find_one({
        "email": data["email"],
        "password": data["password"]
    })

    if not admin:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(admin["_id"]))
    return jsonify({"token": token})
