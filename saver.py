import csv
import os
from datetime import datetime


OUTPUT_FILE = "jobs.csv"

FIELDS = ["title", "company", "location", "stipend", "duration", "link", "scraped_on"]


def save_to_csv(jobs: list[dict], filename: str = OUTPUT_FILE) -> None:
    """Save list of job dicts to a CSV file."""

    if not jobs:
        print("⚠️  No jobs to save.")
        return

    # Add a timestamp to each job
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    for job in jobs:
        job["scraped_on"] = today

    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)

        # Write header only if file is new
        if not file_exists:
            writer.writeheader()

        writer.writerows(jobs)

    print(f"💾 Saved {len(jobs)} jobs to '{filename}'")


def load_from_csv(filename: str = OUTPUT_FILE) -> list[dict]:
    """Load existing jobs from CSV (useful for deduplication later)."""
    if not os.path.exists(filename):
        return []

    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
