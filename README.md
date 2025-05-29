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


![Screenshot (44)](https://github.com/user-attachments/assets/b0f033d2-eb5f-4d69-9336-1a718c020ff3)





![Screenshot (41)](https://github.com/user-attachments/assets/333b0497-3ef2-483f-880e-003bd9876359)





![Screenshot (42)](https://github.com/user-attachments/assets/810fc511-c967-4a98-b09d-f24f902c0ef5)


How to Run
1. Install dependencies: pip install streamlit scikit-learn pandas matplotlib
   
2. Place all files together
   
3. Run using: streamlit run app.py

Summary :

Practical web app combining ML prediction with an intuitive interface. This project combines machine learning and web app deployment to predict traffic volume based on time and date inputs. It successfully integrates user-friendly interfaces with powerful predictive modeling to create a tool that is both practical and informative. The design ensures easy accessibility and clear visibility, with background styling and form optimization enhancing the user experience.
Overall, this Traffic Congestion Prediction Web App offers a clear demonstration of how modern web technologies can be combined with data science to solve real-world problems effectively.

Conclusion:

A successful foundation for smart traffic management apps using data science and modern web technologies. The Traffic Congestion Prediction Web App successfully integrates data science, machine learning, and a clean user interface to solve a practical problem. Users can easily predict traffic volume based on simple inputs, receive quick insights about congestion levels, and visualize traffic patterns over a full day. This project highlights the power of predictive analytics combined with user-friendly deployment, making it an excellent foundation for further enhancements such as real-time updates, integration with maps, and predictive traffic management systems.


