import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("./vehicles_us.csv")
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Mostrar gráfico de dispersión')

st.header('Crear un histograma')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')                
    fig = px.histogram(car_data, x="odometer")   # crear un histograma    
    st.plotly_chart(fig, use_container_width=True)  # mostrar un gráfico Plotly interactivo

if scatter_button:  # Al hacer clic en el botón de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color='fuel')  # Crear gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)    # Mostrar gráfico de dispersión