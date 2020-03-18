nombre=input("nombre de la persona: ")

personas = {
    "carlos":24,
    "jelena":26,
    "julia":24,
    "daniel":25
}

print(personas["carlos"])
print("la edad de la persona es: ",personas.get(nombre,"no existe"))

personas["daniel"]=24
print(personas)

personas["julieta"] = 20
print(personas)

del personas["julieta"]
print(personas)


########### iteraciones de diccionarios
for llave in personas.keys():
    print(llave)

for valor in personas.values():
    print(valor)

for llave,valor in personas.items():
    print(llave,valor)

########### operador in 
print('daniel' in personas)
print('Veronica' in personas)

########### diccionary comprenhention
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)