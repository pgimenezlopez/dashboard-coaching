import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import streamlit as st

# Inicializar Firebase con secrets.toml
def init_firebase():
    try:
        firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate(st.secrets["FIREBASE"])
        firebase_admin.initialize_app(cred)

# Guardar una sesión
def guardar_sesion(usuario_email, cliente, fecha, claridad, objetivo, accion, estado):
    init_firebase()
    db = firestore.client()

    if isinstance(fecha, datetime):
        fecha_str = fecha.strftime("%Y-%m-%d")
    else:
        fecha_str = str(fecha)

    doc_ref = db.collection("usuarios").document(usuario_email).collection("clientes").document(cliente).collection("sesiones").document(fecha_str)
    doc_ref.set({
        "fecha": fecha,
        "nivel_claridad": claridad,
        "objetivo": objetivo,
        "accion": accion,
        "estado": estado,
        "timestamp": datetime.utcnow()
    })

# Leer sesiones de un cliente
def leer_sesiones(usuario_email, cliente):
    init_firebase()
    db = firestore.client()
    sesiones_ref = db.collection("usuarios").document(usuario_email).collection("clientes").document(cliente).collection("sesiones")
    docs = sesiones_ref.order_by("fecha").stream()
    sesiones = []
    for doc in docs:
        data = doc.to_dict()
        sesiones.append({
            "Fecha": data["fecha"].strftime("%Y-%m-%d") if isinstance(data["fecha"], datetime) else str(data["fecha"]),
            "Nivel de claridad (1-10)": data["nivel_claridad"],
            "Objetivo de sesión": data["objetivo"],
            "Acción comprometida": data["accion"],
            "Estado de avance": data["estado"]
        })
    return sesiones
