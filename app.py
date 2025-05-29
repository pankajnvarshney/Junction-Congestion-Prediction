import streamlit as st
from predict_page import show_predict_page
from app_page import show_app_page

st.set_page_config(page_title='Traffic Prediction')

page = st.sidebar.selectbox('Select Page', ('Predict', 'App Info'))

if page == 'Predict':
    show_predict_page()
else:
    show_app_page()