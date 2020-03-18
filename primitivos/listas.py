lista = [1,2,3]
print(lista[0:2])

lista.append(4)
print(lista)

lista[0]='a'
print(lista)

lista.pop()
print(lista)


a=[1,2,3]
b=a
print(id(a))
print(id(b))

##########tener cuidado con lasreferencias a memoria
c = [a,b]
print(c)
a.append('se agrego en a por lo tanto en b tambien')
print(c)