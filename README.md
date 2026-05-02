# 🎵 Music Recommendation System

A content-based music recommender built with Python and Streamlit that suggests similar songs based on your selection, complete with album art fetched from the iTunes API.

---
## 🚀 Features

- 🎧 Content-based filtering using cosine similarity
- 🖼️ Live album art fetched from the iTunes Search API (no API key required)
- 🔍 Searchable song dropdown with alphabetical sorting
- ⚡ Cached data loading for fast performance
- 🌙 Clean dark-themed UI via Streamlit

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| Recommendation Engine | Scikit-learn (cosine similarity) |
| NLP / Text Processing | NLTK (PorterStemmer, word_tokenize) |
| Album Art | iTunes Search API |
| Data | Pickle (df.pkl, similarity.pkl) |
| Language | Python 3.x |

---

## 📁 Project Structure

```
MUSICRECOMMENDATIONSYSTEM/
│
├── app.py                  # Main Streamlit app
├── notebook.ipynb          # Data preprocessing & model building
├── df.pkl                  # Processed music dataframe
├── similarity.pkl          # Precomputed cosine similarity matrix
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/music-recommendation-system.git
cd music-recommendation-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK data

```python
import nltk
nltk.download('punkt_tab')
```

### 5. Generate the pickle files

Run the Jupyter notebook (`notebook.ipynb`) end-to-end to generate `df.pkl` and `similarity.pkl`, then place them in the project root.

### 6. Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
nltk
requests
pickle5
```

Generate with:

```bash
pip freeze > requirements.txt
```

---

## 🧠 How It Works

1. Song lyrics/tags are preprocessed using NLTK stemming and tokenization.
2. A TF-IDF or Bag-of-Words matrix is built from the processed text.
3. Cosine similarity is computed between all songs and saved as `similarity.pkl`.
4. When a user selects a song, the top 5 most similar songs are retrieved.
5. Album art is fetched in real time from the iTunes Search API using the song name and artist.

---

## 🌐 iTunes API

Album art is sourced from Apple's free iTunes Search API — no authentication or API key required.

```
https://itunes.apple.com/search?term={song+artist}&media=music&limit=1
```

---

## 🙌 Acknowledgements

- Dataset: [Kaggle Music Dataset](https://www.kaggle.com/)
- Album Art: [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/)
- UI Framework: [Streamlit](https://streamlit.io/)
