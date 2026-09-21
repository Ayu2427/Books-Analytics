# Books to Scrape — Price & Rating Analytics

An end-to-end data analytics project covering web scraping, data cleaning, exploratory data analysis, statistical analysis, and interactive visualization using Python, Pandas, BeautifulSoup, Matplotlib, Streamlit, and Power BI.

## Workflow

Web Scraping → Data Cleaning → EDA → Statistical Analysis → Visualization → Dashboard

## Key Questions

- What is the typical book price?
- How are book ratings distributed?
- Is there an association between price and rating?
- Which books are at the high end of the price distribution?
- Are there missing values, duplicates, or unusual price observations?

## Technology Stack

Python • Requests • BeautifulSoup • Pandas • NumPy • Matplotlib • Streamlit • Power BI • Jupyter Notebook

## Repository Structure

```
Books-Analytics/
├── data/
│   ├── books_clean.csv
│   └── books_sample.csv
├── src/
│   ├── scraper.py
│   ├── clean_data.py
│   └── eda.py
├── dashboard/
│   └── app.py
├── notebooks/
│   └── Books_Analytics.ipynb
├── reports/
│   └── eda_summary.txt
├── docs/
│   └── POWER_BI_GUIDE.md
├── Books_Analytics_Final_Report.pdf
├── requirements.txt
└── README.md
```

## Dataset

The project uses **Books to Scrape**, a sandbox website designed for web-scraping practice. Its displayed prices and ratings are randomly assigned for demonstration purposes, so the results should be treated as an educational analytics demonstration rather than real market intelligence.

## Sample Results

The 20-book working sample contains:

- Average price: **£38.05**
- Median price: **£41.38**
- Price range: **£13.99–£57.25**
- Average rating: **2.85/5**
- In-stock rate: **100%**
- Price-rating correlation: **-0.076**
- IQR price outliers: **0**

## How to Run

```bash
pip install -r requirements.txt
python src/scraper.py
python src/clean_data.py
python src/eda.py
streamlit run dashboard/app.py
```

## Power BI

Import `data/books_clean.csv` into Power BI and build KPI cards, rating and price distributions, a price-vs-rating scatter plot, a top-10 price chart, a detailed table, and slicers.

See `docs/POWER_BI_GUIDE.md`.

## Notes

The included CSV files contain a small working sample for reproducibility. The scraper can collect the available catalogue pages from the source site when executed.

## Author

**Ayu2427**
