from tkinter import *
from tkinter import messagebox
import sqlite3

#-----------------------------funciones-----------------------------------------------
def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE DATOS_USUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(10),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')
		messagebox.showinfo("BBDD","La base de datos fue creada con exito")
	except:
		messagebox.showwarning("¡Atención","La base de datos ya existe")	


def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")

	if(valor=="yes"):
		root.destroy()

def limpiarCampos():
	miNombre.set("")
	miId.set("")
	miApellido.set("")
	miDireccion.set("")
	miPass.set("")
	textoComentario.delete(1.0,END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	"""miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,'" + miNombre.get() +
			"','" + miPass.get() +
			"','" + miApellido.get() +
			"','" + miDireccion.get() +
			"','" + textoComentario.get("1.0",END) + "')")"""
	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END)
	miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)",(datos)) # Consultas Parametricas
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro insertado con éxito")

def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT *FROM DATOS_USUARIOS WHERE ID="+miId.get())
	elUsuario=miCursor.fetchall() #Devuelve un array de la consulta	

	for usario in elUsuario:
		miId.set(usario[0])
		miNombre.set(usario[1])
		miPass.set(usario[2])
		miApellido.set(usario[3])
		miDireccion.set(usario[4])
		textoComentario.insert(1.0,usario[5])
	miConexion.commit()


def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	"""miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+
		"',PASSWORD='" + miPass.get()+
		"',APELLIDO='" + miApellido.get()+
		"',DIRECCION='" + miDireccion.get()+
		"',COMENTARIOS='" + textoComentario.get("1.0",END)+
		"'WHERE ID="+ miId.get())"""
	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END)
	miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=?"+
		"WHERE ID="+miId.get(),(datos))
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro actualizado con éxito")


def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID="+miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro borrado con exito")

root=Tk()
#-----------------------Menu superior-----------------------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar Campos",command=limpiarCampos)


CRUDMenu=Menu(barraMenu,tearoff=0)
CRUDMenu.add_command(label="Crear",command=crear)
CRUDMenu.add_command(label="Leer",command=leer)
CRUDMenu.add_command(label="Actualizar",command=actualizar)
CRUDMenu.add_command(label="Borrar",command=eliminar)


ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de....")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)



#-----------------------------comienzo de campos--------------------------

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame,textvariable=miId)
cuadroID.grid(row=0,column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#-------------------------------------------comienza los label-----------------------

idLabel=Label(miFrame, text="Id: ")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame, text="Contraseña: ")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)


#------------------------------------Botones Inferiores---------------------

miFrame2=Frame(root)
miFrame2.pack()

botonInsertar=Button(miFrame2,text="Insertar",command=crear)
botonInsertar.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Seleccionar",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Borrar",command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

root.mainloop()
