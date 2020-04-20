"""
Complejidad algoritmica

    Complejidad temporal (cauanto tarda el algoritmo en realizar una tarea)
    complejidad espacial (el cosumo del algoritmo en terminos de memoria)
    Se define como T(n)

    Complejidad temporal
        Cronometrar el tiempo el que acurre un algoritmo
        Contar los pasos con una medida abstracta de operación
        Contar los pasos conforme nos aproximamos al infinito (Mejor forma)

"""
import time 

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)


if __name__ == "__main__":
    n = 900

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
