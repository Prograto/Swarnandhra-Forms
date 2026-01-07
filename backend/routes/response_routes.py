from flask import Blueprint, request, jsonify
from utils.db import responses_collection
from datetime import datetime
import flask

response_bp = Blueprint("responses", __name__)

@response_bp.route("/submit", methods=["POST"])
def submit_response():
    data = request.json
    responses_collection.insert_one({
        "formId": data["formId"],
        "answers": data["answers"],
        "submittedAt": datetime.utcnow()
    })
    return jsonify({"message": "Submitted"})

# ✅ Allow OPTIONS without JWT
@response_bp.route("/form/<form_id>", methods=["GET", "OPTIONS"])
def get_form_responses(form_id):
    if flask.request.method == "OPTIONS":
        return jsonify({}), 200

    # JWT only for GET
    from flask_jwt_extended import verify_jwt_in_request
    verify_jwt_in_request()

    responses = list(responses_collection.find({"formId": form_id}))
    for r in responses:
        r["_id"] = str(r["_id"])
    return jsonify(responses)


