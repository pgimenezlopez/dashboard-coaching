# 🧠 Dashboard de Coaching Personalizado

App interactiva para coaches que permite registrar y visualizar sesiones de sus clientes. Desarrollada en Python con Streamlit y Firebase.

---

## 🚀 Funcionalidades principales

- Registro de sesiones de coaching por cliente
- Visualización de métricas clave
- Gráfico de evolución de claridad
- Datos guardados en Firebase Firestore
- Diseño visual limpio y simple

---

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.10
- **Frontend:** Streamlit
- **Gráficos:** Plotly Express
- **Base de datos:** Firebase Firestore (NoSQL)
- **Backend:** Firebase Admin SDK
- **Gestión de secretos:** `secrets.toml`
- **Entorno:** Local con opción de despliegue en Streamlit Cloud

---

## 🔧 Instalación y ejecución local

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu_usuario/dashboard-coaching.git
cd dashboard-coaching
```

2. **Crear archivo de configuración: `.streamlit/secrets.toml`**

```toml
[FIREBASE]
type = "service_account"
project_id = "tu_proyecto"
private_key_id = "xxxxx"
private_key = """-----BEGIN PRIVATE KEY-----
TU_CLAVE_PRIVADA
-----END PRIVATE KEY-----"""
client_email = "xxxxx"
client_id = "xxxxx"
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecutar la app**

```bash
streamlit run dashboard_visual_mejorado.py
```

---

## ☁️ Despliegue en Streamlit Cloud

1. Subí tu proyecto a GitHub
2. Entrá a [streamlit.io/cloud](https://streamlit.io/cloud)
3. Conectá tu repo y cargá los secrets desde el panel
4. Publicá tu app

---

## 📬 Autor

**Pablo Giménez**  
Ingeniero en Computación — Gestión de Proyectos — Ciencia de Datos Visual