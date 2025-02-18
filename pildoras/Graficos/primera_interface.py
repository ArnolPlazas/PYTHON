from tkinter import *

raiz=Tk() #intanciar 
raiz.title("Ventana de prueba")
raiz.resizable(1,1)#ancho,alto no permite dedimencionar (0,0) (false,false)
raiz.iconbitmap("Bitcoin.ico")#icono de la ventana debe ser .ico
raiz.geometry("650x350")#definir el ancho y alto de la ventana
raiz.config(bg="blue")
raiz.config(relief="groove") #tipo de borde
raiz.config(bd=18)
raiz.config(cursor="hand2")#tipo de cursor

miFrame=Frame()
#miFrame.pack(side="right",anchor="n")#Empaquetar el frame dentro de la raiz side->anclado
miFrame.pack(fill="y", expand="true") #miFrame.pack(fill="x")   miFrame.pack(fill="both", expand="true")
miFrame.config(bg="red")
miFrame.config(width="600",height="350")
miFrame.config(bd=10)#grozor del borde
miFrame.config(relief="ridge") #tipo de borde
miFrame.config(cursor="pirate")#tipo de cursor

raiz.mainloop() #bocle infinito. (continua ejecución)

