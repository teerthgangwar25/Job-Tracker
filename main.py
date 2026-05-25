from paginator import scrape_all_pages
from saver import save_to_csv


def main():
    print("=" * 45)
    print("       🧑‍💻 Internshala Job Scraper")
    print("=" * 45)

    # --- Config ---
    keyword   = input("\nEnter job keyword (e.g. python, web dev): ").strip()
    max_pages = input("How many pages to scrape? (default 3): ").strip()
    max_pages = int(max_pages) if max_pages.isdigit() else 3

    # --- Scrape ---
    jobs = scrape_all_pages(keyword, max_pages=max_pages)

    # --- Save ---
    if jobs:
        save_to_csv(jobs)
        print("\n🎉 Done! Check 'jobs.csv' for your results.")
    else:
        print("\n😕 No jobs found. Try a different keyword.")


if __name__ == "__main__":
    main()
