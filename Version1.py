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
                            ip TEXT NOT NULL,
                            solicitud TEXT)''')
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

# FUNCIÓN PARA MODIFICAR DATOS DE UN ROUTER
def modificar_router(nombre_actual, nuevo_nombre, nueva_ip):
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE routers SET nombre = ?, ip = ? WHERE nombre = ?", (nuevo_nombre, nueva_ip, nombre_actual))
        conexion.commit()
        return cursor.rowcount > 0

# FUNCIÓN PARA MODIFICAR SOLICITUD DE UN ROUTER
def modificar_solicitud_router(nombre_actual, nueva_solicitud):
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE routers SET solicitud = ? WHERE nombre = ?", (nueva_solicitud, nombre_actual))
        conexion.commit()
        return cursor.rowcount > 0

# FUNCIÓN PARA ENVIAR SOLICITUD DE REPARACIÓN Y REVISIÓN
def enviar_solicitud_reparacion_revision(nombre_router, solicitud):
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE routers SET solicitud = ? WHERE nombre = ?", (solicitud, nombre_router))
        conexion.commit()
        return cursor.rowcount > 0

# INICIALIZAR BASE DE DATOS
inicializar_db()


# INICIALIZAR BASE DE DATOS
inicializar_db()

