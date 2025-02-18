from tkinter import *


root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
	opcionesEscogida=""

	if(playa.get()==1):
		opcionesEscogida+="playa "
	if(montagna.get()==1):
		opcionesEscogida+="montaña "
	if(turismoRural.get()==1):
		opcionesEscogida+="turismo rural "

	textoFinal.config(text=opcionesEscogida)

foto=PhotoImage(file="avion.png")
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="Elige destinos",width=50).pack()

Checkbutton(frame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Montaña",variable=montagna,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Turismo rural",variable=turismoRural,onvalue=1,offvalue=0,command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()