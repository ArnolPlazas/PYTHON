import pickle

class Vehiculos():
	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",
			self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenado: ",self.frena)

coche1=Vehiculos("Mazda","MX5")
coche2=Vehiculos("Tesla","X")
coche3=Vehiculos("Mazda","Megane")
coches=[coche1,coche2,coche3]
fichero=open("coches","wb")
pickle.dump(coches,fichero)
fichero.close()
del(fichero)

fichero_apertura=open("coches","rb")
coches=pickle.load(fichero_apertura)
fichero_apertura.close()
for c in coches:
	print(c.estado())