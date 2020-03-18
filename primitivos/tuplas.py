tupla = ()

print(type(tupla))
tupla=(1,'dos', True)

print(tupla[2])


#sumas de tuplas
tupla=(1,)
otra_tupla=(2,3,4)

print(tupla+otra_tupla)

x,y,z = otra_tupla

def coordenadas():
    return(5,6)

coordenada=coordenadas()
x,y = coordenadas()

print(coordenada)
print(x,y)
