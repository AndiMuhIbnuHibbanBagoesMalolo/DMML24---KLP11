import streamlit as st
import numpy as np
import joblib

# Fungsi untuk halaman Prediksi BMI
def bmi_prediction():
    st.title('Prediksi BMI')
    st.image('gambar/BMI-Infographic-1.jpg', width=400)

    weight = st.number_input('Berat Badan (kg)', min_value=0.0, max_value=200.0, step=0.1, format="%.2f")
    height = st.number_input('Tinggi Badan (cm)', min_value=0.0, max_value=300.0, step=0.1, format="%.2f")

    if st.button('Prediksi BMI'):
        try:
            with open('model/mse.pkl', 'rb') as file:
                model = joblib.load(file)
        except FileNotFoundError:
            st.error('Model BMI tidak ditemukan. Harap pastikan Anda sudah melatih dan menyimpan model terlebih dahulu.')
            st.stop()

        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            interpretation = "KEKURANGAN berat badan (Underweight)"
            gambar = 'gambar/underweight.jpg'
            color = '#4B70F5'
        elif bmi < 25:
            interpretation = "Berat badan NORMAL"
            gambar = 'gambar/normalman.jpg'
            color = '#06D001'
        elif bmi < 30:
            interpretation = "KELEBIHAN berat badan (Overweight)"
            gambar = 'gambar/overweight.jpg'
            color = '#FFF455'
        else:
            interpretation = "OBESITAS"
            gambar = 'gambar/obesity.jpg'
            color = '#E72929'
            
        st.write(f'BMI Anda : {bmi:.2f}')
        st.image(gambar, width=200)
        st.markdown(f'<p style="font-size:25px; color:{color};"><strong>{interpretation}</strong></p>', unsafe_allow_html=True)
    
        if interpretation == "KEKURANGAN berat badan (Underweight)":
            st.write('**Individu dengan BMI di bawah 18.5 dapat dianggap memiliki berat badan kurang. Mereka mungkin perlu mempertimbangkan peningkatan asupan nutrisi untuk mencapai berat badan yang sehat.**  '
            '[Lebih lanjut tentang Kekurangan Berat Badan](https://www.alodokter.com/faktor-penyebab-badan-kurus-dan-tips-sehat-untuk-mengatasinya)')
        elif interpretation == "Berat badan NORMAL":
            st.write('**BMI Anda berada dalam kisaran normal, menunjukkan berat badan yang sehat untuk tinggi badan Anda.**  '
            '[Lebih lanjut tentang Berat Badan Normal](https://www.family.abbott/id-id/ensure/tools-and-resources/tips-on-how-to-live-strong/nutrition/menjaga-berat-badan.html)')
        elif interpretation == "KELEBIHAN berat badan (Overweight)":
            st.write('**Individu dengan BMI antara 25 dan 29.9 dianggap kelebihan berat badan. Mereka mungkin perlu mempertimbangkan untuk mengurangi kalori atau meningkatkan aktivitas fisik.**  '
            '[Lebih lanjut tentang Kelebihan Berat Badan](https://www.alodokter.com/berat-badan-berlebih)')
        else:
            st.write('**BMI Anda menunjukkan obesitas. Perubahan gaya hidup seperti diet sehat dan olahraga teratur dapat membantu mengurangi risiko masalah kesehatan.**  '
            '[Lebih lanjut tentang Obesitas](https://www.mitrakeluarga.com/artikel/obesitas)')

# Fungsi untuk halaman Prediksi Body Fat
def body_fat_prediction():
    st.title('Prediksi Lemak Tubuh')
    
    # Input Density: Kepadatan tubuh dalam g/cm³
    density = st.number_input('**Kepadatan**', min_value=0.0, format="%.2f")
    st.write("Kepadatan tubuh, biasanya diukur dalam g/cm³. Ini adalah faktor dalam menghitung persentase lemak tubuh.")
    
    # Input Age: Usia dalam tahun
    age = st.number_input('Usia', min_value=0, format="%d")
    st.write("*Usia individu dalam tahun. Usia dapat mempengaruhi distribusi dan persentase lemak tubuh.*")
    
    # Input Weight: Berat badan dalam pon (lbs)
    weight = st.number_input('**Berat Badan (lbs)**', min_value=0.0, format="%.2f")
    st.write("*Berat badan individu dalam pon (lbs). Berat badan penting untuk menghitung persentase lemak tubuh.*")
    
    # Input Height: Tinggi badan dalam inci
    height = st.number_input('**Tinggi Badan (inci)**', min_value=0.0, format="%.2f")
    st.write("*Tinggi badan individu dalam inci. Tinggi badan adalah faktor penting lainnya dalam menghitung persentase lemak tubuh.*")
    
    # Input Neck: Lingkar leher dalam sentimeter (cm)
    neck = st.number_input('**Lingkar Leher (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar leher dalam sentimeter (cm). Lingkar leher digunakan dalam berbagai formula estimasi lemak tubuh.*")
    
    # Input Chest: Lingkar dada dalam sentimeter (cm)
    chest = st.number_input('**Lingkar Dada (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar dada dalam sentimeter (cm). Pengukuran dada dapat membantu menentukan distribusi lemak tubuh.*")
    
    # Input Abdomen: Lingkar perut dalam sentimeter (cm)
    abdomen = st.number_input('**Lingkar Perut (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar perut dalam sentimeter (cm). Pengukuran perut penting untuk menilai lemak visceral.*")
    
    # Input Hip: Lingkar pinggul dalam sentimeter (cm)
    hip = st.number_input('**Lingkar Pinggul (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar pinggul dalam sentimeter (cm). Pengukuran pinggul membantu memahami distribusi lemak tubuh.*")
    
    # Input Thigh: Lingkar paha dalam sentimeter (cm)
    thigh = st.number_input('**Lingkar Paha (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar paha dalam sentimeter (cm). Pengukuran paha berkontribusi dalam memperkirakan total lemak tubuh.*")
    
    # Input Knee: Lingkar lutut dalam sentimeter (cm)
    knee = st.number_input('**Lingkar Lutut (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar lutut dalam sentimeter (cm). Pengukuran lutut juga bisa menjadi bagian dari estimasi lemak tubuh.*")
    
    # Input Ankle: Lingkar pergelangan kaki dalam sentimeter (cm)
    ankle = st.number_input('**Lingkar Pergelangan Kaki (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar pergelangan kaki dalam sentimeter (cm). Pengukuran pergelangan kaki mungkin digunakan dalam beberapa metode estimasi lemak tubuh.*")
    
    # Input Biceps: Lingkar bisep dalam sentimeter (cm)
    biceps = st.number_input('**Lingkar Bisep (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar bisep dalam sentimeter (cm). Lingkar bisep dapat membantu menentukan massa otot versus lemak.*")
    
    # Input Forearm: Lingkar lengan bawah dalam sentimeter (cm)
    forearm = st.number_input('**Lingkar Lengan Bawah (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar lengan bawah dalam sentimeter (cm). Pengukuran lengan bawah berkontribusi pada analisis komposisi tubuh secara keseluruhan.*")
    
    # Input Wrist: Lingkar pergelangan tangan dalam sentimeter (cm)
    wrist = st.number_input('**Lingkar Pergelangan Tangan (cm)**', min_value=0.0, format="%.2f")
    st.write("*Lingkar pergelangan tangan dalam sentimeter (cm). Lingkar pergelangan tangan digunakan dalam formula estimasi lemak tubuh.*")

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