import time
from scraper import get_page, parse_jobs


def scrape_all_pages(keyword: str, max_pages: int = 5) -> list[dict]:
    """
    Loop through pages and collect all job listings.

    Args:
        keyword:   Search term e.g. "python", "web development"
        max_pages: Max number of pages to scrape (default: 5)

    Returns:
        List of job dicts
    """
    all_jobs = []
    seen_links = set()  # Track links to avoid duplicates

    print(f"\n🔍 Searching for '{keyword}' internships...\n")

    for page in range(1, max_pages + 1):
        print(f"📄 Page {page}/{max_pages}")

        soup = get_page(keyword, page)

        if soup is None:
            print("  Stopping — failed to fetch page.")
            break

        jobs = parse_jobs(soup)

        if not jobs:
            print("  No more listings found. Stopping.")
            break

        # Deduplicate by link
        new_jobs = []
        for job in jobs:
            if job["link"] not in seen_links:
                seen_links.add(job["link"])
                new_jobs.append(job)

        all_jobs.extend(new_jobs)
        print(f"  ✅ Found {len(new_jobs)} listings (total so far: {len(all_jobs)})")

        # Be polite — wait 2 seconds between requests
        if page < max_pages:
            time.sleep(2)

    print(f"\n✅ Scraping complete! Total jobs collected: {len(all_jobs)}")
    return all_jobs
