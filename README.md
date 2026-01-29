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

## 🚀 Características Implementadas

### 1. **Datos Simulados Profesionales**
- Módulo `data.py` con función `get_analytics_data()`
- 12 registros de ejemplo con fechas dinámicas
- 3 empresas monitoreadas (Empresa A, B, C)
- 3 tipos de métricas (Visitantes, Conversiones, Click-Through Rate)

### 2. **Paginación Server-Side (Django)**
```python
from django.core.paginator import Paginator

paginator = Paginator(analytics_data, 5)  # 5 registros por página
page_obj = paginator.get_page(page_number)
```
- 5 registros por página
- Navegación con botones Anterior/Siguiente
- Gestión completa en backend (Python)
- URLs con parámetro `?page=`
- Control inteligente de botones (deshabilitados en primera/última página)

### 3. **Diseño Profesional**
- **Gradiente visual**: Fondo morado-azul (#667eea → #764ba2)
- **Layout Grid CSS**: Estructura de 12 columnas x 17 filas
- **Tipografía moderna**: Fuentes Roboto y Poppins
- **Tabla estilizada**: Bordes redondeados, hover effects
- **Animaciones sutiles**: Botones interactivos con transiciones

### 4. **Componentes Visuales**

#### Header
- Título "Analytics Portal" en caja redondeada
- Línea divisoria vertical
- Diseño simétrico y elegante

#### Presentation (Izquierda)
- Título con efecto de texto duplicado (pseudo-elemento ::before)
- Descripción del portal
- Icono GitHub animado (scale + rotate en hover)

#### Table (Derecha)
- Tabla con 4 columnas
- Encabezado morado con bordes redondeados
- Filas alternas con colores suaves
- Hover effects en filas
- Scroll automático para datos
- Paginación con botones cian/turquesa

#### Footer
- Información de copyright
- Posicionada en fila 16 del grid

### 5. **Variables CSS Globales**
```css
:root {
  /* Grid */
  --grid-columns: 12;
  --grid-rows: 17;
  
  /* Dimensiones */
  --w-cell: 8.33vw;
  --h-cell: 3.3088vw;
  
  /* Colores */
  --R1-color: #eb162c;
  --B2-color: #1e8c93;
  --W1-color: #eee8f2;
  
  /* Tipografía */
  --main-font: "Poppins", Arial;
  --poppins-font: "Poppins", sans-serif;
  
  /* Pesos */
  --font-normal: 400;
  --font-semi-bold: 600;
  --font-bold: 700;
}
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


## 📊 Flujo de Datos

```
request (GET /analytics/?page=2)
    ↓
views.py (dashboard function)
    ↓ get_analytics_data() → 12 registros
    ↓ Paginator(data, 5) → 3 páginas
    ↓ get_page(2) → registros 5-10
    ↓
context = {
  'analytics_data': [...],    # 5 registros de página 2
  'page_obj': <Page 2 of 3>,  # Info paginación
  'paginator': <Paginator>
}
    ↓
template render (index.html)
    ↓
HTML + CSS renderizado
    ↓
response (Página 2 con botones)
```

## 🧪 Testing

Ejecutar tests unitarios:
```bash
python manage.py test dashboard
```

Tests incluidos:
- ✅ Accesibilidad de vistas
- ✅ Templates correctos
- ✅ Contexto esperado
- ✅ Estructura de datos
- ✅ Contenido HTML

Ejecutar con verbosidad:
```bash
python manage.py test dashboard --verbosity=2
```

## 📄 Licencia

MIT License - 2026

---

**Nota:** Esta es una prueba técnica que demuestra habilidades en:
- ✅ Django (vistas, templates, paginación)
- ✅ HTML5 (semántica, estructura)
- ✅ CSS3 (grid, flexbox, animaciones, variables)
- ✅ Python (organización de código, buenas prácticas)
- ✅ Desarrollo Web Profesional (escalabilidad, mantenibilidad)

