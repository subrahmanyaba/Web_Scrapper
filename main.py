from scrapers.andalusia_scraper import scrape_doctors
from database.mongodb import save_to_mongo, export_csv
from analyse.data_analysis import run_analysis, export_analysis

def main():

    # Scraping section
    print(f"[Searching] {'Starting doctor scraping...'}")
    doctors = scrape_doctors()
    print(f"[Searching] Scraped {len(doctors)} doctors")
    print(('*-*'*20))


    # DB section
    print("[Saving] Saving to MongoDB...")
    save_to_mongo(doctors)
    print(('*-*'*20))

    # Exporting section
    print("[Exporting] Exporting data to CSV...")
    export_csv(doctors, "exports/doctors.csv")
    print(('*-*'*20))

    # Analysis section
    print("[Analyzing] Running analysis...")
    analysis_result = run_analysis(doctors)
    print("[Exporting] Exporting analysis to JSON...")
    export_analysis(analysis_result, "exports/analysis.json")
    print("[Exporting] All tasks complete!")

if __name__ == "__main__":
    main()
