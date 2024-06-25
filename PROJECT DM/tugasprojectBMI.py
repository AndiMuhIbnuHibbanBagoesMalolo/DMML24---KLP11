import streamlit as st
import numpy as np
import pickle

st.title('Prediction BMI')

# Input pengguna
weight = st.number_input('Berat Badan (lbs)', min_value=0.0, format="%.2f")
height = st.number_input('Tinggi Badan (inches)', min_value=0.0, format="%.2f")

# Tombol untuk prediksi
if st.button('Prediksi BMI'):
    # Memuat model yang telah dilatih
    try:
        with open('mse.pkl', 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        st.error('Model BMI tidak ditemukan. Harap pastikan Anda sudah melatih dan menyimpan model terlebih dahulu.')
        st.stop()

    # Hitung BMI (tidak perlu model untuk perhitungan sederhana)
    bmi = weight / ((height / 100) ** 2)  # Konversi tinggi ke meter

    # Interpretasi BMI (sesuaikan dengan kategori yang diinginkan)
    if bmi < 18.5:
        interpretation = "Kekurangan berat badan"
    elif bmi < 25:
        interpretation = "Berat badan normal"
    elif bmi < 30:
        interpretation = "Kelebihan berat badan"
    else:
        interpretation = "Obesitas"

    # Menampilkan hasil prediksi
    st.write(f'BMI Anda: {bmi:.2f}')
    st.write(f'Interpretasi BMI: {interpretation}')
