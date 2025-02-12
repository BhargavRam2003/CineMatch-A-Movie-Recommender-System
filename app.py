import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_list)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended = []
    for i in movie_list:
        recommended.append((movies.iloc[i[0]].title))
    return recommended

st.title("Movie Recommender System")

option = st.selectbox(
    "Choose any movie from the list.We will Suggest top 5 Similar movies for you 😉",
    (movies['title']),
)

if st.button("Recommend"):

    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)

    