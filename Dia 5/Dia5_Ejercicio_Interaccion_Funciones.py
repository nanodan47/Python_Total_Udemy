"""
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:
"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:
"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:
"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
"""
from random import randint
from random import choice

def lanzar_dados():
    """
    Función que simula el lanzamiento de dos dados
    @@return:
    numero1: valor entre 1 y 6
    numero2: valor entre 1 y 6
    """
    lista_dado2 = [1,2,3,4,5,6]
    dado1 = randint(1,6)
    dado2 = choice(lista_dado2)
    return dado1,dado2

def evaluar_jugada(num1,num2):
    """
    Función que evalua la jugada según estos criterios
    Si la suma es menor o igual a 6:
    "La suma de tus dados es {suma_dados}. Lamentable"

    Si la suma es mayor a 6 y menor a 10:
    "La suma de tus dados es {suma_dados}. Tienes buenas chances"

    Si la suma es mayor o igual a 10:
    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

    @@return
    cadena con respuesta dependiend de suma
    """
    suma_dados = num1+num2
    respuesta = ''
    if suma_dados < 7:
        respuesta = f'La suma de tus dados es {suma_dados}. Lamentable'
    elif  6 < suma_dados < 10:
         respuesta = f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    else:
        respuesta = f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'
    return respuesta

dado1,dado2=lanzar_dados()
print(evaluar_jugada(dado1,dado2))





"""
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), 
y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. 
El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, 
y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
"""
lista_numeros = [1,2,15,7,2]
def reducir_lista (lista):
    mi_set = set(lista)
    mi_set.remove(max(mi_set))
    return list(mi_set)


def promedio(lista):
    return sum(lista)/len(lista)

print(promedio(reducir_lista(lista_numeros)))


"""
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). 
Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. 
El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

*Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
*Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
"""

def lanzar_moneda():
    coin = ['Cara','Cruz']
    lanzamiento = choice(coin)
    return lanzamiento

lista_numeros = [n for n in range(1,10)]
def probar_suerte(moneda,lista):
    mi_lista = []
    match moneda:
        case 'Cara':
            print('La lista se autodestruirá')
        case _:
            print('La lista fue salvada')
            mi_lista = lista
    return mi_lista

print(probar_suerte(lanzar_moneda(),lista_numeros))



from array import array
temp_array = array('i', [1,2,3])
print(temp_array.index(2))
temp_array.insert(10, 'hello')
print(temp_array)