"""
Los algoritmos son una serie de instrucciones que nos lleva a un resultado, por ejemplo que
tal si queremos saber si un número se encuentra en una lista.

Una forma es buscar un ítem tras otro, pero sí la lista es muy larga esta forma no es la mas
eficiente, una forma mas eficiente de solucionar éste problema es usar una búsqueda binaria.

Con el algoritmo de búsqueda binaria partimos de la lista ordenada, nosotros sabemos que hay
números mayores y menores que el numero que estamos buscando.

Seleccionamos un numero aleatorio para dividir la lista, puedes escoger cualquier número, en
éste caso sumamos el primer y el último indice de la lista, los sumamos y dividimos en dos
(por eso se llama binario), luego comparamos el número que esta en el indice, de esta manera
ya eliminamos la mitad de las opciones. Podemos continuar dividiendo la lista y comparando
actualizando los limites hasta que lleguemos al resultado 
"""


def binary_search(numbers, number_to_find, low, high):
    if low > high: # Si el numero no esta en la lista
        return False
    mid = int((low + high) / 2)
    if numbers[mid] == number_to_find: # si ya se encontro el numero en la lista
        return True
    elif numbers[mid] > number_to_find: # si el numero que esta en el indice mid es mayor al buscado
        return binary_search(numbers, number_to_find, low, mid - 1)
    else: # si el numero que esta en el indice mid es menor al buscado
        return binary_search(numbers, number_to_find, mid + 1, high)    






if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    number_to_find = int (input('Regresa un número: '))
    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El numero si esta en la lista')
    else:
        print('El numero no esta en la lista')