import re

cadena="Vamos a aprender expresiones regulares en Python.Python es un lenguaje sencillo"

texto="aprender"
textoBuscar="Python"

'''if re.search(texto,cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")'''

texto_encontrado=re.search(texto,cadena)

print(texto_encontrado.start()) # Returna la posicion inicial del texto buscado
print(texto_encontrado.end()) # Returna la posicion final del texto buscado
print(texto_encontrado.span()) # Returna una tupla con la  posición inicial y la final

print(re.findall(textoBuscar,cadena)) # Deveulve una lista con n veces la palabra que se quiere buscar 
print(len(re.findall(textoBuscar,cadena))) # n veces que aparece la palabra