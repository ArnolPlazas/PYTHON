from tkinter import *

root=Tk()
miFrame=Frame(root,width=500,height=400)
miFrame.pack()
miLabel1=Label(miFrame, text="Hola alumnos",fg="red",font=("Comic Sans MS",18))
miLabel1.place(x=100,y=200)#ubicar el label en una coordenada x,y

miImagen=PhotoImage(file="tux.png")#clase que permite rescatar y manipular imagenes
miLabel2=Label(miFrame,image=miImagen).place(x=300,y=200)
root.mainloop()