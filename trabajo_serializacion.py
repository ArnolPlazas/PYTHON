import pickle

#Creacion del fichero cifrado en binario

#lista_nombres=["Pedro","Ana","Maria","Isabela"]
#fichero_binario=open("lista_nombres","wb") #wb: escritura binaria
#pickle.dump(lista_nombres,fichero_binario)#volcar la info de lista_nombre a fichero_bianrio
#fichero_binario.close()#cerrar el archivo
#del(fichero_binario)#Eliminar el archivo en memoria

#Lectura del fichero cifrado en binario

fichero=open("lista_nombres","rb")
lista=pickle.load(fichero)
print(lista)
