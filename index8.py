# Importing the libraries I need
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

# ============================
# PART 1: LOADING THE DATA
# ============================

# First I try loading the full dataset. It's too big for GitHub (about 150MB)
# so I just take a 50,000 row sample and save it separately for future use.
try:
    # full dataset, low_memory to avoid dtype warnings
    df = pd.read_csv("metadata.csv", low_memory=False)
    df_sample = df.sample(n=50000, random_state=42)  # create smaller dataset
    df_sample.to_csv("metadata_sample.csv", index=False)  # save sample
    print("Full dataset loaded, sample created as metadata_sample.csv")
except FileNotFoundError:
    # If the big file is not available, I just load the sample
    df_sample = pd.read_csv("metadata_sample.csv")
    print("Sample dataset loaded (metadata_sample.csv)")

# I’ll only work with the sample to make everything faster and lighter
df = df_sample

# Quick checks on the data
print(df.shape)   # dimensions of the dataset
print(df.info())  # column types + missing values overview
print(df.isnull().sum())  # missing values count per column

# ============================
# PART 2: CLEANING + PREP
# ============================

# Some rows don’t have publish_time or title → I drop them
df = df.dropna(subset=["publish_time", "title"])

# publish_time is a string, so I convert it into datetime format
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# I add a year column to make it easy to count papers by year
df["year"] = df["publish_time"].dt.year

# Just for extra analysis, I count words in each abstract (if missing, treat as empty string)
df["abstract_word_count"] = df["abstract"].fillna(
    "").apply(lambda x: len(x.split()))

# ============================
# PART 3: ANALYSIS + VISUALS
# ============================

# Count how many papers were published each year
year_counts = df["year"].value_counts().sort_index()

# Find the top 10 journals
top_journals = df["journal"].value_counts().head(10)

# Word cloud from paper titles
all_titles = " ".join(df["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400,
                      background_color="white").generate(all_titles)

# --- PLOTS ---

# Plot publications by year
plt.figure(figsize=(10, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.savefig("publications_by_year.png")
plt.close()

# Plot top journals
plt.figure(figsize=(10, 5))
plt.bar(top_journals.index, top_journals.values)
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Journal")
plt.ylabel("Number of Papers")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.close()

# Save the word cloud image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.savefig("titles_wordcloud.png")
plt.close()

# ============================
# PART 4: STREAMLIT APP
# ============================

# Streamlit app starts here
st.title("CORD-19 Data Explorer (Sampled Data)")
st.write("Exploring COVID-19 research papers using a 50,000-row sample.")

# Add a slider to pick which years I want to look at
min_year, max_year = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2022))

# Filter dataset by year range selected
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Show publications over time (bar chart)
st.subheader("Publications Over Time")
year_counts_filtered = filtered_df["year"].value_counts().sort_index()
st.bar_chart(year_counts_filtered)

# Show top journals
st.subheader("Top Journals")
st.bar_chart(filtered_df["journal"].value_counts().head(10))

# Show word cloud image
st.subheader("Word Cloud of Titles")
st.image("titles_wordcloud.png")

# Display a small sample of the data
st.subheader("Sample of the Data")
st.write(filtered_df.head())
