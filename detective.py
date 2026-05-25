import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

url = "https://internshala.com/internships/keywords-python/page-1"
response = requests.get(url, headers=HEADERS, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

# Print first job card's full HTML
cards = soup.find_all("div", class_="individual_internship")
print(f"Found {len(cards)} cards\n")

if cards:
    print("=== FIRST CARD HTML ===")
    print(cards[0].prettify())