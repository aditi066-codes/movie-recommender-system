import pickle
import streamlit as st
import pandas as pd

# ---------------- LOAD DATA ----------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# ---------------- STREAMLIT UI ----------------
st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from dropdown",
    movie_list
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")

    for movie in recommendations:
        st.write(movie)