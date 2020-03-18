
def primera_letra(lista_palabras):
    primera_letra=[]

    for palabra in lista_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, f'{palabra} esta vacio'

        primera_letra.append(palabra[0])

    return primera_letra

lista = ['carlos','Jelena', 'Julia','Daniel','',2]

print(primera_letra(lista))