import streamlit as st
import numpy as np
import pickle

def main():
    # Membuat layout kolom
    col1, col2 = st.columns([2, 5])

    # Di kolom pertama (col1), letakkan gambar
    with col1:
        st.title('Prediksi BMI')

    # Di kolom kedua (col2), letakkan judul dan teks lainnya
    with col2:
        st.image('gambar/BMI-Infographic-1.jpg', width=400)
        
if __name__ == '__main__':
    main()
    
# Input pengguna
weight = st.slider('Berat Badan (lbs)', min_value=0.0, max_value=200.0, step=0.1, format="%.2f")
height = st.slider('Tinggi Badan (inches)', min_value=0.0, max_value=300.0, step=0.1, format="%.2f")

# Tombol untuk prediksi
if st.button('Prediksi BMI'):
    # Memuat model yang telah dilatih
    try:
        with open('model/mse.pkl', 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        st.error('Model BMI tidak ditemukan. Harap pastikan Anda sudah melatih dan menyimpan model terlebih dahulu.')
        st.stop()

    # Hitung BMI (tidak perlu model untuk perhitungan sederhana)
    bmi = weight / ((height / 100) ** 2)  # Konversi tinggi ke meter

    # Interpretasi BMI menurut WHO
    if bmi < 18.5:
        interpretation = "Kekurangan berat badan (Underweight)"
        gambar = 'gambar/underweight.jpg'
    elif bmi < 25:
        interpretation = "Berat badan normal"
        gambar = 'gambar/normal.jpg'
    elif bmi < 30:
        interpretation = "Kelebihan berat badan (Overweight)"
        gambar = 'gambar/overweight.jpg'
    else:
        interpretation = "Obesitas"
        gambar = 'gambar/obesity.jpg'
        

    # Menampilkan hasil prediksi
    st.write(f'BMI Anda: {bmi:.2f}')
    st.image(gambar, width=200)
    st.write(f'***{interpretation}***')
    
    # Menambahkan caption untuk interpretasi BMI
    if interpretation == "Kekurangan berat badan (Underweight)":
        st.write('**Individu dengan BMI di bawah 18.5 dapat dianggap memiliki berat badan kurang. Mereka mungkin perlu mempertimbangkan peningkatan asupan nutrisi untuk mencapai berat badan yang sehat.**')
    elif interpretation == "Berat badan normal":
        st.write('**BMI Anda berada dalam kisaran normal, menunjukkan berat badan yang sehat untuk tinggi badan Anda.**')
    elif interpretation == "Kelebihan berat badan (Overweight)":
        st.write('**Individu dengan BMI antara 25 dan 29.9 dianggap kelebihan berat badan. Mereka mungkin perlu mempertimbangkan untuk mengurangi kalori atau meningkatkan aktivitas fisik.**')
    else:
        st.write('**BMI Anda menunjukkan obesitas. Perubahan gaya hidup seperti diet sehat dan olahraga teratur dapat membantu mengurangi risiko masalah kesehatan.**')
