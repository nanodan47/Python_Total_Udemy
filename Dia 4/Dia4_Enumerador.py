"""
Facilita acceder a los índices de una lista
"""
lista = ['a','b','c']
indice = 0

for item in lista:
    print (indice,item)
    indice += 1

for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)

for indice,item in enumerate(range(50,55)):
    print(indice,item)    

mi_tupla = list(enumerate(lista))
print(mi_tupla)
print(mi_tupla[0][0])

