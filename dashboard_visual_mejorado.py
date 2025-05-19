import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, datetime
from firebase_conexion import guardar_sesion, leer_sesiones, listar_clientes
import io

st.set_page_config(layout="wide")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Dashboard de Coaching Mejorado")
st.markdown("Seguimiento visual, análisis y exportación de sesiones de coaching con datos en la nube (Firebase).")

# Usuario simulado (en producción usar login real)
usuario_email = "coachdemo@email.com"

# Ingreso manual o selección de cliente
clientes = listar_clientes(usuario_email)

st.markdown("## 🧑‍💼 Cliente")
nuevo_cliente = st.checkbox("Agregar nuevo cliente")
if nuevo_cliente:
    cliente = st.text_input("Nombre del nuevo cliente")
else:
    cliente = st.selectbox("Seleccionar cliente", clientes)

# Registro de sesión
st.markdown("## ✍️ Registrar nueva sesión")
with st.form("registro_sesion"):
    fecha = st.date_input("Fecha", value=date.today())
    claridad = st.slider("Claridad (1-10)", 1, 10, 5)
    objetivo = st.text_input("Objetivo trabajado")
    accion = st.text_input("Acción comprometida")
    estado = st.selectbox("Estado", ["Completado", "En progreso", "Pendiente"])
    observaciones = st.text_area("Observaciones (opcional)")
    submitted = st.form_submit_button("Guardar")

    if submitted and cliente:
        guardar_sesion(usuario_email, cliente, datetime.combine(fecha, datetime.min.time()), claridad, objetivo, accion, estado, observaciones)
        st.success("✅ Sesión guardada")

# Visualización
if cliente:
    sesiones = leer_sesiones(usuario_email, cliente)
    if sesiones:
        df = pd.DataFrame(sesiones)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        df["Semana"] = df["Fecha"].dt.strftime("%Y-%U")
        df["Mes"] = df["Fecha"].dt.strftime("%Y-%m")

        st.markdown("---")
        col1, col2 = st.columns(2)
        col1.metric("Total de sesiones", len(df))
        col2.metric("Promedio claridad", round(df["Nivel de claridad (1-10)"].mean(), 2))

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("📊 Distribución de estados")
            fig_estado = px.pie(df, names="Estado de avance", title="Sesiones por estado", hole=0.4)
            st.plotly_chart(fig_estado, use_container_width=True)

        with col4:
            st.subheader("📈 Claridad semanal")
            claridad_sem = df.groupby("Semana")["Nivel de claridad (1-10)"].mean().reset_index()
            fig_claridad = px.bar(claridad_sem, x="Semana", y="Nivel de claridad (1-10)", text_auto=True)
            fig_claridad.update_layout(height=400)
            st.plotly_chart(fig_claridad, use_container_width=True)

        st.markdown("## 📋 Sesiones detalladas")
        st.dataframe(df[["Fecha", "Objetivo de sesión", "Estado de avance", "Observaciones"]], use_container_width=True)

        st.markdown("## 📥 Descargar sesiones en Excel")
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, sheet_name="Sesiones")
        st.download_button(
            label="📁 Descargar Excel",
            data=buffer.getvalue(),
            file_name=f"sesiones_{cliente.lower()}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.info("No hay sesiones aún.")
