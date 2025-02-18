from tkinter import ttk
from tkinter import *
import sqlite3

class Product:

    db_name = 'database.db'

    def __init__(self,window):
        self.wind=window
        self.wind.title('Aplicación de productos')

        #creación del contenedor
        frame=LabelFrame(self.wind, text='Registra un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Entrada nombre
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.name=Entry(frame)  # guardar el dato en una propiedad de  la clase
        self.name.focus() # abre la aplicacion con el cursor en esta entrada
        self.name.grid(row = 1, column = 1 )

        #Entrada precio
        Label(frame, text='Precio: ').grid(row=2, column=0)
        self.price=Entry(frame)  # guardar el dato en una propiedad de  la clase
        self.price.grid(row = 2, column=1)

        #Boton para agregar producto
        ttk.Button(frame, text='Guardar Producto', command = self.agregar_producto).grid(row = 3, columnspan = 2, sticky = W + E)

        #Mensaje de salida
        self.mensaje=Label(text = '', fg= 'red' )
        self.mensaje.grid(row=3, column = 0, columnspan = 2, sticky= W + E)

        #Tabla
        self.tabla = ttk.Treeview(height = 10, column = 2)
        self.tabla.grid(row = 4, column = 0, columnspan = 2)
        self.tabla.heading('#0', text = 'Nombre', anchor=CENTER)
        self.tabla.heading('#1', text='Precio', anchor=CENTER)
        self.obtener_producto()

    def consultar (self, consulta, parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado=cursor.execute(consulta,parametros)
            conn.commit()
        return resultado

    def obtener_producto(self):
        #Limpiar la tabla
        registros=self.tabla.get_children() # obtener todos los datos de la tabla
        for e in registros:
            self.tabla.delete(e)
        #consultar los datos
        consulta = 'SELECT * FROM T_PRODUCTOS ORDER BY NOMBRE DESC'
        db_filas=self.consultar(consulta)

        #Llenar los datos
        for r in db_filas:
            self.tabla.insert('', 0, text = r[1], values = r[2])

    def validar(self):
        return len(self.name.get()) !=0 and len(self.price.get()) != 0 # retornar un true solo si se ingresa valores en precio y nombre

    def agregar_producto(self):
        if self.validar():
            consulta= 'INSERT INTO T_PRODUCTOS VALUES (NULL,?,?)'
            parametros = (self.name.get(), self.price.get())
            self.consultar(consulta, parametros)
            self.mensaje['text'] = 'Producto {} agragado corectamente'.format(self.name.get())
            self.name.delete(0, END)  # Limpiar los valores
            self. price.delete(0, END)
        else:
            self.mensaje['text'] = 'El nombre y el precio son requeridos'
        self.obtener_producto()

    def eliminar(self):

if __name__=='__main__':
    window=Tk()
    Product(window)
    window.mainloop()