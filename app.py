
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("random_forest_model.pkl")

# Title
st.title("Boston House Price Prediction App")

# Input fields
st.write("Enter values for prediction:")

# Create input fields for user data (adjust based on your dataset)
CRIM = st.number_input("CRIM", min_value=0.0, step=0.1)
ZN = st.number_input("ZN", min_value=0.0, step=1.0)
INDUS = st.number_input("INDUS", min_value=0.0, step=0.1)
CHAS = st.selectbox("CHAS", [0, 1])
NOX = st.number_input("NOX", min_value=0.0, step=0.01)
RM = st.number_input("RM", min_value=0.0, step=0.1)
AGE = st.number_input("AGE", min_value=0.0, step=1.0)
DIS = st.number_input("DIS", min_value=0.0, step=0.1)
RAD = st.number_input("RAD", min_value=1, step=1)
TAX = st.number_input("TAX", min_value=0, step=1)
PTRATIO = st.number_input("PTRATIO", min_value=0.0, step=0.1)
B = st.number_input("B", min_value=0.0, step=0.1)
LSTAT = st.number_input("LSTAT", min_value=0.0, step=0.1)

# Create prediction button
if st.button("Predict"):
    input_data = pd.DataFrame([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]],
                              columns=["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"])
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")

