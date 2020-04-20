import sqlite3

miConexion=sqlite3.connect("GestionProductos")#crear y abrir la BD

micursor=miConexion.cursor()#crear el cursor o puntero



# micursor.execute('''
# 	CREATE TABLE PRODUCTOS (
# 	ID INTEGER PRIMARY KEY AUTOINCREMENT,
# 	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
# 	PRECIO INTEGER,
# 	SECCION VARCHAR (20))
# 	''')
# productos=[
# 	("pelota",20,"jugetería"),
# 	("pantalón",15,"confección"),
# 	("destornillador",25,"ferretería"),
# 	("jarrón",45,"cerámica"),
# ]
# micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",	productos)



# micursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección' ")
# productos=micursor.fetchall()
# print(productos)

micursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota' ")

miConexion.commit()#confirmar el cambio de la BD

miConexion.close() #cerrar la BD