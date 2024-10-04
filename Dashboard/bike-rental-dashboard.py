import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    hour_df = pd.read_csv(r'C:\xampp\htdocs\stupen\hour.csv')
    return hour_df


def plot_rental_patterns(hour_df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday', y='cnt', data=hour_df)
    plt.title('Pola Penyewaan Sepeda di Hari Kerja vs Akhir Pekan')
    plt.xlabel('Hari Kerja (0: Akhir Pekan, 1: Hari Kerja)')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks(ticks=[0, 1], labels=['Akhir Pekan', 'Hari Kerja'])
    st.pyplot(plt)

def plot_weather_effect(hour_df):
    plt.figure(figsize=(10, 6))
    avg_rentals_by_weather = hour_df.groupby('weathersit')['cnt'].mean().reset_index()
    sns.barplot(x='weathersit', y='cnt', data=avg_rentals_by_weather, palette='viridis')
    plt.title('Pengaruh Cuaca Terhadap Penyewaan Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Penyewaan')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Clear', 'Mist', 'Light Rain', 'Heavy Rain'])
    st.pyplot(plt)

st.title("Dashboard Penyewaan Sepeda")

hour_df = load_data()


st.write("Data Penyewaan Sepeda:")
st.dataframe(hour_df.head())


st.subheader("Pola Penyewaan Sepeda di Hari Kerja dan Akhir Pekan")
plot_rental_patterns(hour_df)

st.subheader("Pengaruh Cuaca Terhadap Penyewaan Sepeda")
plot_weather_effect(hour_df)
