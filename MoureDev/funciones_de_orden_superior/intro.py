
# funcion como argumento
def apply_func(func, x):
    return func(x)

print(apply_func(len, "Arnol Plazas"))

# retorno de funcion

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier = apply_multiplier
print(type(multiplier))

multiplier = apply_multiplier(2)
print(multiplier(5))

print(apply_multiplier(3)(2))

# Sistema
numbers = [1, 2, 3, 4, 5]

## map()
def apply_double(n):
    return n * 2

print(map(apply_double, numbers))
print(type(map(apply_double, numbers)))
print(list(map(apply_double, numbers)))

## filter()
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numbers)))

## sorted()
print(sorted(numbers))
print(sorted(numbers, reverse= True))
print(sorted(numbers, key= lambda x: -x))

## reduce
from functools import reduce


def sum(x, y):
    return x + y

print(reduce(sum, numbers))








