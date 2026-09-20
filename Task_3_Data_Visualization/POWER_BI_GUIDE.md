# Power BI Dashboard Build

1. Open Power BI Desktop.
2. Get Data → Text/CSV → `data/books_clean.csv`.
3. Confirm:
   - Price_GBP = Decimal Number
   - Rating_Num = Whole Number
   - Title = Text
   - Availability = Text
4. Add KPI cards:
   - Count of Title
   - Average of Price_GBP
   - Median of Price_GBP
   - Average of Rating_Num
5. Add visuals:
   - Rating distribution: clustered column chart
   - Price distribution: column chart using price bins
   - Price vs Rating: scatter chart
   - Top 10 books: bar chart
   - Detailed book table
6. Add slicers for Rating and Availability.
7. Add a text box with 3–5 findings.
8. Save as `Books_Analytics_Dashboard.pbix`.

Suggested dashboard title:
BOOKS TO SCRAPE — PRICE & RATING ANALYTICS
