<!-- @format -->

# 📦 Sistema de Gestión de Inventario (CLI)

Aplicación de línea de comandos (CLI) desarrollada en Python para gestionar de manera eficiente el inventario de productos. Utiliza **SQLite** como base de datos persistente y la biblioteca **Colorama** para ofrecer una interfaz de usuario atractiva y legible.

---

## ✨ Características Principales

-   **CRUD Completo:** Funcionalidades para **C**rear, **L**eer, **A**ctualizar y **E**liminar productos.
-   **Base de Datos Persistente:** Usa **SQLite** para almacenar los datos localmente, asegurando que la información se mantenga entre sesiones.
-   **Búsqueda Flexible:** Permite buscar productos por ID, nombre (parcial) o categoría.
-   **Reporte de Bajo Stock:** Genera informes de productos con cantidad igual o inferior a un límite definido.
-   **Diseño Modular:** El proyecto está estructurado en módulos para fácil mantenimiento y escalabilidad.

---

## 🛠️ Estructura de la Base de Datos

El sistema utiliza una única tabla llamada `productos` con la siguiente estructura:

| Campo           | Tipo de Dato | Restricciones                | Propósito                               |
| :-------------- | :----------- | :--------------------------- | :-------------------------------------- |
| **id**          | `INTEGER`    | `PRIMARY KEY, AUTOINCREMENT` | Identificador único del producto.       |
| **nombre**      | `TEXT`       | `NOT NULL`                   | Nombre descriptivo del producto.        |
| **descripcion** | `TEXT`       | `NULL`                       | Detalles adicionales del producto.      |
| **cantidad**    | `INTEGER`    | `NOT NULL`                   | Stock disponible actual.                |
| **precio**      | `REAL`       | `NOT NULL`                   | Precio de venta del producto.           |
| **categoria**   | `TEXT`       | `NULL`                       | Categoría o clasificación del producto. |

---

## 🚀 Instalación y Ejecución

Sigue estos sencillos pasos para poner en marcha el sistema en tu máquina local.

### 1. Requisitos

Necesitas tener **Python 3.x** instalado.

### 2. Instalar Colorama

```bash
pip install coloram
```

### 3. Correr el archivo main.py
