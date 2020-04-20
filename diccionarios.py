midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres"}
print(midiccionario["Francia"])
print(midiccionario)

midiccionario["Italia"]="Roma"
print(midiccionario)

midiccionario["Colombia"]="Medellin"
print(midiccionario)
midiccionario["Colombia"]="Bogota"
print(midiccionario)

del midiccionario["Reino Unido"]
print(midiccionario)

midiccionario2={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
print(midiccionario2)

lista=["España","Francia","Reino Unido","Alemania"]
midiccionario3={lista[0]:"Madrid",lista[1]:"Paris",lista[2]:"Londres",lista[3]:"Berlin"}
print(midiccionario3)
print(midiccionario3["Francia"])
print(midiccionario3[lista[2]])


dic={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1993,1996,1997,1998]}
print(dic["Anillos"])

dic2={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(dic2["Anillos"])

print(dic.keys())
print(dic.values())
print(len(dic))
