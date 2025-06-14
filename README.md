# Web Scraper – Andalusia Health

This project is a technical test to build a web crawler that extracts medical professionals' details from the Andalusia Health website and stores them in a MongoDB database. The project also includes basic data analysis and reporting.

---

## 🔧 Tech Stack

- **Python 3**
- **Playwright** (for web scraping)
- **MongoDB Atlas** (for cloud data storage)
- **pymongo**, **pandas**, **dotenv**

---

## 📌 Features

- Scrapes doctor data from:  
  [https://www.andalusiahealth.com/find-a-doctor/results](https://www.andalusiahealth.com/find-a-doctor/results)

- Extracted fields:
  - Full Name
  - Profile URL
  - Speciality
  - Address & Landmark
  - Phone Number
  - Multiple Location (Yes/No)
  - Accepts New Patients (Yes/No)
  - Employed Provider (Yes/No)
  - Ratings (if available)

- Stores data in MongoDB
- Generates reports on:
  - Total doctors
  - Doctors with ratings
  - Duplicate phone numbers
  - Doctors with multiple locations

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/web-scrapper.git -b master
cd web-scrapper
