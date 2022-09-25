"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def doble_cero(*args):
    cero = False
    ceros = 0
    for val in args:
        if val == 0 and not cero:
            cero = True
            ceros +=1
        elif val == 0 and cero:
            ceros +=1
            if ceros == 3:   
                return cero
            else:
                pass
        else:
            cero = False
    return cero

print(doble_cero(5,6,1,0,0,9,3,5))
print(doble_cero(6,0,5,1,0,3,0,1))

 

"""
SOLUCIÓN DEL PROFESOR
"""

def doble_cero(*args):
    contador = 0
    for num in args:
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador+=1
    return False

print(doble_cero(5,6,1,0,0,9,3,5))
print(doble_cero(6,0,5,1,0,3,0,1))