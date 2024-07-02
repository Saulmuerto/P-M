import sqlite3
database = 'BaseP&M.db'

conn = sqlite3.connect(database, check_same_thread=False)
cursor = conn.cursor()
def registro(nombre, apellido, correo, ocupasion, contrasenia,):
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL,
        Correo TEXT NOT NULL,
        Ocupacion TEXT NOT NULL,
        Contrasenia TEXT NOT NULL
    )''')
    
    cursor.execute('''
        INSERT INTO usuario (Nombre, Apellido, Correo, Ocupacion, Contrasenia)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, apellido, correo, ocupasion, contrasenia))
    user = cursor.fetchone()
    conn.commit()
    return user 
