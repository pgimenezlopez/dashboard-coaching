from supabase import create_client
from datetime import datetime

# 🔐 Reemplazá con tus credenciales de Supabase
url = "https://ophypahgfhhknircimab.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9waHlwYWhnZmhoa25pcmNpbWFiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk1NzU3MjksImV4cCI6MjA2NTE1MTcyOX0.wi_ytU9pa4TW1cWKI1l4rz7o4stCU0kP4KBDJ_F-9r4
supabase = create_client(url, key)

def guardar_sesion(usuario, cliente, fecha, claridad, objetivo, accion, estado):
    data = {
        "usuario": usuario,
        "cliente": cliente,
        "fecha": fecha.isoformat(),
        "claridad": claridad,
        "objetivo": objetivo,
        "accion": accion,
        "estado": estado
    }
    supabase.table("sesiones").insert(data).execute()

def leer_sesiones(usuario, cliente):
    result = supabase.table("sesiones").select("*").eq("usuario", usuario).eq("cliente", cliente).order("fecha").execute()
    if result.data:
        for item in result.data:
            item["Fecha"] = datetime.fromisoformat(item["fecha"]).date()
            item["Nivel de claridad (1-10)"] = item["claridad"]
            item["Objetivo de sesión"] = item["objetivo"]
            item["Acción comprometida"] = item["accion"]
            item["Estado de avance"] = item["estado"]
        return result.data
    return []