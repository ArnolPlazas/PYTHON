import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo)

if __name__ == "__main__":
    tamagno_de_lista = int(input('¿De que tamaño sera la lista? '))
    objetivo = int(input('¿Que número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamagno_de_lista)])


    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')