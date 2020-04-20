# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 08:50:04 2019

@author: afplazasac
"""
from io import open


def leerArchivoDGC():
    archivo_texto=open("PL_DGC.txt","r")
    lineas_texto=archivo_texto.readlines()#Leer un archivo linea a linea y guardar en una list
    archivo_texto.close()
    return lineas_texto[15:] #elementos de la lista


def crearArchivoDGC():
    info = leerArchivoDGC()
    info_final=[]
    for i in info:
        if i[:6] == '|1167|' :
            pipe = i.count('|')
            if pipe == 54:
                g = [j for j, n in enumerate(i) if n == '|']
                change_list= list(i)
                change_list[g[6]] = '-'
                change_string = ''.join(change_list)
                info_final.append(change_string)                   
            else:
                info_final.append(i)
    archivo_texto = open('PL_DGC2.txt','w')
    archivo_texto.writelines(info_final)
    archivo_texto.close

def leerArchivoRECESH():
    archivo_texto=open("PL_RECESH.txt","r")
    lineas_texto=archivo_texto.readlines()#Leer un archivo linea a linea y guardar en una list
    archivo_texto.close()
    return lineas_texto[10:] #elementos de la lista


def crearArchivoRECESH():
    info = leerArchivoRECESH()
    info_final=[]
    for i in info:
        if i[:6] == '|   NI' :
            info_final.append(i)
    archivo_texto = open('PL_RECESH2.txt','w')
    archivo_texto.writelines(info_final)
    archivo_texto.close
        


def run():
    crearArchivoDGC()
    crearArchivoRECESH()
    

if __name__ == '__main__':
    run()