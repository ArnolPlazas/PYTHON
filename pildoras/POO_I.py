class Coche():
	def __init__(self):	#Constructor de la clase Coche
		self.__largoChaisis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos		
		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()
		if(self.__enmarcha and chequeo):#Si el enmarcha y chequeo es igual a true
			return "El coche está en marcha"
		elif(self.__enmarcha and chequeo==False):
			return "Algo salio mal en el chequeo. No se puede arrancar"
		else:
			return "El coche esta parado"

	def estado(self):
		print("El conche tiene ", self.__ruedas," ruedas.Un ancho de ", self.__anchoChasis,"y un largo de ", self.__largoChaisis)

	def __chequeo_interno(self):
		print("Realizando chequeo interno")
		self.gasolina="OK"
		self.aceite="mal"
		self.puertas="cerradas"
		if(self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="cerradas"):
			return True
		else:
			return False		

miCoche=Coche() #Instanciar una clase
#print("El largo del coche es: ",miCoche.largoChaisis)# Acceder a las propiedades
#print("El coche tiene: ",miCoche.ruedas, " ruedas.")
print(miCoche.arrancar(True))#Llamar al metodo arrancar(comportamiento)
miCoche.estado()

print("------------- A continuación creamos el segundo objeto---------------")
miCoche2=Coche()
#print("El largo del coche es: ",miCoche2.largoChaisis)# Acceder a las propiedades
#print("El coche tiene: ",miCoche2.ruedas, " ruedas.")
print(miCoche2.arrancar(False))
miCoche2.estado()