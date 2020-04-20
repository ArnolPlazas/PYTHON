import pickle

class Persona:

	def __init__(self,nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre de ",self.nombre)

	def __str__(self): #convertir en cadena de texto la info de un objeto
		return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
	personas=[]

	def __int__(self):
		ListaDePersonas=open("ficheroExterno","ab+")# abrir para agregar info binaria
		ListaDePersonas.seek(0)
		
		try: #Excepción para cuando no haya que cargar
			self.personas=pickle.load(ListaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero está vacío")
		finally:
			ListaDePersonas.close()
			del(ListaDePersonas)	
	
	def agregarPerdonas(self,p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)
	
	def guardarPersonasEnFicheroExterno(self):
		ListaDePersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas,ListaDePersonas)
		ListaDePersonas.close
		del(ListaDePersonas)

	def mostrarFicheroExterno(self):
		print("La información del fichero externo es: ")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()
persona=Persona("Camilo","Maculino",29)
miLista.agregarPerdonas(persona)
miLista.mostrarFicheroExterno()


# p=Persona("Antonio","Maculino",39)
# miLista.agregarPerdonas(p)
# p=Persona("Ana","Femenino",19)
# miLista.agregarPerdonas(p)

#miLista.mostrarPersonas()