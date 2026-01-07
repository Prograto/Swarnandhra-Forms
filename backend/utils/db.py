from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["college_forms"]

forms_collection = db["forms"]
responses_collection = db["responses"]
