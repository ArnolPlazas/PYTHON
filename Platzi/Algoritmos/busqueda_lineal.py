import random

def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    tamagno_de_lista = int(input('¿De que tamaño sera la lista? '))
    objetivo = int(input('¿Que número quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamagno_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')