import json
import os
from collections import defaultdict

def run_analysis(doctors):
    total_doctors = len(doctors)
    doctors_with_ratings = 0  # placeholder if ratings are scraped
    phone_to_doctors = defaultdict(list)
    multi_location_doctors = []

    for doctor in doctors:
        if doctor.get("rating"):
            doctors_with_ratings += 1

        phone = doctor.get("phone")
        if phone:
            phone_to_doctors[phone].append(doctor)

        if doctor.get("multiple_locations", False):
            multi_location_doctors.append(doctor)

    duplicate_phone_doctors = {
        phone: entries for phone, entries in phone_to_doctors.items() if len(entries) > 1
    }

    return {
        "total_doctors": total_doctors,
        "doctors_with_ratings": doctors_with_ratings,
        "doctors_with_duplicate_phones": {
            phone: [doc["full_name"] for doc in docs]
            for phone, docs in duplicate_phone_doctors.items()
        },
        "doctors_with_multiple_locations": [
            doc["full_name"] for doc in multi_location_doctors
        ]
    }

def export_analysis(analysis_result, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(analysis_result, f, indent=2)

    print(f"Analysis exported to {file_path}")
