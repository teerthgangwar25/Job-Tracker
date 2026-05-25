import requests
from bs4 import BeautifulSoup
import time

# Fake browser headers so Internshala doesn't block us
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

BASE_URL = "https://internshala.com/internships/keywords-{keyword}/page-{page}"


def get_page(keyword: str, page: int) -> BeautifulSoup | None:
    """Fetch a single page and return a BeautifulSoup object."""
    url = BASE_URL.format(keyword=keyword.replace(" ", "%20"), page=page)
    print(f"  Fetching: {url}")

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise error if status != 200
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Failed to fetch page {page}: {e}")
        return None


def parse_jobs(soup: BeautifulSoup) -> list[dict]:
    """Extract job data from a parsed page."""
    jobs = []

    listings = soup.find_all("div", class_="individual_internship")

    if not listings:
        return jobs  # Empty = no more pages

    for listing in listings:
        try:
            # TITLE — inside <a id="job_title"> inside <h2>
            title_tag = listing.find("a", id="job_title")

            # COMPANY — inside <p class="company-name">
            company = listing.find("p", class_="company-name")

            # LOCATION — inside <div class="locations"> then <a> tag
            location_div = listing.find("div", class_="locations")
            location_tag = location_div.find("a") if location_div else None

            # STIPEND — inside <span class="stipend">
            stipend = listing.find("span", class_="stipend")

            # DURATION — 3rd <div class="row-1-item">, find by calendar icon sibling
            duration = None
            for item in listing.find_all("div", class_="row-1-item"):
                if item.find("i", class_="ic-16-calendar"):
                    duration = item.find("span")
                    break

            # LINK — data-href attribute on the main card div
            link = listing.get("data-href", "N/A")
            if link != "N/A":
                link = "https://internshala.com" + link

            job = {
                "title":    title_tag.get_text(strip=True)    if title_tag    else "N/A",
                "company":  company.get_text(strip=True)       if company      else "N/A",
                "location": location_tag.get_text(strip=True)  if location_tag else "N/A",
                "stipend":  stipend.get_text(strip=True)       if stipend      else "N/A",
                "duration": duration.get_text(strip=True)      if duration     else "N/A",
                "link":     link,
            }
            jobs.append(job)

        except Exception as e:
            print(f"  ⚠️  Skipped one listing due to error: {e}")
            continue

    return jobs