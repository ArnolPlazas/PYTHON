
"""
Un decoradores una función que recibe otra función y regresa una tercera función.

Para reconocer un decorador, puedes ver que tienes un arroba sobre la declaración de
 una función.

"""


def protected(func):
    def wrapper(password):
        if password == 'platzi':
            return func() # Ejecutar la función que decora
        else:
            print('La contraeña es incorrecta')

    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta.')

if __name__ == "__main__":
    password = str(input('ingresa tu contraeña: '))

    protected_func(password)