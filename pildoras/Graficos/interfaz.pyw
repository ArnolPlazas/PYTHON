from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0,column=1) #crea una grilla (fila,columna)
cuadroNombre.config(fg="red",justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1)
cuadroPass.config(show="*")# remplazar lo escrito por un caracter

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1) 

textoComentario=Text(miFrame,width=16,height=15)
textoComentario.grid(row=4,column=1,padx=10,pady=10)

scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsw")

textoComentario.config(yscrollcommand=scrollVert.set)

  
#padding: es la distancia de un elemento al limite del contenedor padre
#padx y pady
# sticky=n,ne,e,se,s,sw,w,nw aliniar el texto(puntos cardinales)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10) 

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10) 

ApellidoLabel=Label(miFrame, text="Apellido: ")
ApellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10) 

DireccionLabel=Label(miFrame, text="Dirección: ")
DireccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10) 

CometariosLabel=Label(miFrame, text="Comentarios: ")
CometariosLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10) 


def codigoBoton():
	minombre.set("Arnol")

botonEnvio=Button(raiz, text="Enviar",command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()
