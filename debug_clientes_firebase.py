import streamlit as st
from firebase_conexion import listar_clientes, guardar_sesion
from datetime import datetime

st.title("🧪 Debug Firebase: Clientes registrados")

usuario_email = "coachdemo@email.com"

# Mostrar clientes actuales desde Firebase
clientes = listar_clientes(usuario_email)
if clientes:
    st.success(f"Clientes detectados: {clientes}")
else:
    st.warning("⚠️ No se encontraron clientes. Probá guardar una sesión primero.")

# Agregar cliente de prueba para verificar si guarda correctamente
if st.button("➕ Crear cliente ficticio (TestUser)"):
    guardar_sesion(
        usuario_email=usuario_email,
        cliente="TestUser",
        fecha=datetime.now(),
        claridad=7,
        objetivo="Objetivo de prueba",
        accion="Acción de prueba",
        estado="En progreso"
    )
    st.success("Cliente 'TestUser' creado con sesión ficticia. Volvé a cargar.")