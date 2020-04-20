class Estudiante(): 
    def __init__(self,nombre_r,edad_r): 
        self.nombre = nombre_r 
        self.edad = edad_r 

    def hola(self): 
	    return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad)

e1 = Estudiante("Arturo", 21) 
e2 = Estudiante("Arnol", 29) 
print (e1.hola())