"""
Entrelaza dos listas y las vuelve tuplas
nombres=['Andrea','Daniel','Fernando'] apellidos=['Jaramillo','Gutierrez','Rosero']
zip(nombres,apellidos)
list(zip(nombres,apellidos))
"""

nombres=['Andrea','Daniel','Fernando'] 
edades = [65,29,45]

nom_edad = list(zip(nombres,edades))
print(nom_edad)


#Ignora si hay uno de más
nombres=['Andrea','Daniel','Fernando','Edith'] 
edades = [65,29,45]

nom_edad = list(zip(nombres,edades))
print(nom_edad)

ciudades = ['Lima','Madrid','Mexico']
nom_edad = list(zip(nombres,edades,ciudades))
print(nom_edad)

for nombre,edad,ciudad in nom_edad:
    print(f'{nombre} tiene {edad} años y vive en la ciudad de {ciudad}')