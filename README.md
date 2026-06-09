<div align="center">
  <h1>📋 Internshala Job Scraper</h1>
  <p>A Python web scraper that collects internship listings from Internshala based on any keyword and saves them to a CSV file for easy viewing and filtering.</p>
  
  <p>
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License MIT">
    <img src="https://img.shields.io/badge/status-active-success.svg" alt="Status Active">
  </p>
</div>

---

## 📑 Table of Contents

- [ Sample Output](#-sample-output)
- [ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚙️ Setup & Installation](#️-setup--installation)
- [ How It Works](#-how-it-works)
- [ Data Collected](#-data-collected)
- [🚀 Features](#-features)
- [⚠️ Troubleshooting](#️-troubleshooting)
- [ Possible Upgrades](#-possible-upgrades)
- [📄 License](#-license)

---

## Sample Output

| title | company | location | stipend | duration | link | scraped_on |
|---|---|---|---|---|---|---|
| Full Stack Development | Freelance Trainings | Ahmedabad | ₹ 2,000 - 2,100 /month | 4 Months | https://internshala.com/... | 2026-05-17 11:02 |
| Python Developer | TechCorp | Remote | ₹ 5,000 /month | 3 Months | https://internshala.com/... | 2026-05-17 11:02 |

---

## Tech Stack

- **Python 3.8+**
- **requests** — fetching web pages
- **BeautifulSoup4** — parsing HTML
- **csv** — saving data
- **schedule** *(optional)* — running automatically on a timer

---

## 📁 Project Structure

```text
job-scraper/
│
├── main.py          # Entry point — run this file
├── scraper.py       # Fetches and parses each page
├── paginator.py     # Loops through multiple pages, handles deduplication
├── saver.py         # Saves results to jobs.csv
├── detective.py     # Debug tool — prints raw HTML of a job card
├── jobs.csv         # Scraped output (auto-generated on first run)
├── requirements.txt # Python dependencies
└── README.md        # You are here
```

---

## ⚙️ Setup & Installation

### 1. Clone or download the project

```bash
git clone https://github.com/teerthgangwar25/job-scraper.git
cd job-scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the scraper

```bash
python main.py
```

### 4. Follow the prompts

```text
Enter job keyword (e.g. python, web dev): python
How many pages to scrape? (default 3): 3
```

### 5. Check your results

Open `jobs.csv` in Excel, Google Sheets, or any text editor.

---

## How It Works

```text
main.py  →  paginator.py  →  scraper.py  →  Internshala
                                                  ↓
                          saver.py      ←  job listings
                              ↓
                          jobs.csv
```

1. `main.py` takes your keyword and page count as input
2. `paginator.py` loops through pages 1, 2, 3... and deduplicates results
3. `scraper.py` fetches each page and extracts job details using BeautifulSoup
4. `saver.py` appends all results to `jobs.csv` with a timestamp

---

## Data Collected

Each job listing captures:

| Field | Description |
|---|---|
| `title` | Internship title |
| `company` | Company name |
| `location` | City or Work From Home |
| `stipend` | Monthly stipend amount |
| `duration` | Length of internship |
| `link` | Direct link to the listing |
| `scraped_on` | Date and time of scraping |

---

## 🚀 Features

- ✅ Scrapes multiple pages in one run
- ✅ Deduplicates listings automatically
- ✅ Appends new results without overwriting old data
- ✅ Polite scraping — 2 second delay between pages
- ✅ Graceful error handling — skips broken listings, continues scraping
- ✅ Timestamps every result so you know when it was found

---

## ⚠️ Troubleshooting

> [!WARNING]
> **Getting `N/A` for all fields?**
> Internshala may have updated their HTML. Run `detective.py` to inspect the live HTML and update the selectors in `scraper.py`.

> [!NOTE]
> **`ModuleNotFoundError: No module named 'requests'`?**
> You have multiple Python versions. Use the full Python path:
> ```bash
> C:/Users/<you>/AppData/Local/Python/bin/python.exe -m pip install -r requirements.txt
> ```

> [!TIP]
> **Getting blocked or 0 results?**
> The `User-Agent` header in `scraper.py` may be outdated. Update it to a current browser's user agent string from [whatismybrowser.com](https://www.whatismybrowser.com/detect/what-is-my-user-agent/).

---

## Possible Upgrades

- [ ] Filter results by minimum stipend
- [ ] Filter for Work From Home only
- [ ] Send a daily email digest of new listings
- [ ] Add a Streamlit dashboard to browse results
- [ ] Support multiple job sites (Naukri, LinkedIn)
- [ ] Schedule automatic daily runs

---

## License

MIT License — free to use, modify, and distribute.

---

> Built with Python 🐍 | Data from [Internshala](https://internshala.com)
