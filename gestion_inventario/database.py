import sqlite3
from typing import Optional

DB_NAME = "inventario.db"


def conectar_db() -> sqlite3.Connection:
    """
    Establece y devuelve el objeto de conexión a la base de datos.
    uso un gestor de contexto (with) para asegurar el cierre.
    """
    conexion = sqlite3.connect(DB_NAME)
    return conexion


def crear_tabla():
    """Crea la tabla 'productos' en la base de datos si no existe."""
    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    cantidad INTEGER NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT
                )
            """
            )

    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
