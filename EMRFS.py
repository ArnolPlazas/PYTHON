#coding: utf-8
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import cx_Oracle
#-------------------------------------VARIABLES----------------------------


#----------------------FUNCIONES-------------------------------------

#----------------------FUNCIONES DE BASE DE DATOS-------------------

def Buscar_Pedido():
    con = cx_Oracle.connect('CAPEX_19', 'BEMORE19', '192.168.44.4:1522/CAPEX')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM T_SEGUIMIENTO_EMRFS WHERE PEDIDO="+pedido.get())
    historiaPedidos=cursor.fetchall() #Devuelve un array de la consulta	
    for item in historiaPedidos:
        cuadroSeguimiento.insert('','end',values=item)
        print(item)
    cursor.close()
    con.close()
    
def Agregar_Seguimiento():
    pass

def Agregar_Resposable():
    pass

def Actualizar_Responsable():
    pass    


#----------------------CONSTRUCCION DE LA VISTA-------------------------------------
root=Tk()
miFrame=Frame(root)
miFrame.pack()

pedido=StringVar()
pedidoLabel=Label(miFrame, text="Pedido: ")
pedidoLabel.grid(row=0,column=0,sticky="e")

cuadroPedido=Entry(miFrame,textvariable=pedido)
cuadroPedido.grid(row=0,column=1)

botonLeer=Button(miFrame,text="Consultar",command=Buscar_Pedido)
botonLeer.grid(row=0,column=1,sticky="e",padx=10,pady=10,columnspan=3)

cuadroSeguimiento=ttk.Treeview(miFrame,columns=('COMENTARIO','TIPO','FECHA'))


cuadroSeguimiento.heading('#0',text='PEDIDO')
cuadroSeguimiento.heading('#1',text='COMENTARIO')
cuadroSeguimiento.heading('#2',text='TIPO')
cuadroSeguimiento.heading('#3',text='FECHA')

cuadroSeguimiento.column('#0', width=100,stretch=tk.YES)
cuadroSeguimiento.column('#1', width=700,stretch=tk.YES)
cuadroSeguimiento.column('#2', width=100,stretch=tk.YES)
cuadroSeguimiento.column('#3', width=100,stretch=tk.YES)
cuadroSeguimiento.grid(row=2,columnspan=2)
root.mainloop()
