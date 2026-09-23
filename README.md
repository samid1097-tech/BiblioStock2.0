BiblioStock 2.0
BiblioStock 2.0 es un sistema de gestión e inventario diseñado para controlar y administrar el catálogo de libros, préstamos y stock de una biblioteca de forma sencilla y eficiente desde la consola.
---
Características Principales
Registro e Inventario: Permite agregar nuevos libros al sistema almacenando detalles como título, autor, año y cantidad disponible.
Búsqueda y Consultas: Búsqueda rápida de libros por título, autor o categoría.
Gestión de Préstamos: Control e historial de libros prestados y devueltos.
Persistencia de Datos: Guardado automático de información en archivos locales (JSON / Base de Datos).
---
Requisitos Previos
Asegúrate de contar con lo siguiente en tu entorno local:
Python 3.10+
Git
---
Instalación y Configuración
Sigue estos pasos para clonar el repositorio y ejecutar la aplicación en tu máquina local:
Clonar el repositorio:
```bash
   git clone https://github.com/samid1097-tech/BiblioStock2.0.git
   cd BiblioStock2.0
   ```
Crear y activar un entorno virtual (opcional pero recomendado):
En Windows:
```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
En macOS / Linux:
```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
Instalar dependencias (si aplica):
```bash
   pip install -r requirements.txt
   ```
---
Uso
Para iniciar el menú de la aplicación, ejecuta el módulo principal desde la terminal:
```bash
python main.py
```
---
Estructura del Proyecto
```text
BiblioStock2.0/
│
├── main.py              # Punto de entrada de la aplicación
├── inventario.py        # Módulo de administración de libros y stock
├── datos/               # Archivos de datos locales (JSON / SQLite)
├── .gitignore           # Archivos omitidos en el control de versiones
└── README.md            # Documentación del proyecto
```
---
Colaboradores
Samid Plata (@samid1097-tech)
David (@davi662)
juan manuel (@castrorueda-afk)
camilo (@Unbornx18)