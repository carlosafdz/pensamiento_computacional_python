a = int(input("numero entero: "))
respuesta = 0


while respuesta**2 < a:
    respuesta += 1
    print(respuesta)

if respuesta**2 == a:
    print(f'la raiz cuadrada de {a} es {respuesta}')

else: 
    print(f'respuesta no tiene raiz cuadrada exacta')