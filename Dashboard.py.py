

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# LOAD DATA
@st.cache(allow_output_mutation=True)
def load_data():
    # lokasi file
    data_day = pd.read_csv("/content/day.zip")
    data_hour = pd.read_csv("/content/hour.csv.zip")
    return data_day, data_hour
    data_day, data_hour = load_data()

# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Sharing Dashboard")

# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Maulidina Maulani**")
st.sidebar.markdown("**• Email: mlidinalni@gmail.com**")
st.sidebar.title("Dataset Bike Share")

# MAIN PAGE
# ==============================
# PAGE: Visualisasi 1
# ==============================

# Mengimpor data dari file CSV
data_day = pd.read_csv('/content/day.zip')

st.header("Visualisasi 1: Jumlah Penyewaan Sepeda yang sudah didistribusikan berdasarkan musim")
fig1 = px.box(data_day, x='season', y='cnt',
              labels={'cnt':'Jumlah Penyewaan Sepeda', 'season':'Musim'},
              category_orders={"season": ["1", "2", "3", "4"]})
fig1.update_traces(quartilemethod="inclusive")
fig1.update_xaxes(title_text='Musim')
fig1.update_yaxes(title_text='Jumlah Penyewaan Sepeda')
st.plotly_chart(fig1)

# PAGE: Visualisasi 2
# ==============================
st.header("Visualisasi 2: Pola Penyewaan Sepeda Weekday dan Weekend")
fig2 = px.box(data_day, x='workingday', y='cnt',
              labels={'cnt':'Jumlah Penyewaan Sepeda', 'workingday':'Model Type Day'},
              category_orders={"workingday": ["0", "1"]})
fig2.update_xaxes(title_text='Tipe Hari', tickvals=[0, 1], ticktext=['Weekend', 'Weekday'])
fig2.update_yaxes(title_text='Jumlah Penyewaan Sepeda')
st.plotly_chart(fig2)