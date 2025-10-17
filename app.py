import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Cuadro de mandos: Análisis de anuncios de coches en EE. UU.')

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# ✅ AQUI agregamos el botón de dispersión antes del "if"
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: Precio vs Odómetro')
    fig2 = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    ))
    fig2.update_layout(title_text='Precio vs Odómetro')
    st.plotly_chart(fig2, use_container_width=True)

    
