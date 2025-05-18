import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, date

def init_firebase():
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_dict = dict(st.secrets["FIREBASE"])
        # Decodificamos la private_key para que tenga saltos de línea reales
        firebase_dict["private_key"] = firebase_dict["private_key"].replace("\\n", "\n")
        cred = credentials.Certificate(firebase_dict)
        firebase_admin.initialize_app(cred)


def guardar_sesion(usuario_email, cliente, fecha, claridad, objetivo, accion, estado):
    init_firebase()
    db = firestore.client()
    if isinstance(fecha, date):
        fecha = datetime.combine(fecha, datetime.min.time())
    doc_ref = db.collection("usuarios").document(usuario_email).collection("clientes").document(cliente).collection("sesiones").document(fecha.strftime("%Y-%m-%d"))
    doc_ref.set({
        "fecha": fecha,
        "nivel_claridad": claridad,
        "objetivo": objetivo,
        "accion": accion,
        "estado": estado,
        "timestamp": datetime.utcnow()
    })

def leer_sesiones(usuario_email, cliente):
    init_firebase()
    db = firestore.client()
    sesiones_ref = db.collection("usuarios").document(usuario_email).collection("clientes").document(cliente).collection("sesiones")
    docs = sesiones_ref.order_by("fecha").stream()
    sesiones = []
    for doc in docs:
        data = doc.to_dict()
        sesiones.append({
            "Fecha": data["fecha"].strftime("%Y-%m-%d"),
            "Nivel de claridad (1-10)": data["nivel_claridad"],
            "Objetivo de sesión": data["objetivo"],
            "Acción comprometida": data["accion"],
            "Estado de avance": data["estado"]
        })
    return sesiones