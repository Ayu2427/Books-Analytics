from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
src = BASE / "data" / "books_scraped.csv"
out = BASE / "data" / "books_clean.csv"

df = pd.read_csv(src)
df["Price_GBP"] = (
    df["Price"].astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)
rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
df["Rating_Num"] = df["Rating"].map(rating_map)
df["Title_Length"] = df["Title"].astype(str).str.len()
df["Word_Count"] = df["Title"].astype(str).str.split().str.len()
df["Availability"] = df["Availability"].astype(str).str.strip().str.title()

df = df.drop_duplicates(subset=["Title", "Price_GBP"])
df.to_csv(out, index=False, encoding="utf-8-sig")
print(f"Saved cleaned dataset: {out} ({len(df)} rows)")
