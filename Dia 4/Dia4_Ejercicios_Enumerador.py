lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

for a in enumerate('Python'):
    print(a)

lista_indices = []
for tupla in enumerate("Python"):
    lista_indices.append(tupla)
print(lista_indices)


p = 'mi string'.startswith('m')
print(p)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print (indice)
    else:
        continue
    