def applicar(num):
    operaciones=[abs,float]
    resultados=[]
    for operacion in operaciones:
        resultados.append(operacion(num))
    return resultados

print(applicar(-2))