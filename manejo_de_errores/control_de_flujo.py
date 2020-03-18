
# python usa el principio "mas facil pedir perdon que permiso" EAFP

def buscar_pais(paises,pais):
    """ 
    paises en un diccionario
    pais es una llave
    """
    try: # se intenta ejectar la sentencia o centencias declaradas
        return paises[pais]
    except KeyError: # se ejecuta si existe un error
        return None
    else: 
        print("no hubo ningun error") #se ejecuta si no hay un error
    finally:
        print("siempre se va a ejecutar") #se ejecuta independientemente de que exista o no un error
    