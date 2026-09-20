from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "books_clean.csv")

print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nDescriptive statistics:\n", df[["Price_GBP","Rating_Num","Title_Length","Word_Count"]].describe())

corr = df["Price_GBP"].corr(df["Rating_Num"])
q1, q3 = df["Price_GBP"].quantile([0.25, 0.75])
iqr = q3 - q1
outliers = df[(df["Price_GBP"] < q1 - 1.5*iqr) | (df["Price_GBP"] > q3 + 1.5*iqr)]

report = f"""BOOK DATASET — EDA SUMMARY

Records: {len(df)}
Average price: £{df.Price_GBP.mean():.2f}
Median price: £{df.Price_GBP.median():.2f}
Price range: £{df.Price_GBP.min():.2f} to £{df.Price_GBP.max():.2f}
Average rating: {df.Rating_Num.mean():.2f}/5
In-stock rate: {df.Availability.eq('In Stock').mean()*100:.1f}%
Price-rating correlation: {corr:.3f}
Price IQR outliers: {len(outliers)}

Business/analytical questions:
1. What is the typical book price?
2. How are ratings distributed?
3. Is higher rating associated with higher price?
4. Which books are at the high end of the price distribution?
5. Are there missing values, duplicates, or unusual prices?

Findings:
- The sample contains {len(df)} scraped book records.
- All sampled records are marked in stock.
- The mean price is £{df.Price_GBP.mean():.2f}; the median is £{df.Price_GBP.median():.2f}.
- The price-rating correlation is {corr:.3f}; this sample does not establish a causal relationship.
- {len(outliers)} price observations are flagged by the 1.5×IQR rule.
"""
(BASE/"reports"/"eda_summary.txt").write_text(report, encoding="utf-8")
