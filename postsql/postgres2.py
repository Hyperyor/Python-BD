from pg import DB

def crearTabla(conn):

    conn.query("drop table if exists joseluis")
    conn.query("CREATE TABLE joseluis(fecha_lanzamiento varchar, titulo varchar, consola varchar, cantidad integer, precio float);")

def insertarDatos(conn):

    conn.insert('joseluis', fecha_lanzamiento = '2006-03-28', titulo ='God of War', consola = 'PS4', cantidad = 1000, precio = 45.00)
    conn.insert('joseluis', fecha_lanzamiento = '2006-04-05', titulo ='Minecraft', consola = 'PC', cantidad = 1000, precio = 20.00)
    conn.insert('joseluis', fecha_lanzamiento = '2006-04-06', titulo ='Monster Hunter', consola = 'PC', cantidad = 500, precio = 53.00)

def mostrarDatos(conn):

    q = conn.query('select * from joseluis')
    #print(q.getresult())

    for row in q.getresult():
        print(row)

def eliminarElemento(conn):

    conn.query("delete from joseluis where titulo='Monster Hunter'")

def conexionPygreSQL():

    #establecemos la conexion
    conn = DB(dbname="biblioteca", user="hyper", passwd="pass", host="127.0.0.1", port=5432)
    print("Database Connected....")

    #creamos la tabla, eliminandola antes del create si ya existe
    crearTabla(conn)

    print("Tabla creada")

    insertarDatos(conn)

    print("Compras realizadas por JoseLuis: ")
    mostrarDatos(conn)

    print("Vamos a vender Monster Hunter...")
    #eliminamos una fila
    eliminarElemento(conn)

    print("... hecho")

    print("JoseLuis ha vendido Monster Hunter por lo que su biblioteca queda así: ")
    mostrarDatos(conn)

    conn.commit()
    conn.close()