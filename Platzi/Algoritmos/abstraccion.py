"""
Abastracción

    Enforcarse en la información relevante

    Separar la información central de los detalles secundarios

    Utilizar variables y métodos (privados o publicos)

"""

class Lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabon')
    
    def _lavar(self):
        print('Lavando ropa')

    def _centrifugar(self):
        print('Centrifugando ropa')

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()