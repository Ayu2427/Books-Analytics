import time
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
OUTPUT = Path("data/books_scraped.csv")
HEADERS = {"User-Agent": "Mozilla/5.0 (educational web scraping project)"}

def scrape_page(url):
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    rows = []
    for card in soup.select("article.product_pod"):
        title_tag = card.select_one("h3 a")
        price_tag = card.select_one("p.price_color")
        stock_tag = card.select_one("p.instock.availability")
        rating_tag = card.select_one("p.star-rating")
        link = title_tag.get("href", "") if title_tag else ""
        rows.append({
            "Title": title_tag.get("title", "").strip() if title_tag else "",
            "Price": price_tag.get_text(strip=True) if price_tag else "",
            "Availability": stock_tag.get_text(" ", strip=True) if stock_tag else "",
            "Rating": rating_tag.get("class", ["", "Unknown"])[1] if rating_tag and len(rating_tag.get("class", [])) > 1 else "Unknown",
            "URL": BASE_URL + "catalogue/" + link.replace("../", "") if link else ""
        })
    return rows, soup

def main():
    all_rows, url, page = [], BASE_URL, 1
    while url:
        print(f"Scraping page {page}: {url}")
        rows, soup = scrape_page(url)
        all_rows.extend(rows)
        next_link = soup.select_one("li.next a")
        if not next_link:
            break
        url = BASE_URL + "catalogue/" + next_link.get("href")
        page += 1
        time.sleep(0.5)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(all_rows).to_csv(OUTPUT, index=False, encoding="utf-8-sig")
    print(f"Saved {len(all_rows)} records to {OUTPUT}")

if __name__ == "__main__":
    main()
