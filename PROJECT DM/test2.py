import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Judul aplikasi
st.title('Prediksi Body Fat')

# Input pengguna
density = st.number_input('Density', min_value=0.0, format="%.4f")
age = st.number_input('Age', min_value=0, format="%d")
weight = st.number_input('Weight (lbs)', min_value=0.0, format="%.2f")
height = st.number_input('Height (inches)', min_value=0.0, format="%.2f")
neck = st.number_input('Neck (cm)', min_value=0.0, format="%.2f")
chest = st.number_input('Chest (cm)', min_value=0.0, format="%.2f")
abdomen = st.number_input('Abdomen (cm)', min_value=0.0, format="%.2f")
hip = st.number_input('Hip (cm)', min_value=0.0, format="%.2f")
thigh = st.number_input('Thigh (cm)', min_value=0.0, format="%.2f")
knee = st.number_input('Knee (cm)', min_value=0.0, format="%.2f")
ankle = st.number_input('Ankle (cm)', min_value=0.0, format="%.2f")
biceps = st.number_input('Biceps (cm)', min_value=0.0, format="%.2f")
forearm = st.number_input('Forearm (cm)', min_value=0.0, format="%.2f")
wrist = st.number_input('Wrist (cm)', min_value=0.0, format="%.2f")

# Tombol untuk prediksi
if st.button('Prediksi Body Fat'):
    # Data dummy untuk model regresi (seharusnya diganti dengan data yang sesungguhnya)
    X_dummy = np.random.rand(100, 14)
    y_dummy = np.random.rand(100)
    
    # Membuat model regresi linier
    model = LinearRegression()
    model.fit(X_dummy, y_dummy)
    
    # Menyiapkan data input untuk prediksi
    input_data = np.array([[density, age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist]])
    
    # Melakukan prediksi
    prediksi_body_fat = model.predict(input_data)
    
    # Menampilkan hasil prediksi
    st.write(f'Prediksi Body Fat: {prediksi_body_fat[0]:.2f}%')
