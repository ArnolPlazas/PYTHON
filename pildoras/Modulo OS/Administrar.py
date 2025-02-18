import os

def init():
    print("*******ADMINISTRAR ARCHIVO Y CARPETAS********")
    opcion=input("Seleccione una opción     c=crear    e=eliminar")
    if(opcion=="c"):
        ruta=input("Indique la ruta, si no indicas la ruta, la ruta sera la actual: ")
        if(ruta==""): ruta=os.getcwd()+"\\"
        #comprobar si la ruta existe
        if(os.path.isdir(ruta)):
            tipo=input("Indique el tipo  (a=archivo  c=carpeta): ")
            if(tipo=="a"):
                archivo=input("Indique el nombre del archivo: ")
                #Crear el archivo
                manejador=open(ruta+archivo,"w")
                manejador.close()
                print("Archivo ", archivo," creado con exito.")
            elif(tipo=="c"):
                

        
