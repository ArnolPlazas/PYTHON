from tkinter import *
from tkinter import messagebox
root=Tk()

def infoAdicional():
	messagebox.showinfo("Procesador de Arnol","Procesador DE texto 2018")

def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU")	

def salirAplicacion():
	valor=messagebox.askquestion("Salir","Salir de la aplicación")

	if valor=="yes":
		root.destroy()

def salirAplicacion2():
	valor=messagebox.askokcancel("Salir","Salir de la aplicación")

	if valor==True:
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar","No ces posible cerrar. Documento Bloqueado")
	if valor==True:
		root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=500,height=500)

archivoMenu=Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)


archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramienta=Menu(barraMenu)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()