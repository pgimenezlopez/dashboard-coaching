import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, date

def init_firebase():
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_dict = dict(st.secrets["FIREBASE"])
        firebase_dict["private_key"] = firebase_dict["private_key"].replace("\\n", "\n").replace("\n", "\n").encode().decode("unicode_escape")
        cred = credentials.Certificate(firebase_dict)
        firebase_admin.initialize_app(cred)

def guardar_sesion(usuario, cliente, fecha, claridad, objetivo, accion, estado, observaciones=""):
    init_firebase()
    db = firestore.client()
    doc_ref = db.collection("usuarios").document(usuario).collection("clientes").document(cliente).collection("sesiones").document()
    doc_ref.set({
        "Fecha": fecha.isoformat(),
        "Nivel de claridad (1-10)": claridad,
        "Objetivo de sesión": objetivo,
        "Acción comprometida": accion,
        "Estado de avance": estado,
        "Observaciones": observaciones or ""  # 👈 Asegura que no falle si viene vacío
    })


def leer_sesiones(usuario, cliente):
    init_firebase()
    db = firestore.client()
    sesiones_ref = db.collection("usuarios").document(usuario).collection("clientes").document(cliente).collection("sesiones")
    docs = sesiones_ref.order_by("Fecha").stream()
    sesiones = []
    for doc in docs:
        data = doc.to_dict()
        if "Observaciones" not in data:
            data["Observaciones"] = ""  # 👈 Si no existe, agrega campo vacío
        sesiones.append(data)
    return sesiones


def listar_clientes(usuario_email):
    init_firebase()
    db = firestore.client()
    clientes_ref = db.collection("usuarios").document(usuario_email).collection("clientes")
    documentos = clientes_ref.stream()
    return [doc.id for doc in documentos]