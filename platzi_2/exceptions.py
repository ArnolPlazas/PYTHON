try:
    divisor = int(input("Enter a number to divide by: "))
    dividend = 100 / divisor
    print(dividend)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
    print(e)
except ValueError as e:
    print("You must enter a number!")
    print(e)

# Imprimir la jerarquía comenzando desde la clase base Exception
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)


print_exception_hierarchy(Exception)