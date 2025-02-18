from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1) #crea una grilla (fila,columna)
cuadroNombre.config(fg="red",justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1)
cuadroPass.config(show="*")# remplazar lo escrito por un caracter

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1) 
  
#padding: es la distancia de un elemento al limite del contenedor padre
#padx y pady
# sticky=n,ne,e,se,s,sw,w,nw aliniar el texto(puntos cardinales)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10) 

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10) 

ApellidoLabel=Label(miFrame, text="Apellido: ")
ApellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10) 

DireccionLabel=Label(miFrame, text="Dirección de la casa: ")
DireccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10) 


raiz.mainloop()
