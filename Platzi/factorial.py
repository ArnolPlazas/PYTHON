

def factorial(number):
    if number == 0:  # Caso base, para no generar un bucle infinito
        return 1
    
    return number * factorial(number -1) # Recursividad




if __name__ == "__main__":
    number = int (input('Escrbe un número: '))
    result = factorial(number)
    print(result)