import sys

def factorial(a):
    """
        calcula el factorial de n

        n es entero 
        n > 0
        regresa n!
    """
    print(a)
    if a == 0:
        return 0
    elif a == 1:
        return 1
    return a * factorial(a-1)

sys.setrecursionlimit(2000) #modifica el limite de recursion 
print(sys.getrecursionlimit()) #imprime el limite de recursion establecido

valor = int(input('introducir valor: '))
print(factorial(valor))