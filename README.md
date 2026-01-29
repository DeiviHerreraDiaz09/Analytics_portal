# Analytics Portal - Prueba Técnica Django

Una aplicación web profesional desarrollada con **Django 6.0.1** que demuestra la implementación de buenas prácticas en el framework.

## 📋 Objetivo

Construir una aplicación Django que demuestre comprensión profunda de la estructura del framework, incluyendo vistas, templates, paginación y estilos profesionales.

## ✅ Requisitos Cumplidos

- ✅ Proyecto llamado: `analytics_portal`
- ✅ App creada: `dashboard`
- ✅ Vista que renderiza página HTML con:
  - Título: "Analytics Portal"
  - Tabla con datos simulados del backend
- ✅ Tabla contiene 4 columnas:
  - Fecha
  - Cliente
  - Métrica
  - Valor
- ✅ Sin base de datos (datos simulados en memoria)
- ✅ **Extra**: Paginación, diseño profesional, buenas prácticas

## 🏗️ Estructura del Proyecto

```
analytics_portal/
├── static/
│   └── css/
│       └── variables.css              # Variables CSS globales
├── analytics_portal/                  # Configuración del proyecto
│   ├── settings.py                   # Configuraciones Django
│   ├── urls.py                       # URLs principales
│   ├── wsgi.py
│   └── asgi.py
├── dashboard/                         # Aplicación principal
│   ├── static/dashboard/
│   │   └── css/
│   │       └── style.css             # Estilos específicos
│   ├── templates/dashboard/
│   │   ├── index.html                # Template activo (nuevo diseño)
│   │   └── dashboard_test.html       # Template alternativo
│   ├── migrations/
│   ├── data.py                       # Datos simulados
│   ├── views.py                      # Vistas con paginación
│   ├── models.py
│   ├── tests.py
│   ├── urls.py                       # URLs de la app
│   ├── apps.py
│   └── admin.py
├── manage.py
├── requirements.txt
└── README.md
```

## 🛠️ Tecnologías Utilizadas

- **Django 6.0.1**: Framework web Python
- **Python 3.12.5**: Lenguaje de programación
- **CSS3**: Estilos (Grid, Flexbox, Gradientes, Animaciones)
- **HTML5**: Estructura semantic
- **Font Awesome 6.5.1**: Iconos (GitHub)
- **Google Fonts**: Tipografía (Roboto, Poppins)

## 💻 Instalación y Uso (Local)

### 1. Requisitos Previos
```bash
Python 3.12+
pip (gestor de paquetes)
```

### 2. Clonar/Descargar el Proyecto
```bash
git clone https://github.comDeiviHerreraDiaz09Analytics_portal.git

cd analytics_portal
```

### 3. Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar Servidor
```bash
python manage.py runserver
```

### 7. Acceder a la Aplicación
```
http://localhost:8000/
http://localhost:8000/analytics/    # Página principal
http://localhost:8000/admin/        # Panel de administración
```

## 🐳 Ejecutar el proyecto con Docker (forma sencilla)

Con Docker puedes levantar el proyecto sin instalar Python ni dependencias en tu máquina.

---

### 1. Requisitos
Tener instalados:
- Docker
- Docker Compose

Verifica:
```bash
docker --version
docker compose version
```

### 2. Levantar la aplicación

Desde la raíz del proyecto ejecuta:

```bash
docker compose up --build
```

Docker se encargará de:

- Construir la imagen
- Instalar dependencias
- Iniciar Django

### 3. Abrir en el navegador

Accede a:

```
http://localhost:8000/
http://localhost:8000/analytics/    # Página principal
http://localhost:8000/admin/        # Panel de administración
```

## Decisiones Técnicas Tomadas

- Se utilizó Django con vistas y templates tradicionales, ya que el objetivo de la prueba es demostrar comprensión de la estructura base del framework sin añadir complejidad innecesaria.

- Los datos se definieron de forma simulada en memoria, cumpliendo el requerimiento explícito de no usar base de datos ni persistencia.

- Se implementó paginación desde la vista, para demostrar manejo de grandes volúmenes de datos y buenas prácticas en la presentación.

- Se separaron estilos globales y específicos mediante CSS modular, mejorando mantenibilidad y claridad.

- La estructura del proyecto sigue las convenciones estándar de Django, facilitando escalabilidad y comprensión del código.

- Se incluyó Docker y Docker Compose como opción adicional para facilitar la ejecución del proyecto en distintos entornos.


## Principales Aprendizajes

- Refuerzo del uso correcto de vistas, templates y contexto en Django.

- Importancia de mantener una separación clara de responsabilidades entre lógica de negocio y presentación.

- Uso de paginación y datos simulados como alternativa válida para pruebas técnicas sin persistencia.

- Mejora en la organización de proyectos Django con enfoque en legibilidad y mantenibilidad.

- Valor de documentar correctamente un proyecto para facilitar su ejecución y evaluación técnica.

## 📄 Licencia

MIT License - 2026

---
