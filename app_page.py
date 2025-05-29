import streamlit as st

def show_app_page():
    st.title("Traffic Prediction App Info")

    st.write(
        """
        ## About the App
        This app predicts **Traffic Congestion Levels** based on:
        - Day of the week
        - Hour of the day
        - Whether it's a holiday
        
        ## How it Works
        We trained a machine learning model using historical traffic data.
        
        The model outputs a congestion score.
        
        Lower values mean less traffic, higher values mean more congestion.
        """
    )
