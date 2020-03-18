def multiplocar2(n):
    return n*2

def sumar2(n):
    return n+2

def aplicarfun(f,numeros):
    resultados=[]
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados

num=[1,2,3]

print(aplicarfun(multiplocar2,num))
print(aplicarfun(sumar2,num))
