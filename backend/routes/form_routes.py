from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from bson import ObjectId
from datetime import datetime
from utils.db import forms_collection
from utils.db import forms_collection, responses_collection


form_bp = Blueprint("forms", __name__)

# CREATE FORM
@form_bp.route("/create", methods=["POST"])
@jwt_required()
def create_form():
    data = request.json
    form = {
        "title": data["title"],
        "description": data.get("description", ""),
        "imageUrl": data.get("imageUrl"),
        "questions": data["questions"],
        "isActive": True,
        "createdAt": datetime.utcnow()
    }
    result = forms_collection.insert_one(form)
    return jsonify({"formId": str(result.inserted_id)})

# LIST FORMS (ADMIN DASHBOARD)
@form_bp.route("", methods=["GET"])
@jwt_required()
def list_forms():
    forms = list(forms_collection.find())

    for f in forms:
        fid = f["_id"]

        response_count = responses_collection.count_documents({
            "$or": [
                {"formId": ObjectId(fid)},
                {"formId": str(fid)}
            ]
        })

        f["_id"] = str(fid)
        f["responseCount"] = response_count

    return jsonify(forms)



# PUBLIC FORM (GET)
@form_bp.route("/<id>", methods=["GET"])
def get_public_form(id):
    form = forms_collection.find_one({"_id": ObjectId(id)})
    if not form or not form.get("isActive"):
        return jsonify({"error": "Form not available"}), 404

    form["_id"] = str(form["_id"])
    return jsonify(form)


# GET FORM (PUBLIC)
@form_bp.route("/admin/<id>", methods=["GET"])
@jwt_required()
def get_form_admin(id):
    form = forms_collection.find_one({"_id": ObjectId(id)})
    if not form:
        return jsonify({"error": "Form not found"}), 404

    form["_id"] = str(form["_id"])
    return jsonify(form)

# UPDATE FORM
@form_bp.route("/<id>", methods=["PUT"])
@jwt_required()
def update_form(id):
    data = request.json
    forms_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return jsonify({"message": "Form updated"})

# ENABLE / DISABLE
@form_bp.route("/<id>/toggle", methods=["PATCH"])
@jwt_required()
def toggle_form(id):
    form = forms_collection.find_one({"_id": ObjectId(id)})
    forms_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"isActive": not form["isActive"]}}
    )
    return jsonify({"message": "Toggled"})

#DELETE

@form_bp.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete_form(id):
    form_object_id = ObjectId(id)

    forms_collection.delete_one({"_id": form_object_id})

    # 🔥 ALSO DELETE RELATED RESPONSES
    responses_collection.delete_many({
        "$or": [
            {"formId": form_object_id},
            {"formId": id}
        ]
    })

    return jsonify({"message": "Form and responses deleted"})

