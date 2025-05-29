import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime
import calendar
import matplotlib.pyplot as plt

# Load your trained model
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Helper functions
def date_to_day(year, month, date):
    date = datetime.datetime(year, month, date)
    day_name = calendar.day_name[date.weekday()]
    return day_name

def get_part_of_day(hour):
    if 5 <= hour <= 11:
        return 'Morning'
    elif 12 <= hour <= 16:
        return 'Afternoon'
    elif 17 <= hour <= 20:
        return 'Evening'
    else:
        return 'Night'

part_of_day_mapping = {'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}

def show_predict_page():
    st.title("🚦 congestion Volume Prediction App")

    st.write("### Please provide the following information:")

    # Inputs
    year = st.selectbox('Select Year', list(range(2015, 2025)), index=5)
    month = st.selectbox('Select Month', list(range(1, 13)), index=0)
    date = st.selectbox('Select Day of Month', list(range(1, 32)), index=0)
    hour = st.slider('Select Hour of Day', 0, 23, 8)

    # Calculate additional features
    day_name = date_to_day(year, month, date)
    day_mapping = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
        'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    day_encoded = day_mapping[day_name]
    is_weekend = 1 if day_name in ['Saturday', 'Sunday'] else 0
    part_of_day = get_part_of_day(hour)
    part_of_day_encoded = part_of_day_mapping[part_of_day]

    # Display calculated information
    st.write(f"**Day:** {day_name}")
    st.write(f"**Weekend:** {'Yes' if is_weekend else 'No'}")
    st.write(f"**Part of Day:** {part_of_day}")

    # Prepare model input
    input_dict = {
        'year': [year],
        'month': [month],
        'date': [date],
        'hour': [hour],
        'day_encoded': [day_encoded],
        'is_weekend': [is_weekend],
        'part_of_day_encoded': [part_of_day_encoded]
    }
    X = pd.DataFrame(input_dict)

    # Predict button
    if st.button('🚗 Predict Congestion  Volume'):
        with st.spinner('Predicting Congestion volume...'):
            prediction = model.predict(X)
            traffic_volume = int(prediction[0])

            # Show traffic volume number
            st.subheader(f"🚘 Predicted Congestion Volume: **{traffic_volume} vehicles**")

            # Show severity feedback
            if traffic_volume < 50:
                st.success(f"🟢 Low congestion Volume ({traffic_volume} vehicles)")
            elif 50 <= traffic_volume < 150:
                st.warning(f"🟡 Moderate congestion Volume ({traffic_volume} vehicles)")
            else:
                st.error(f"🔴 High congestion Volume ({traffic_volume} vehicles)")

    st.write("---")

    # Optional Traffic Volume Trend
    st.header("📈 congestion Volume Trend Throughout the Day")

    if st.checkbox("Show congestion Volume Trend Chart"):
        sample_hours = list(range(24))
        sample_predictions = []

        for h in sample_hours:
            part_of_day_h = get_part_of_day(h)
            part_of_day_encoded_h = part_of_day_mapping[part_of_day_h]

            input_dict_h = {
                'year': [year],
                'month': [month],
                'date': [date],
                'hour': [h],
                'day_encoded': [day_encoded],
                'is_weekend': [is_weekend],
                'part_of_day_encoded': [part_of_day_encoded_h]
            }
            X_h = pd.DataFrame(input_dict_h)
            pred = model.predict(X_h)[0]
            sample_predictions.append(pred)

        # Plotting the trend
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(sample_hours, sample_predictions, marker='o', color='blue')
        ax.set_xticks(sample_hours)
        ax.set_xlabel('Hour of Day')
        ax.set_ylabel('Predicted congestion Volume (vehicles)')
        ax.set_title('Predicted congestion Volume Throughout the Day')
        st.pyplot(fig)





