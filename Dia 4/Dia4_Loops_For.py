"""
Hay objetos iterables como las listas,
existen dos tipos de loops:
1. Se ejecuntan de forma infinita (while)
2. Se ejecutan de forma finita (for)
"""

nombres = ['Juan','Ana','Carlos','Belen','Fran']

for elementos in nombres:
    print('Hola')


for elementos in nombres:
    print(elementos)

lista = ['a','b','c','d']

for letra in lista:
    indice_letra = lista.index(letra)
    print(letra,indice_letra)

nombres = ['Pablo','Laura','Fede','Luis','Julia']
for nombre in nombres:
    if nombre.lower().startswith('l'):
        print(nombre)
    else:
        print('Este nombre no empieza con l')

#listas
numeros=[1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor+numero
    print(mi_valor)
print(mi_valor)

lista_con_listas =[[1,2],[3,4],[5,6]]
for a,b in lista_con_listas:
    print(a,b)

#diccionarios

dic={'clave1':'a','clave2':'b','clave3':'c'}

for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for clave,valor in dic.items():
    print(clave,valor)




#break
nombre = input('Escribe tu nombre: ')
for letra in nombre:
    if letra == 'a':
        break
    else:
        print(letra)

#continue
nombre = input('Escribe tu nombre: ')
for letra in nombre:
    if letra == 'a':
        continue
    else:
        print(letra)