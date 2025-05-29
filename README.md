# Junction-Congestion-Prediction
🛣️ Junction Congestion Predictor
Junction Congestion Predictor is an intelligent, machine learning-based web application designed to forecast hourly traffic volume at key urban junctions. Leveraging historical traffic data and advanced regression techniques, the system enables users to anticipate congestion levels based on simple inputs such as date and time. The application is built using Python, trained using the Random Forest Regressor from Scikit-learn, and deployed with an intuitive interface via Streamlit.

This project addresses a critical challenge in modern cities—traffic congestion at road junctions, which contributes significantly to lost time, fuel waste, and increased emissions. By forecasting traffic volumes with high accuracy, the tool empowers commuters to plan more efficient travel, supports traffic authorities in optimizing control systems, and provides urban planners with data-driven insights for future infrastructure development.

The system extracts key temporal features such as hour of the day, day of the week, weekend status, and part of the day from the input DateTime, and uses them to predict vehicle flow through a trained model. Each junction has its own dedicated model, ensuring localized prediction accuracy. The predictions are not only displayed as raw vehicle counts but also classified into severity levels (Low, Moderate, High), and visualized with trend charts for the entire day.

Whether used as a standalone prediction tool or integrated into a larger smart city ecosystem, the Junction Congestion Predictor showcases the powerful application of machine learning for real-time, human-centric urban problem-solving.
