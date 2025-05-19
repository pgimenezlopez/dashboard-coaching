# 🧠 Dashboard de Coaching Personalizado

Este proyecto es una aplicación web interactiva que permite a coaches realizar el seguimiento de sus clientes y sesiones de manera visual y organizada. Está desarrollado en Python con Streamlit, y utiliza Firebase como backend para almacenar la información en la nube.

---

## 🚀 Funcionalidades principales

- Registro de sesiones de coaching por cliente
- Visualización de métricas clave (claridad, acciones completadas)
- Gráfico interactivo de evolución
- Base de datos segura en la nube (Firestore)
- Compatible con despliegue local o en Streamlit Cloud

---

## 🛠️ Stack Tecnológico

| Componente        | Tecnología                     |
|-------------------|--------------------------------|
| Lenguaje          | Python 3.10                    |
| Framework UI      | [Streamlit](https://streamlit.io/) |
| Gráficos          | Plotly Express                 |
| Base de datos     | Firebase Firestore (NoSQL)     |
| Autenticación     | Firebase Admin SDK             |
| Configuración     | `secrets.toml` para credenciales |
| Hosting opcional  | Streamlit Cloud                |

---

## 🧩 Estructura de datos en Firebase

```
usuarios/
  └── {correo_usuario}/
       └── clientes/
            └── {nombre_cliente}/
                 └── sesiones/
                      └── {fecha}/ → datos de la sesión
```

---

## 📦 Requisitos (`requirements.txt`)

```
streamlit
pandas
plotly
firebase-admin
```

---

## 🔧 Instalación y ejecución (modo local)

1. Cloná el repositorio:

```bash
git clone https://github.com/tu_usuario/dashboard-coaching.git
cd dashboard-coaching
```

2. Creá el archivo `.streamlit/secrets.toml` con las credenciales de Firebase:

```toml
[FIREBASE]
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = """-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----"""
client_email = "..."
...
```

3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutá la app:

```bash
streamlit run dashboard_visual_mejorado.py
```

---

## ☁️ Despliegue en Streamlit Cloud

1. Subí tu repositorio a GitHub
2. Entrá en [https://streamlit.io/cloud](https://streamlit.io/cloud) y conectá el repo
3. Cargá los secrets desde el panel de configuración
4. ¡Listo para compartir con tus clientes!

---

## 🧑‍💻 Autor

**Pablo Giménez**  
Ingeniero en Computación | Consultor en Gestión de Proyectos | Emprendiendo con ciencia de datos y herramientas visuales.

---

## 📬 Contacto

¿Te interesa probarlo, adaptarlo o colaborar?  
Contactame por GitHub o [LinkedIn](https://www.linkedin.com).

---