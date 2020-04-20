"""
El ordenamiento por mezcla es un algoritmo de divide y conquist. Primero
divide una lista en partes iguales hasta que que queden sublistas de 1 o 0
elementos. Luego las recombina en forma ordenada

John von Numan
"""


import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[: medio]
        derecha = lista[medio :]
        print(izquierda, '*' * 5, derecha )

        # Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador opara la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1   
    
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)
    return lista

if __name__ == "__main__":
    
    tamagno_de_lista = int(input('¿De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamagno_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
