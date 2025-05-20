import firebase_admin
from firebase_admin import credentials, firestore
import json

# 🔑 Inicializar Firebase con tu clave
with open("firebase_key.json") as f:
    firebase_dict = json.load(f)

cred = credentials.Certificate(firebase_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()

usuario_email = "coachdemo@email.com"

clientes_ref = db.collection("usuarios").document(usuario_email).collection("clientes")
clientes_docs = clientes_ref.stream()

for cliente_doc in clientes_docs:
    cliente_id = cliente_doc.id
    sesiones_ref = clientes_ref.document(cliente_id).collection("sesiones")
    sesiones_docs = sesiones_ref.stream()

    for sesion_doc in sesiones_docs:
        data = sesion_doc.to_dict()
        #if "Observaciones" not in data:
        print(f"Actualizando sesión de {cliente_id}...")
        sesiones_ref.document(sesion_doc.id).update({"Observaciones": "dummy"})
