def todos_positivos(lista_numeros):
    """
    Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de
    una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con
    valores positivos y negativos.
    No invoques la función, solo es necesario definirla.
    """
    for elemento in lista_numeros:
        if elemento < 0:
            return False
        else:
            pass
    return True

lista_numeros = [132465,-11,12,443,-2121]



def suma_menores(lista_numeros):
    """
    Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando
    sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
    """
    mi_suma=0
    for elemento in lista_numeros:
        if elemento in range(1,1000):
            mi_suma +=elemento
        else:
            pass
    return mi_suma

lista_numeros = [132465,-11,12,443,-2121]




def cantidad_pares(lista_numeros):
    """
    Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una 
    lista (lista_numeros), y devuelva el resultado de dicha cuenta.
    """
    mi_suma=0
    for elemento in lista_numeros:
        if elemento%2 == 0:
            mi_suma +=1
        else:
            pass
    return mi_suma

lista_numeros = [20,50,12,443,33]