"""
Colección ordenada de objetos, se escribe entre corchetes y puede contener muchos items en su interior, son ordenadas y cada elemento
un lugar numerado

EJEMPLO: [1, 2, 3, 4], ['hola','como ta', 'le ta le tu'], [1, 'hola', 'sal', 'marte',0]
POSICIÓN: 0  1  2  3 
"""

mi_lista=['a','b','c']
print('Tipo: ',type(mi_lista))
print('Tamaño: ',len(mi_lista))
print('Primer valor: ', mi_lista[0])
print('Ultimo valor: ', mi_lista[len(mi_lista)-1])

#Igual que en Dia3_extraer_sub-string.py se puede obtener una parte de la lista
print('Dos primeros elementos de la lista: ', mi_lista[0:2] )
print('Todos los elementos invertidos: ', mi_lista[::-1] )

mi_lista2=['d','f','g']
mi_lista3=mi_lista+mi_lista2
print('lista 3: ',mi_lista3)


mi_lista3[0]='alfa'
print('lista 3: ',mi_lista3)

#agrega a la lista un elelnto
mi_lista3.append('append')
print('lista 3: ',mi_lista3)

#eliminar algún elemento de la lista, si no se pone parámetro se elimina el último element
mi_lista3.pop(0)
print('lista 3: ',mi_lista3)


lista_ordenar = ['g','o','b','m','c']
print(lista_ordenar)
lista_ordenar.sort()
print(lista_ordenar)


lista_ordenar = ['g','o','b','m','c']
new_list = lista_ordenar.copy()
new_list.sort()
print(new_list)

new_list.reverse()
print(new_list)


redes = ['YouTube', 'Facebook', 'Twitter', 'Whatsapp']
redes.sort()
print(redes)