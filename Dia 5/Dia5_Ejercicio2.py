"""
Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden alfabético. 
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']

"""

def ordenadas_unicas(palabra: str) -> list:
    lista = {letra for letra in palabra}
    lista = list(lista)
    lista.sort()
    return lista

print(ordenadas_unicas('entretenido'))