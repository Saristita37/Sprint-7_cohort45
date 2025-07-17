import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis de venta de vehículos usados EEUU")

car_data = pd.read_csv('vehicles_us.csv')
hist_button=st.button('Construir histograma de kilomentraje')

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_lineplot=st.checkbox('Construir evolución de precio')

if build_lineplot:
    st.write('Evolución precio promedio según condiciones del vehículo')

    df = car_data.groupby(['date_posted', 'condition'])['price'].mean().reset_index()
    fig_2=px.line(df, x='date_posted', y='price', color='condition',
                  title='precio promedio vehículos según día de publicación')
    st.plotly_chart(fig_2, use_container_width=True)
