miLista=["Maria","Marta","Pepe","Antonio"]

print(miLista[:])
print(miLista[2])
print(miLista[-4])
print(miLista[1:3])
print(miLista[:2])

miLista.append("Camila")
print(miLista[:])

miLista.insert(2,"Andrea")
print(miLista[:])

miLista.extend(["Pedro","Mario"])
print(miLista[:])

print(miLista.index("Antonio"))

milistados=[True,"Alfred",3.1416,17]
print(milistados)

print("Alfred" in milistados)

milistados.remove(True)
print(milistados[:])

miLista.pop()
print(miLista[:])

miLista3=miLista+milistados
print(miLista3[:])

miLista3=milistados*2
print(miLista3[:])