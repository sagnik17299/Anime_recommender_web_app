import streamlit as st
import pickle as pkl
import pandas as pd
import requests

st.title("My Anime Recommender ")

# Function to fetch poster using Jikan API
def fetch_poster(anime_title):
    url = f"https://api.jikan.moe/v4/anime?q={anime_title}&limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            anime_data = data["data"][0]
            image_url = anime_data["images"]["jpg"]["large_image_url"]
            return image_url
    return "https://via.placeholder.com/200x300.png?text=No+Image"

# Load similarity matrix
similarity = pkl.load(open('similarity.pkl','rb'))

def recommender(anime_name):
    anime_index = anime[anime['title'] == anime_name].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_anime = []
    recommended_anime_posters = []

    for i in anime_list:
        anime_title = anime.iloc[i[0]].title
        recommended_anime.append(anime_title)
        recommended_anime_posters.append(fetch_poster(anime_title))

    return recommended_anime, recommended_anime_posters

# Load dataset
anime_dict = pkl.load(open("anime_dict.pkl",'rb'))
anime = pd.DataFrame(anime_dict)

# Select anime
selected_anime = st.selectbox("Name of your anime", anime['title'].values)

if st.button("Recommend"):
    names, posters = recommender(selected_anime)
    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
