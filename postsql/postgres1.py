
#debe ser con python 3.5
import psycopg2


def creacionTabla(cur):

   cur.execute("drop table if exists joseluis")
   cur.execute("CREATE TABLE joseluis(fecha_lanzamiento varchar(50), titulo varchar(50), consola varchar(50), cantidad integer, precio float);")
   print("Table Created....")

def insertarDatos(cur):

   cur.execute("INSERT INTO joseluis (fecha_lanzamiento , titulo , consola , cantidad , precio) VALUES (%s, %s, %s, %s, %s)", ('2006-03-28', 'God of War', 'PS4', 1000, 45.00))
   cur.execute("INSERT INTO joseluis (fecha_lanzamiento , titulo , consola , cantidad , precio) VALUES (%s, %s, %s, %s, %s)", ('2006-04-05', 'Minecraft', 'PC', 1000, 20.00))
   cur.execute("INSERT INTO joseluis (fecha_lanzamiento , titulo , consola , cantidad , precio) VALUES (%s, %s, %s, %s, %s)", ('2006-04-06', 'Monster Hunter', 'PC', 500, 53.00))

def mostrarDatos(cur):

   cur.execute('SELECT * FROM joseluis ORDER BY precio')
   for row in cur.fetchall():
      print(row)
   
def eliminarElemento(cur, titulo):

   cur.execute('DELETE FROM joseluis WHERE titulo=%s', titulo)

def conexionPsycopg():

   #establecemos la conexion
   conn = psycopg2.connect(database="biblioteca", user="hyper", password="pass", host="127.0.0.1", port="5432")
   print("Database Connected....")

   cur = conn.cursor()

   #creamos la tabla
   creacionTabla(cur)

   #insertamos datos
   insertarDatos(cur)

   print("Compras realizadas por JoseLuis: ")
   mostrarDatos(cur)

   print("Vamos a vender Minecraft...")
   #eliminamos una fila
   t = ('Minecraft',)
   eliminarElemento(cur, t)

   print("... hecho")

   print("JoseLuis ha vendido Minecraft por lo que su biblioteca queda así: ")
   mostrarDatos(cur)


   conn.commit()
   conn.close()