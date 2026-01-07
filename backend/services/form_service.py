from db.mongo import forms_collection, responses_collection
from bson import ObjectId

class FormService:

    @staticmethod
    def create_form(form_data):
        return forms_collection.insert_one(form_data)

    @staticmethod
    def get_form(form_id):
        form = forms_collection.find_one({"_id": ObjectId(form_id)})
        if form:
            form["_id"] = str(form["_id"])
        return form

    @staticmethod
    def get_responses(form_id):
        responses = list(responses_collection.find({"formId": form_id}))
        for r in responses:
            r["_id"] = str(r["_id"])
        return responses
