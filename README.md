# 🎬 Anime Recommender Web App

Welcome to the **Anime Recommender System**, your personalized gateway to discover the best anime based on your interests! Built using **Machine Learning**, **NLP**, and **Streamlit**, this web app delivers accurate recommendations powered by real-time anime data and advanced similarity scoring.

---

## 🚀 Features

✅ **Personalized Recommendations** – Get top 6 anime suggestions based on your favorite titles  
✅ **Interactive UI** – Built with **Streamlit** for a smooth, user-friendly experience  
✅ **Real-time Data Integration** – Powered by the **Jikan MyAnimeList API**  
✅ **Advanced NLP Pipelines** – Cleaned, processed, and vectorized anime descriptions using **spaCy** & **NLTK**  
✅ **Optimized Scoring** – Combines **TF-IDF**, **cosine similarity**, and a **custom weighted function** with anime ratings  
✅ **Dynamic Posters** – View recommended anime titles with their corresponding poster images  

---

## 🛠 Tech Stack

| Tool/Library        | Purpose |
|--------------------|---------|
| Python              | Core programming language |
| Streamlit           | Web app framework |
| BeautifulSoup      | Web scraping anime data |
| Jikan API           | Access to MyAnimeList data |
| spaCy, NLTK         | NLP pipelines for text processing |
| TF-IDF              | Feature extraction for similarity computation |
| Cosine Similarity   | Matching algorithm for recommendations |
| Custom Weighting    | Enhanced scoring based on ratings & similarity |

---

## 📂 Project Structure

├── app.py # Streamlit app file
├── data/ # Scraped anime data
├── models/ # Preprocessed models and TF-IDF vectors
├── assets/ # Images, posters, and icons
├── requirements.txt # Python dependencies
├── README.md # This file
