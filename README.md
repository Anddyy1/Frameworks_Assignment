# COVID-19 Metadata Analysis

This is my assignment where I worked with the **CORD-19 metadata dataset**.  
I used **Pandas, Matplotlib, Seaborn, and Streamlit** to clean the data, explore it, and build some visualizations.  
The idea was to practice the full **data science workflow** — from loading the data, cleaning it, analyzing it, and then sharing results with a simple dashboard.

---

## 📂 Project Files

```

Frameworks\_Assignment/
│-- index8.py              # My main analysis script + Streamlit app
│-- metadata\_sample.csv    # A smaller sample dataset I’m using for testing
│-- README.md              # This file
│-- requirements.txt       # Libraries I need

```

---

## ⚡ What I Did
- Loaded the dataset and checked its shape + structure  
- Cleaned missing values and handled weird/mixed datatypes  
- Looked at descriptive statistics of the key fields  
- Created some visualizations (trends, authors, abstracts)  
- Built a simple Streamlit app to make the results interactive  
- Added a smaller sample dataset so I don’t have to load the entire huge file every time  

---

## 📊 Dataset
The full dataset (`metadata.csv`) is too big for GitHub (over 150 MB).  
👉 If you want to use it, download it from Kaggle here:  
[CORD-19 Research Challenge - Metadata](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Once you download, just put it in the project folder like this:

```

Frameworks\_Assignment/metadata.csv

````

⚠️ For now, I’ve included **metadata_sample.csv** (50k rows) so you can test everything quickly without crashing your machine.

---

## ▶️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

My `requirements.txt` looks like this:

```
pandas
matplotlib
seaborn
streamlit
wordcloud
```

### 3. Run with Python

If you just want to test with the sample dataset:

```bash
python index8.py
```

### 4. Run with Streamlit

If you want to open the interactive app in your browser:

```bash
streamlit run index8.py
```

---

## ✅ What You’ll Get

* A script with the full analysis workflow
* Some visualizations that show trends in the data
* A working Streamlit app that you can interact with
* Practice with real-world messy data and how to handle it

---

## 📌 Notes

* I’m ignoring `mag_id` because it’s empty in the dataset
* I used `low_memory=False` when loading the CSV to fix the dtype warnings
* The sample dataset is enough to test things, but if you want deeper results, use the full dataset

---

## 📜 License

This is just for learning and educational purposes.