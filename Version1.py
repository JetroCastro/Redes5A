import sqlite3

"""
SISTEMA DE GESTIÓN DE ROUTERS TEÓRICO
Proyecto escolar - Código modular y altamente comentado
"""

# CONFIGURACIÓN DE BASE DE DATOS (MODIFICAR SEGÚN NECESIDAD)
DB_NAME = "network_db.sqlite"

def conectar_db():
    return sqlite3.connect(DB_NAME)

def inicializar_db():
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS routers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT UNIQUE NOT NULL,
                            ip TEXT NOT NULL)''')
        conexion.commit()

# FUNCIÓN PARA AÑADIR UN ROUTER
def añadir_router(nombre, ip):
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO routers (nombre, ip) VALUES (?, ?)", (nombre, ip))
            conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False

# FUNCIÓN PARA ELIMINAR UN ROUTER
def eliminar_router(nombre):
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM routers WHERE nombre = ?", (nombre,))
        conexion.commit()
        return cursor.rowcount > 0

# INICIALIZAR BASE DE DATOS
inicializar_db()

# choripan
