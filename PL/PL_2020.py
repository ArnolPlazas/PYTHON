import glob,os
import cx_Oracle
import csv, operator
from datetime import date,datetime
from io import open


class archivo:       
        
    def cargar_datos(self):
        Registros = self.consultar_datos()
        con = cx_Oracle.connect('XCAPEX_XX', 'XXXXXXX', '192.168.44.4:1522/XCAPEX')
        cursor = con.cursor()

        for r in Registros:
            r.append(len(Registros))
            cursor.execute("INSERT INTO T_CTRL_PLANOS VALUES (:1,:2,:3,:4,:5,SYSDATE)",r)

        con.commit()    
        cursor.close()
        con.close()
        

    def consultar_datos(self):
        formato = "%d-%m-%y %I:%m %p"
        archivos_txt=glob.glob("PL_2020/*.txt")
        archivos_csv=glob.glob("PL_2020/*.csv")
        archivos=archivos_txt+archivos_csv
        nombre_archivos=[]
        inf_archivos=[]
        registro=[]
        for e in archivos:
            nombre_archivos.append(e[8:])
            
        for e in nombre_archivos:
            registro=[e,float(os.path.getsize('PL_2020/'+e)/1000),self.numero_lineas(e),datetime.fromtimestamp(os.stat('PL_2020/'+e).st_mtime).strftime(formato)]
            inf_archivos.append(registro)
        return inf_archivos

    def numero_lineas(self, fichero):
        lineas_csv=0
        if fichero.endswith(".txt") or fichero.endswith(".TXT") :
            return len(open('PL_2020/'+fichero,"r").readlines())
        else:    
            with open('PL_2020/'+fichero, encoding= "Latin-1" ) as csvarchivo:
                entrada = csv.reader(csvarchivo)
                for reg in entrada:
                    lineas_csv+=1
        return lineas_csv

ejecucion = archivo()
ejecucion.cargar_datos()

