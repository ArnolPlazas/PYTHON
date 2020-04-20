from io import open

#archivo_texto=open("archivo.txt","w") # abrir en memoria y crear el archivo nombre y tipo de archivo y w:escritura

#frase="Estupendo dia para estudiar Phyton\n Martes"
#archivo_texto.write(frase) #metodo write para escribir algo dentro del archivo
#archivo_texto.close()#cerrrar el archivo 

#archivo_texto=open("archivo.txt","r")#abrir en memoria, r:modo lectura
#texto=archivo_texto.read() #guardar en una variable la lectura del archivo
#archivo_texto.close()
#print(texto)

#archivo_texto=open("archivo.txt","r")
#lineas_texto=archivo_texto.readlines()#Leer un archivo linea a linea y guardar en una list
#archivo_texto.close()
#print(lineas_texto[0])#imprimir el segundo elemento de la lista

#archivo_texto=open("archivo.txt","a")# abrir el archivo en modo append(añadir)
#archivo_texto.write("\n siempre es una buena ocacion para estudiar Python")
#archivo_texto.close()

archivo_texto=open("archivo.txt","r+")#lectura y escritura
#print(archivo_texto.read())
#archivo_texto.seek(0)
#print(archivo_texto.read())
#archivo_texto.seek(0)

#archivo_texto.seek(len(archivo_texto.read())/2)
#print(archivo_texto.read())

#archivo_texto.write("HOLA MUNDO")

lista_texto=archivo_texto.readlines()
lista_texto[0]="Texto desde el exterior\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()
