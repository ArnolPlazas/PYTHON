
import random

def ordenamiento_por_insercion(lista):
    lista_ordenada = []
    valor_actual = lista[0]

    for l in lista:
        if l[i + 1] < valor_actual:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]







if __name__ == "__main__":
    
    tamagno_de_lista = int(input('¿De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamagno_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)