entero = int(input("numero: "))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - entero) >= epsilon and respuesta <= entero:
    respuesta = respuesta + paso
    print(respuesta)

if abs(respuesta**2 - entero) >= epsilon:
    print('no se encontro la raiz cuadrada del objetivo')

else:
    print(f'la raiz cuadrada de {entero} es {respuesta}')  

