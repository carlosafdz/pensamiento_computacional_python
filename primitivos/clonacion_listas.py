a = [1,2,3,4,5,6,7]
b = a

print(id(a))
print(id(b), 'tiene la misma direccion de memoria que a por lo que es el mismo objeto')

c = list(a)
print(id(c),'ya tiene una direccion de memoria diferente por lo tanto es un objeto distinto')

d = a[::]
print(id(d),'otro metodo de clonar la lista para crear un objeto distinto')

