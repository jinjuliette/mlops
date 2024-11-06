import streamlit as st
import joblib

model = joblib.load("regression.joblib")
size = st.number_input("Size", min_value=0, step=1)
nb_rooms = st.number_input("Number of bedrooms", min_value=0, step=1)
garden = st.number_input("Has garden", min_value=0, max_value=1, step=1)
st.write(model.predict([[size, nb_rooms, garden]]))