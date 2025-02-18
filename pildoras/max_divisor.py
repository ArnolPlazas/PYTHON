def max_divisor(n):
    maximo_actual=0
    i=1
    while i<n:
        if n%i==0:
            maximo_actual=i
        i+=1
    return maximo_actual

print(max_divisor(10))
