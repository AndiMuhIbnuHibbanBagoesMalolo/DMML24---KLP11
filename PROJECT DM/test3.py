import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk memuat data dari file yang diunggah
@st.cache
def load_data():
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = df.dropna()  # Menghapus baris dengan nilai yang hilang
        return df
    return None

# Sidebar untuk unggah file
st.sidebar.header('Unggah File Data')
uploaded_file = st.sidebar.file_uploader("Unggah file CSV", type=["csv"])

# Memuat dataset jika ada file yang diunggah
df = load_data(uploaded_file)

if df is not None:
    # Membuat dan melatih model
    def train_model(df):
        features = ['age', 'weight', 'height', 'neck', 'chest', 'abdom', 'hip', 'thigh', 'knee', 'ankle', 'biceps', 'forearm', 'wrist']
        X = df[features]
        y = df['bodyfat']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model, X_test, y_test, features

    model, X_test, y_test, features = train_model(df)

    # Sidebar untuk input fitur
    st.sidebar.header('Input Features')
    age = st.sidebar.number_input('Age', min_value=10, max_value=100, value=25)
    weight = st.sidebar.number_input('Weight (kg)', min_value=30.0, max_value=200.0, value=70.0)
    height = st.sidebar.number_input('Height (cm)', min_value=100.0, max_value=250.0, value=175.0)
    neck = st.sidebar.number_input('Neck Circumference (cm)', min_value=20.0, max_value=60.0, value=36.0)
    chest = st.sidebar.number_input('Chest Circumference (cm)', min_value=50.0, max_value=150.0, value=95.0)
    abdom = st.sidebar.number_input('Abdomen Circumference (cm)', min_value=50.0, max_value=150.0, value=85.0)
    hip = st.sidebar.number_input('Hip Circumference (cm)', min_value=50.0, max_value=150.0, value=95.0)
    thigh = st.sidebar.number_input('Thigh Circumference (cm)', min_value=30.0, max_value=100.0, value=55.0)
    knee = st.sidebar.number_input('Knee Circumference (cm)', min_value=20.0, max_value=60.0, value=38.0)
    ankle = st.sidebar.number_input('Ankle Circumference (cm)', min_value=10.0, max_value=40.0, value=21.0)
    biceps = st.sidebar.number_input('Biceps Circumference (cm)', min_value=20.0, max_value=60.0, value=30.0)
    forearm = st.sidebar.number_input('Forearm Circumference (cm)', min_value=15.0, max_value=50.0, value=25.0)
    wrist = st.sidebar.number_input('Wrist Circumference (cm)', min_value=10.0, max_value=30.0, value=17.0)

    # Mempersiapkan data untuk prediksi
    data_baru = pd.DataFrame({
        'age': [age],
        'weight': [weight],
        'height': [height],
        'neck': [neck],
        'chest': [chest],
        'abdom': [abdom],
        'hip': [hip],
        'thigh': [thigh],
        'knee': [knee],
        'ankle': [ankle],
        'biceps': [biceps],
        'forearm': [forearm],
        'wrist': [wrist]
    })

    # Melakukan prediksi
    prediksi_baru = model.predict(data_baru[features])

    # Menampilkan hasil
    st.write(f"Prediksi Persentase Lemak Tubuh: {prediksi_baru[0]:.2f}%")

    # Visualisasi data
    st.write("### Data Frame")
    st.write(df)

    # Evaluasi model (optional)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
    st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
else:
    st.write("bodyfat.csv")
