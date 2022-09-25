from asyncio.windows_events import NULL


def chequear_3_cifras(numero):
    """
    Funcion para revisar si el número tiene 3 cifras
    """
    return numero in range(100,1000)


cifras=chequear_3_cifras(1)
print(cifras)
cifras=chequear_3_cifras(323)
print(cifras)

suma = 50 + 75
cifras=chequear_3_cifras(suma)
print(cifras)


#Ahora con una lista

def hay_elemento_3(lista_numeros):
    """
    Funcion para revisar si el número tiene 3 cifras
    """
    for elemento in lista_numeros:
        if elemento in range(100,1000):
            return f'{elemento} {True}'
        else:
            pass
    return False

validar_lista = hay_elemento_3([2,99,55])
print(validar_lista)


def devoler_3_cifras(lista_numeros):
    """
    Funcion para revisar si el número tiene 3 cifras
    """
    devolver = []
    for elemento in lista_numeros:
        if elemento in range(100,1000):
            devolver.append(elemento)
        else:
            pass
    if len(devolver) == 0:
        return 'No se encontraron números de 3 cifras'
    else:
        return devolver

validar_lista = devoler_3_cifras([2,99,55])
print(validar_lista)
validar_lista = devoler_3_cifras([125,99,500])
print(validar_lista)
