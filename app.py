import streamlit as st
import pandas as pd


st.title("🏭 AI Manufacturing Cost Predictor")

st.write("Enter production details below:")

material_cost = st.number_input("Material Cost")
labour_hours = st.number_input("Labour Hours")
machine_time = st.number_input("Machine Time")
quantity = st.number_input("Quantity")

if st.button("Predict Cost"):
   
    prediction = (material_cost * quantity) + (labour_hours * 20) + (machine_time * 50)
    
    st.success(f"Predicted Manufacturing Cost: {prediction}")
