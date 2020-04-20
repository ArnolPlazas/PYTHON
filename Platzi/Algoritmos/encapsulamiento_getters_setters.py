"""

Encapsulamiento

    Permite agrupar datos y su comportamiento.
    Controla el acceso a dichos datos.
    Previene modificaciones no autorizadas.

"""

class CasillaDeVotacion:
    def __init__(self, identificador, region):
        self._indentificador = identificador
        self._region = region
        self._pais = None

    @property
    def pais(self):  # metodo getter
        return self._pais

    @pais.setter # metodo setter
    def pais(self, pais):
        if pais in self._region:
            self._pais = pais
        else:
             print(f'El pais {pais} no es valida en la region {self._region}')


casilla = CasillaDeVotacion(123, ['Colombia', 'Venezuela', 'Peru'])
print(casilla.pais)
casilla.pais = 'Colombia'
print(casilla.pais)
casilla.pais = 'Mexico'
print(casilla.pais)

