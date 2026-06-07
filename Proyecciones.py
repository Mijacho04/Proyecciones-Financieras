import streamlit as st
import pandas as pd

# Configuramos la página para que se vea profesional
st.set_page_config(page_title="Finanzas Proyectadas", layout="wide")

st.title("Sistema de Proyecciones Financieras")
st.write("Bienvenido. Comencemos cargando la información base de tu empresa.")

# --- PASO 1: MEMORIA DE LA APP ---
# Esto evita que la página olvide los datos al hacer clic en botones
if 'datos_empresa' not in st.session_state:
    st.session_state['datos_empresa'] = None

# --- PASO 2: BOTÓN CARGAR ---
archivo_subido = st.file_uploader("Elige tu archivo Excel", type=["xlsx"])

if archivo_subido is not None:
    # Leemos el archivo y lo guardamos en la "memoria" de la sesión
    df = pd.read_excel(archivo_subido)
    st.session_state['datos_empresa'] = df
    st.success("✅ Archivo cargado y guardado en memoria con éxito.")

# --- PASO 3: BOTÓN VER Y OPCIÓN SUMAS Y SALDOS ---
# Solo mostramos estas opciones si ya hay un archivo cargado
if st.session_state['datos_empresa'] is not None:
    st.divider() # Una línea decorativa
    
    col1, col2 = st.columns([1, 3]) # Dividimos en columnas para que se vea ordenado

    with col1:
        st.subheader("Menú de Análisis")
        # El botón "Ver" que despliega la opción
        if st.button("Ver Sumas y Saldos"):
            st.session_state['ver_analisis'] = True
        else:
            if 'ver_analisis' not in st.session_state:
                st.session_state['ver_analisis'] = False

    with col2:
        if st.session_state.get('ver_analisis'):
            st.subheader("📊 Despliegue: Sumas y Saldos")
            # Mostramos la tabla de datos del Excel
            st.dataframe(st.session_state['datos_empresa'], use_container_width=True)
            
            # Un pequeño resumen automático para impresionar al cliente
            st.info(f"El archivo contiene {len(st.session_state['datos_empresa'])} registros contables.")
