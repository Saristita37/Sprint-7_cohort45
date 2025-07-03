import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Distribución del Odómetro de Vehículos en EE.UU.")

car_data = pd.read_csv('vehicles_us.csv')
st.write("Primeras filas del dataset:", car_data.head())

fig = px.histogram(car_data, x='odometer', nbins=30, title='Histograma del Odómetro')
st.plotly_chart(fig)
