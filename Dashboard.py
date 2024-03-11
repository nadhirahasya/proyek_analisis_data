import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data
day_df = pd.read_csv("main_data.csv")
hour_df = pd.read_csv("main_data.csv")

# Mengonversi kolom 'dteday' menjadi tipe data datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Menampilkan informasi dan statistik deskriptif
st.write("Info dataset day_df:")
st.write(day_df.info())

st.write("Jumlah duplikasi dalam dataset day_df:")
st.write(day_df.duplicated().sum())

st.write("Deskripsi dataset day_df:")
st.write(day_df.describe(include='all'))

st.write("Info dataset hour_df:")
st.write(hour_df.info())

st.write("Jumlah duplikasi dalam dataset hour_df:")
st.write(hour_df.duplicated().sum())

st.write("Deskripsi dataset hour_df:")
st.write(hour_df.describe(include='all'))

# Visualisasi Histogram Jumlah Peminjaman Sepeda per Bulan
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(day_df['mnth'], bins=12, color='pink', edgecolor='black')
ax.set_title('Histogram Jumlah Peminjaman Sepeda per Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Peminjaman')
ax.set_xticks(range(1, 13))
ax.grid(True)
st.pyplot(fig)

# Mengelompokkan data untuk jumlah peminjaman sepeda berdasarkan kondisi cuaca
cnt_by_weather = day_df.groupby('weathersit')['cnt'].sum().reset_index()

# Visualisasi Jumlah Peminjaman Sepeda berdasarkan Kondisi Cuaca
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=cnt_by_weather, palette='coolwarm', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Peminjaman Sepeda')
st.pyplot(fig)
