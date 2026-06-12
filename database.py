import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect('asistencia.db')
    cursor = conexion.cursor()

    # Tabla de usuarios (para el login)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')

    # Tabla de trabajadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trabajadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            dni TEXT NOT NULL,
            cargo TEXT NOT NULL,
            obra TEXT NOT NULL
        )
    ''')

    # Agregar columna cargo si no existe
    try:
        cursor.execute('ALTER TABLE trabajadores ADD COLUMN cargo TEXT')
    except:
        pass

    # Tabla de asistencia
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asistencia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trabajador_id INTEGER NOT NULL,
            hora_ingreso TEXT,
            hora_salida TEXT,
            fecha TEXT,
            obra TEXT,
            foto_ingreso TEXT,        -- NUEVO: foto tomada al registrar entrada
            ubicacion_ingreso TEXT,   -- NUEVO: coordenadas GPS al registrar entrada
            foto_salida TEXT,         -- NUEVO: foto tomada al registrar salida
            ubicacion_salida TEXT     -- NUEVO: coordenadas GPS al registrar salida
        )
    ''')

    # NUEVO: agregar columnas a base de datos existente sin borrar datos
    try:
        cursor.execute('ALTER TABLE asistencia ADD COLUMN foto_ingreso TEXT')
    except:
        pass
    try:
        cursor.execute('ALTER TABLE asistencia ADD COLUMN ubicacion_ingreso TEXT')
    except:
        pass
    try:
        cursor.execute('ALTER TABLE asistencia ADD COLUMN foto_salida TEXT')
    except:
        pass
    try:
        cursor.execute('ALTER TABLE asistencia ADD COLUMN ubicacion_salida TEXT')
    except:
        pass

    # Crear usuario admin por defecto
    cursor.execute('''
        INSERT OR IGNORE INTO usuarios (id, usuario, contrasena)
        VALUES (1, 'admin', '1234')
    ''')

    conexion.commit()
    conexion.close()
    print('Base de datos creada correctamente')

crear_base_datos()