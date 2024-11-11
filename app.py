import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título en la interfaz de Streamlit
st.header('Análisis de archivo vehículos proyecto sprint 6')

# Crear un botón para construir el histograma
hist_button = st.button('Construir histograma')
if hist_button:  # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un checkbox para construir un scatter
build_scatter = st.checkbox('Construir un scatter')
if build_scatter:  # Al hacer clic en el checkbox
    # Escribir un mensaje
    st.write('Creación de un scatter')
    
    # Crear un gráfico de dispersión (scatter plot)
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico scatter
    st.plotly_chart(fig_scatter, use_container_width=True)

        

