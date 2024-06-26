






import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies=[]

    for i in distances[1:7]:
        recommended_movies.append(movies.iloc[i[0]].title)


    return recommended_movies
st.header("Movie Recommender System")

movies = pickle.load(open('movie_list.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values

option = st.selectbox(
'Type or select a movie from the dropdown' ,
    movie_list
)
if st.button('Recommend'):

    recommendations=recommend(option)
    for i in recommendations:
     st.write(i)
