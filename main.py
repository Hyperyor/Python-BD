
import sql3.conexion_mysqlite as sqlite
import postsql.postgres1 as p1
import postsql.postgres2 as p2

if __name__ == "__main__":
    eleccion = 0
    print("Bienvenido al programa de pruebas Bases de Datos en python.\n")
    print("A continuación se mostrarán los conectores disponibles: \n\n")
    print("1- MySQLite3 \n")
    print("2- PsycoPG2 (PostgreSQL) \n")
    print("3- PygreSQL (PostgreSQL) \n\n")

    while(int(eleccion) <  1 or int(eleccion) > 3):
        eleccion = input("Introduzca una opcion (1-3): ")
    

    if int(eleccion) == 1:

        print("Se procedera a realizar operaciones sobre la BD usando MySQLite3: \n\n")
        
        sqlite.conexionSQLite()
    
    else:
        
        if int(eleccion) == 2:

            print("Se procedera a realizar operaciones sobre la BD usando PsycoPG2: \n\n")
            p1.conexionPsycopg()

        else:

            print("Se procedera a realizar operaciones sobre la BD usando PygreSQL: \n\n")
            p2.conexionPygreSQL()

            
    
        
    

    
    
