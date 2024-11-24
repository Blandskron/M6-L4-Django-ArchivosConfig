# **Proyecto Django: Sistema de Gestión de Ítems**

Este proyecto es una aplicación web desarrollada en **Django 5.1.3**, diseñada para gestionar y visualizar una lista de ítems con un diseño modular, interacción dinámica, y un enfoque en la escalabilidad. Se incluye un sistema de alternancia de temas (claro y oscuro) y una arquitectura optimizada para paginación y mantenimiento.

---

## **Características del Proyecto**

### **1. Funcionalidad Principal**
- **Gestión de Ítems:**
  - Visualización de una lista de ítems con nombre, descripción y precio.
  - Paginación para mejorar la navegación cuando la lista contiene muchos elementos.

- **Interacción Dinámica:**
  - Alternancia entre tema claro y oscuro mediante un botón interactivo con persistencia utilizando `localStorage`.

---

### **2. Estructura Modular**
- **Plantillas Reutilizables:**
  - Estructura basada en `base.html` que organiza el encabezado, pie de página, y el contenido principal.
  - Componentes como `header.html` y `footer.html` facilitan la personalización.

- **Estilos Manejados Modularmente:**
  - Estilos específicos para encabezados, pie de página, listas de ítems y temas claros/oscuros, separados en archivos CSS independientes.

- **Paginación:**
  - Implementada para mostrar 10 ítems por página, garantizando rendimiento y usabilidad.

---

## **Requisitos del Sistema**
- Python 3.8+
- Django 5.1.3
- Base de datos SQLite (configurada por defecto, compatible con PostgreSQL para producción).

---

## **Configuración del Proyecto**

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. **Configura el entorno virtual e instala dependencias:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Aplica las migraciones iniciales:**
   ```bash
   python manage.py migrate
   ```

4. **Carga datos iniciales (opcional):**
   - Inicia el shell interactivo y ejecuta el script de carga:
     ```bash
     python manage.py shell
     ```
     ```python
     from myapp.models import Item
     Item.objects.create(name="Laptop", description="Potente laptop", price=1200.99)
     # Agrega más ítems según lo necesites.
     ```

5. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Accede a la aplicación:**
   - Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## **Estructura del Proyecto**

### **1. Archivos Clave**
| Archivo         | Propósito                                                     |
|------------------|---------------------------------------------------------------|
| `base.html`      | Plantilla principal para todas las páginas.                   |
| `item_list.html` | Renderiza los ítems con paginación y temas dinámicos.          |
| `main.js`        | Maneja la alternancia entre temas claro y oscuro.              |
| `header.css`     | Estilos para el encabezado de la página.                       |
| `footer.css`     | Estilos para el pie de página.                                 |
| `item_list.css`  | Estilos para la lista de ítems.                                |
| `styles.css`     | Estilos generales y temas globales para la aplicación.         |

### **2. Modelos**
- **`Item`:**
  - Modelo que representa los ítems de la aplicación.
  - Atributos:
    - `name` (nombre del ítem).
    - `description` (descripción del ítem).
    - `price` (precio del ítem, con validación para ser positivo).
    - `created_at` (fecha de creación automática).

### **3. Vistas**
- **`item_list`:**
  - Vista basada en funciones que:
    - Recupera todos los ítems de la base de datos.
    - Implementa paginación para mostrar 10 ítems por página.
    - Maneja excepciones relacionadas con la base de datos.

---

## **Cómo Personalizar el Proyecto**

1. **Agregar más ítems:**
   - Modifica el script de carga inicial o utiliza el shell de Django para crear ítems adicionales.

2. **Cambiar estilos:**
   - Edita los archivos CSS (`header.css`, `footer.css`, etc.) para personalizar el diseño según tus necesidades.

3. **Actualizar el tema:**
   - Amplía el script en `main.js` para agregar más opciones de personalización del tema.

4. **Migrar a PostgreSQL:**
   - Configura `DATABASES` en `settings.py` para usar PostgreSQL en lugar de SQLite.

---
