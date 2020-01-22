import sqlite3 


def creacionTabla(c):

    c.execute('''drop table if exists joseluis''') # si existe la destruimos
    c.execute('''CREATE TABLE joseluis
                    (fecha_lanzamiento text, titulo text, consola text, qty integer, price real)''')

def insercionDatos(c):

# Insertamos varios campos a la vez
    compras = [('2006-03-28', 'God of War', 'PS4', 1000, 45.00),
                ('2006-04-05', 'Minecraft', 'PC', 1000, 20.00),
                ('2006-04-06', 'Monster Hunter', 'PC', 500, 53.00),
                ]
    c.executemany('INSERT INTO joseluis VALUES (?,?,?,?,?)', compras)

def mostrarDatos(c):

    for row in c.execute('SELECT * FROM joseluis ORDER BY price'):
        print (row)

def eliminarElemento(c, titulo):

    c.execute('DELETE FROM joseluis WHERE titulo=?', titulo)

def conexionSQLite():

    conn = sqlite3.connect('example.db')

    c = conn.cursor()

    #try:
        # Creamos la tabla
    #    c.execute('''CREATE TABLE joseluis
    #                (fecha_lanzamiento text, titulo text, consola text, qty integer, price real)''')
    #except:
    #    print("tablas ya creadas")
    #    c.execute('DELETE FROM joseluis')

    creacionTabla(c)

    insercionDatos(c)
    

    #mostramos todos los datos
    print("Compras realizadas por JoseLuis: ")
    mostrarDatos(c)

    print("Vamos a vender God of War...")
    #eliminamos una fila
    t = ('God of War',)
    eliminarElemento(c, t)

    print("... hecho")

    print("JoseLuis ha vendido God of War por lo que su biblioteca queda así: ")
    mostrarDatos(c)

    # Guardamos los datos
    conn.commit()

    # Cerramos la conexion
    conn.close()
