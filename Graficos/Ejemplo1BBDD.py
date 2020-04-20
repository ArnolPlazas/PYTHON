import sqlite3

miConexion=sqlite3.connect("PrimeraBase")#crear y abrir la BD

micursor=miConexion.cursor()#crear el cursor o puntero
#micursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")

#micursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON',15,'DEPORTES')")

#variosProductos=[#creacion de una lista para insertar varios registros
#	("Camisa",10,"Deportes"),
#	("Jarrón",10,"Deportes"),
#	("Camión",10,"Deportes")

#]

#micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)

micursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=micursor.fetchall()#obtener todos los valores de una tabal BD en una lista


for producto in variosProductos:
	print("Nombre del artículo: ",producto[0]," Sección: ",producto[2])

miConexion.commit()#confirmar el cambio de la BD

miConexion.close() #cerrar la BD