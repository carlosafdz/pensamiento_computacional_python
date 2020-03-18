a = list(range(0,100))
print(a,'una lista de 0 a 100')

double = [i * 2 for i in a]
print(double, 'una lista que multiplica todos los valores por 2')

pares = [i for i in a if i%2 == 0]
print(pares, 'una lista de todos los pares del 0 al 100')
