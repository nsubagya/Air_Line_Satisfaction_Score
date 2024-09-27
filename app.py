import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r"Air_line_model.pkl")

# Streamlit app title
st.title("Airline Passenger Satisfaction Predictor")

# User input fields for each feature
arrival_delay = st.number_input("Arrival Delay in Minutes", min_value=0, max_value=300, value=5)
departure_delay = st.number_input("Departure Delay in Minutes", min_value=0, max_value=300, value=5)
cleanliness = st.selectbox("Cleanliness", [1, 2, 3, 4, 5], index=2)
inflight_service = st.selectbox("Inflight Service", [1, 2, 3, 4, 5], index=2)
checkin_service = st.selectbox("Checkin Service", [1, 2, 3, 4, 5], index=2)
leg_room_service = st.selectbox("Leg Room Service", [1, 2, 3, 4, 5], index=2)
on_board_service = st.selectbox("On-board Service", [1, 2, 3, 4, 5], index=2)
inflight_entertainment = st.selectbox("Inflight Entertainment", [1, 2, 3, 4, 5], index=2)
seat_comfort = st.selectbox("Seat Comfort", [1, 2, 3, 4, 5], index=2)
online_boarding = st.selectbox("Online Boarding", [1, 2, 3, 4, 5], index=2)

# Create a dictionary of input values
input_data = {
    'Arrival Delay in Minutes': [arrival_delay],
    'Departure Delay in Minutes': [departure_delay],
    'Cleanliness': [cleanliness],
    'Inflight service': [inflight_service],
    'Checkin service': [checkin_service],
    'Leg room service': [leg_room_service],
    'On-board service': [on_board_service],
    'Inflight entertainment': [inflight_entertainment],
    'Seat comfort': [seat_comfort],
    'Online boarding': [online_boarding]
}

# Convert dictionary to DataFrame
input_df = pd.DataFrame(input_data)

# Prediction button
if st.button("Predict Satisfaction"):
    # Make a prediction
    prediction = model.predict(input_df)
    
    # Display the result
    if prediction[0] == 1:
        st.success("The passenger is satisfied!")
    else:
        st.error("The passenger is not satisfied.")
