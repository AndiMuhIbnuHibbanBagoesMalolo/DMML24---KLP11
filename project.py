import streamlit as st
import numpy as np
import joblib

# Fungsi untuk halaman Prediksi BMI
def bmi_prediction():
    st.title('Prediksi BMI')
    col1, col2 = st.columns([5, 5])

    with col2:
        st.image('gambar/BMI-Infographic-1.jpg', width=400)

    with col1:
        weight = st.slider('Berat Badan (lbs)', min_value=0.0, max_value=200.0, step=0.1, format="%.2f")
        height = st.slider('Tinggi Badan (inches)', min_value=0.0, max_value=300.0, step=0.1, format="%.2f")

        if st.button('Prediksi BMI'):
            try:
                with open('model/mse.pkl', 'rb') as file:
                    model = joblib.load(file)
            except FileNotFoundError:
                st.error('Model BMI tidak ditemukan. Harap pastikan Anda sudah melatih dan menyimpan model terlebih dahulu.')
                st.stop()

            bmi = weight / ((height / 100) ** 2)

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

            st.write(f'BMI Anda: {bmi:.2f}')
            st.image(gambar, width=200)
            st.write(f'***{interpretation}***')

            if interpretation == "Kekurangan berat badan (Underweight)":
                st.write('**Individu dengan BMI di bawah 18.5 dapat dianggap memiliki berat badan kurang. Mereka mungkin perlu mempertimbangkan peningkatan asupan nutrisi untuk mencapai berat badan yang sehat.**')
            elif interpretation == "Berat badan normal":
                st.write('**BMI Anda berada dalam kisaran normal, menunjukkan berat badan yang sehat untuk tinggi badan Anda.**')
            elif interpretation == "Kelebihan berat badan (Overweight)":
                st.write('**Individu dengan BMI antara 25 dan 29.9 dianggap kelebihan berat badan. Mereka mungkin perlu mempertimbangkan untuk mengurangi kalori atau meningkatkan aktivitas fisik.**')
            else:
                st.write('**BMI Anda menunjukkan obesitas. Perubahan gaya hidup seperti diet sehat dan olahraga teratur dapat membantu mengurangi risiko masalah kesehatan.**')

# Fungsi untuk halaman Prediksi Body Fat
def body_fat_prediction():
    st.title('Prediksi Body Fat')

    density = st.number_input('Density', min_value=0.0, format="%.2f")
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

    if st.button('Prediksi Body Fat'):
        try:
            with open('model/bodyfat_model.pkl', 'rb') as file:
                model = joblib.load(file)
        except FileNotFoundError:
            st.error('Model tidak ditemukan. Harap pastikan Anda sudah melatih dan menyimpan model terlebih dahulu.')
            st.stop()

        input_data = np.array([[density, age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist]])
        prediksi_body_fat = model.predict(input_data)

        st.write(f'Prediksi Body Fat: {prediksi_body_fat[0]:.2f}%')

# Main function
def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Pilih Prediksi", ["Prediksi BMI", "Prediksi Body Fat"])

    if menu == "Prediksi BMI":
        bmi_prediction()
    elif menu == "Prediksi Body Fat":
        body_fat_prediction()

if __name__ == '__main__':
    main()
