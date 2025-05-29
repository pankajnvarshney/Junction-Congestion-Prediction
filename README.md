# Junction-Congestion-Prediction
🛣️ Junction Congestion Predictor
Junction Congestion Predictor is an intelligent, machine learning-based web application designed to forecast hourly traffic volume at key urban junctions. Leveraging historical traffic data and advanced regression techniques, the system enables users to anticipate congestion levels based on simple inputs such as date and time. The application is built using Python, trained using the Random Forest Regressor from Scikit-learn, and deployed with an intuitive interface via Streamlit.

This project addresses a critical challenge in modern cities—traffic congestion at road junctions, which contributes significantly to lost time, fuel waste, and increased emissions. By forecasting traffic volumes with high accuracy, the tool empowers commuters to plan more efficient travel, supports traffic authorities in optimizing control systems, and provides urban planners with data-driven insights for future infrastructure development.

The system extracts key temporal features such as hour of the day, day of the week, weekend status, and part of the day from the input DateTime, and uses them to predict vehicle flow through a trained model. Each junction has its own dedicated model, ensuring localized prediction accuracy. The predictions are not only displayed as raw vehicle counts but also classified into severity levels (Low, Moderate, High), and visualized with trend charts for the entire day.

Whether used as a standalone prediction tool or integrated into a larger smart city ecosystem, the Junction Congestion Predictor showcases the powerful application of machine learning for real-time, human-centric urban problem-solving.

📂 Project Structure
├── app.py                  # Streamlit app launcher
├── predict_page.py         # Prediction UI and logic
├── app_page.py             # App info & overview page
├── train_model.py          # Trains Random Forest models per junction
├── final_model_1.pkl ...   # Trained model files
├── traffic.csv             # (Optional) Source dataset
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation

pip install -r requirements.txt
streamlit run app.py


------Key Features
Predicts the number of vehicles at a selected junction based on date & time

Shows congestion severity (Low, Moderate, High)

Visualizes traffic volume trends across the entire day

Clean and interactive UI powered by Streamlit

Supports separate models for different junctions (scalable)

Lightweight and easy to deploy

![image](https://github.com/user-attachments/assets/bb14a040-d936-4c17-8682-7a498f940885)

![Screenshot (45)](https://github.com/user-attachments/assets/cdf9419e-bb7e-4976-ab11-1a1dc5aca3f9)

![Screenshot (42)](https://github.com/user-attachments/assets/d2f4bc99-65e1-4bd2-adf4-06cc599f1f49)





