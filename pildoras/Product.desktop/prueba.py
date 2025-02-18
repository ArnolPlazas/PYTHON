from tkinter import ttk
from tkinter import *
import glob, os
import cx_Oracle
import csv, operator
from datetime import date, datetime
from io import open


class archivo:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title('Control de planos')

        # creación del contenedor
        entorno = LabelFrame(self.ventana, text='Manejo de Registros')
        entorno.grid(row=0, column=0, columnspan=5, padx=50, pady=50)

        # mensaje del numero archivos
        Label(entorno, text='No Archivos: ').grid(row=1, column=0, padx=5, pady=10)
        self.cant_archivos = Label(entorno, text='XX', fg='blue')
        self.cant_archivos.grid(row=1, column=4, pady=10)

        # Boton para analizar la carpeta de planos
        ttk.Button(entorno, text='Analizar Carpeta', command=self.obtener_datos).grid(row=2, sticky=W + E, padx=5)

        # Boton para subir los datos
        ttk.Button(entorno, text='Subir Información').grid(row=3, sticky=W + E, padx=5)

        # Tabla
        self.tabla = ttk.Treeview(height=20, column=('TAMAÑO(KB)', 'LIENEAS', 'FECHA ACTUALIZACION'))
        self.tabla.grid(row=4, column=0, columnspan=4)
        self.tabla.heading('#0', text='ARCHIVO', anchor=CENTER)
        self.tabla.heading('#1', text='TAMAÑO(KB)', anchor=CENTER)
        self.tabla.heading('#2', text='LIENEAS', anchor=CENTER)
        self.tabla.heading('#3', text='FECHA ACTUALIZACION', anchor=CENTER)

    def obtener_datos(self):
        # limpiar la tabla
        registros = self.tabla.get_children()
        for e in registros:
            self.tabla.delete(e)

        # Consultar la informacion de los archivos
        consulta = self.consultar_datos
        print(consulta)
        # Llenar datos
        # for r in consulta:
        # self.tabla.insert('', 0, text = r[1], values = (r[2], r[3], r[4]))

    def consultar_datos(self):
        formato = "%d-%m-%y %I:%m %p"
        archivos_txt = glob.glob("PL_2019/*.txt")
        archivos_csv = glob.glob("PL_2019/*.csv")
        archivos = archivos_txt + archivos_csv
        nombre_archivos = []
        inf_archivos = []
        registro = []
        for e in archivos:
            nombre_archivos.append(e[8:])
        for e in nombre_archivos:
            registro = [e, float(os.path.getsize('PL_2019/' + e) / 1000), self.numero_lineas(e),
                        datetime.fromtimestamp(os.stat('PL_2019/' + e).st_mtime).strftime(formato)]
            inf_archivos.append(registro)
        return inf_archivos

    def numero_lineas(self, fichero):
        lineas_csv = 0
        if fichero.endswith(".txt") or fichero.endswith(".TXT"):
            return len(open('PL_2019/' + e, "r").readlines())
        else:
            try:
                with open(fichero) as csvarchivo:
                    entrada = csv.reader(csvarchivo)
                    for reg in entrada:
                        lineas_csv += 1
                return lineas_csv
            except FileNotFoundError:
                return 0


if __name__ == '__main__':
    ventana = Tk()
    archivo(ventana)
    ventana.mainloop()