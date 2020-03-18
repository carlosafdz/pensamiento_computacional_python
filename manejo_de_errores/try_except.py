def divide_elementos_de_lista(lista,divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print("divisor es 0, no podemos dividir 0/0")
        print(e)
        return lista


lista = list(range(10))
divisor  = 0

print(lista)
print(divide_elementos_de_lista(lista,divisor))
