"""
Son parecidas a las listas, pero son inmutables
*Ocupan menos espacio en memorio y se consultan más rápido
*No se puede modificar

Se puede declarar asi ('a','b','c') o 'a','b','c'
"""

mi_tupla=(1,2,3,4)
mi_tupla2= 1,2,3,4

print(type(mi_tupla))
print(type(mi_tupla2))

mi_tupla_mixta = (5,5.5,'String','Diccionario')
print(mi_tupla_mixta[0])
print(mi_tupla_mixta[-2])


mi_tupla=(1,2,(10,20),4)
print(mi_tupla[2])
print(mi_tupla[2][0])


#se puede castear 
mi_tupla = list(mi_tupla)
print(type(mi_tupla))
mi_tupla[0]=16
mi_tupla = tuple(mi_tupla)
print(type(mi_tupla))
print(mi_tupla)

a,b,c,d = mi_tupla
print('a: ',a)
print('b: ',b)
print('c: ',c)
print('d: ',d)

#Largo de la tupla
print(len(mi_tupla))
print(mi_tupla.count(2))
print(mi_tupla.index(16))