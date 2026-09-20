import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Books Analytics Dashboard", layout="wide")
df = pd.read_csv("data/books_clean.csv")

st.title("Books to Scrape — Data Analytics Dashboard")
st.caption("Educational project: web scraping → cleaning → EDA → visualization")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Books", len(df))
c2.metric("Average Price", f"£{df.Price_GBP.mean():.2f}")
c3.metric("Median Price", f"£{df.Price_GBP.median():.2f}")
c4.metric("Average Rating", f"{df.Rating_Num.mean():.2f}/5")

left,right = st.columns(2)
with left:
    fig,ax=plt.subplots()
    ax.hist(df.Price_GBP, bins=8)
    ax.set_title("Price Distribution")
    ax.set_xlabel("Price (£)")
    ax.set_ylabel("Books")
    st.pyplot(fig)
with right:
    counts=df.Rating.value_counts().reindex(["One","Two","Three","Four","Five"]).fillna(0)
    fig,ax=plt.subplots()
    ax.bar(counts.index, counts.values)
    ax.set_title("Rating Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Books")
    st.pyplot(fig)

fig,ax=plt.subplots()
ax.scatter(df.Rating_Num, df.Price_GBP)
ax.set_title("Price vs Rating")
ax.set_xlabel("Rating")
ax.set_ylabel("Price (£)")
st.pyplot(fig)

st.subheader("Highest-Priced Books")
st.dataframe(df.nlargest(10, "Price_GBP")[["Title","Price_GBP","Rating","Availability"]], use_container_width=True)
