from playwright.sync_api import sync_playwright
import time
import re

from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def scrape_doctors():
    doctors = []

    with sync_playwright() as p:

        # Create new browser instance
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the doctor search page
        page.goto(f"{BASE_URL}/find-a-doctor/results", timeout=60000)

        # Wait for the page to load and the doctor cards to be visible
        page.wait_for_selector('.link_provider_display_name', timeout=60000)

        # Find all doctors
        doctor_div_list = page.locator('.link_provider_display_name').locator('..').locator('..').locator('..').locator('..').locator('..').locator('..')
        total_doctors = doctor_div_list.count()
        print(f"Found {total_doctors} doctor cards")

        # Iterate through each doctor and extract details
        for i in range(total_doctors):
            doctor = doctor_div_list.nth(i)

            try:
                name = doctor.locator(".link_provider_display_name").inner_text().strip()
                speciality = doctor.locator('span.Typography-sc-1xkl964-0.ldENbU[itemprop="medicalSpecialty"]').inner_text().strip()

                # Create profile URL from href
                profile_url = doctor.locator("a[data-testref='provider-name-link']").get_attribute("href")
                profile_url = f"https://www.andalusiahealth.com{profile_url}" if profile_url else None

                # Extract Rating
                rating = doctor.locator('span.styles__Span-sc-729csx-0.boQBnU[itemprop="ratingValue"]').inner_text().strip() if doctor.locator('span.styles__Span-sc-729csx-0.boQBnU[itemprop="ratingValue"]').count() > 0 else None
                if rating:
                    try:
                        rating = float(re.search(r"([\d.]+)", rating).group(1))
                    except ValueError:
                        rating = None

                # Extract landmark and address  
                landmark = doctor.locator('span.Typography-sc-1xkl964-0.koLreT[itemprop="name"]').inner_text().strip()
                address = doctor.locator('span[itemprop="streetAddress"] span').inner_text().strip()

                # Extract phone
                phone = doctor.locator("a[href^='tel:']").first.get_attribute("href")
                phone = phone.replace("tel:", "") if phone else None

                has_alternate_address = doctor.locator("a[data-testref='provider-cards-location']").count() > 0
                accepts_new_patients = doctor.locator('div[data-for="accepts-new-patients"]').count() > 0
                is_employed_provider = "Employed Provider" in doctor.inner_text()

                doctors.append({
                    "full_name": name,
                    "specialisation": speciality,
                    "rating": rating,
                    "profile_url": profile_url,
                    "landmark": landmark,
                    "address": address,
                    "phone": phone,
                    "multiple_locations": has_alternate_address,
                    "accepting_new_patients": accepts_new_patients,
                    "employed_provider": is_employed_provider
                })

            except Exception as e:
                print(f"❌ Skipping doctor {i} due to error: {e}")

        browser.close()
        return doctors
