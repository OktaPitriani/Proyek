import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset dengan relative path
@st.cache_data
def load_data():
    # Menggunakan relative path, pastikan file berada di direktori yang sama dengan skrip ini
    hour_df = pd.read_csv('hour.csv')  
    return hour_df

# Visualisasi pola penyewaan sepeda di hari kerja vs akhir pekan dengan warna seragam
def plot_rental_patterns(hour_df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday', y='cnt', data=hour_df, palette='Blues')
    plt.title('Pola Penyewaan Sepeda di Hari Kerja vs Akhir Pekan', fontsize=16)
    plt.xlabel('Hari Kerja (0: Akhir Pekan, 1: Hari Kerja)', fontsize=12)
    plt.ylabel('Jumlah Penyewaan', fontsize=12)
    plt.xticks(ticks=[0, 1], labels=['Akhir Pekan', 'Hari Kerja'], fontsize=10)
    st.pyplot(plt)

# Visualisasi pengaruh cuaca terhadap penyewaan sepeda dengan penekanan warna
def plot_weather_effect(hour_df):
    plt.figure(figsize=(10, 6))
    avg_rentals_by_weather = hour_df.groupby('weathersit')['cnt'].mean().reset_index()

    # Atur warna untuk setiap kondisi cuaca secara manual
    colors = ['#1E90FF', '#66B2FF', '#99CCFF', '#CCDEFF']  # Clear, Mist, Light Rain, Heavy Rain
    
    sns.barplot(x='weathersit', y='cnt', data=avg_rentals_by_weather, palette=colors)
    
    plt.title('Pengaruh Cuaca Terhadap Penyewaan Sepeda', fontsize=16)
    plt.xlabel('Kondisi Cuaca', fontsize=12)
    plt.ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Clear', 'Mist', 'Light Rain', 'Heavy Rain'], fontsize=10)
    st.pyplot(plt)

# Menampilkan judul dashboard di Streamlit
st.title("Dashboard Penyewaan Sepeda")

# Load data
hour_df = load_data()

# Tampilkan data awal
st.write("Data Penyewaan Sepeda:")
st.dataframe(hour_df, use_container_width=True)  # Tampilkan seluruh isi DataFrame

# Buat menu radio untuk memilih visualisasi
menu = st.radio(
    "Pilih indikator visualisasi:",
    ("Pola Penyewaan Sepeda di Hari Kerja dan Akhir Pekan", "Pengaruh Cuaca Terhadap Penyewaan Sepeda")
)

# Tampilkan visualisasi sesuai pilihan
if menu == "Pola Penyewaan Sepeda di Hari Kerja dan Akhir Pekan":
    st.subheader("Pola Penyewaan Sepeda di Hari Kerja dan Akhir Pekan")
    plot_rental_patterns(hour_df)
elif menu == "Pengaruh Cuaca Terhadap Penyewaan Sepeda":
    st.subheader("Pengaruh Cuaca Terhadap Penyewaan Sepeda")
    plot_weather_effect(hour_df)
