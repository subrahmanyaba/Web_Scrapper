from pymongo import MongoClient
import os
from dotenv import load_dotenv
import csv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

def get_mongo_client():
    return MongoClient(MONGO_URL)

def save_to_mongo(data, db_name="andalusia", collection_name="doctors"):
    client = get_mongo_client()
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many({})  # clean slate
    collection.insert_many(data)
    print("Data saved to MongoDB")

def export_csv(data, file_path):
    if not data:
        print("No data to export.")
        return

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    fieldnames = sorted(set().union(*(d.keys() for d in data)))

    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"CSV exported to {file_path}")
