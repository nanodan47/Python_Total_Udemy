
#Esto toma muchas líneas
palabra = 'python'

lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

#Así es mejor
palabra = 'python'
lista = [letra for letra in palabra]
print(lista)

#Esto es igual, pero más corto y sin variables
lista = [letra for letra in 'python']
print(lista)


lista = [n for n in range(0,21,2)]
print(lista)

#se pueden hacer operaciones a la n antes de metarla a la lista, por ejemplo n/2
lista = [n/2 for n in range(0,21,2)]
print(lista)

#También se pueden hacer condicionales
lista = [n for n in range(0,21,2) if n*2>10]
print(lista)

#Con else
lista = [n if n*2>10 else 'no' for n in range(0,21,2)]
print(lista)

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)