a = 4
b = 3
r = b
while a > 1:
    a = a - 1
    b2 = b
    r2 = 0
    while b2 > 0:
        r2 = r2 + r
        b2 = b2 - 1
    r = r2
print(r)
