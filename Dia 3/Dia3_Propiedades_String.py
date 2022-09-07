"""
PROPIEDADES:

Los Strings son inmutables
Los Strings se pueden multiplicar
Salos de línea con """ """
Combropar existencia de caractar con in
Tamaño del String con len(texto)

"""

#Inmutabilidad
nombre = 'Carina'
#nombre[0] = 'K' #Esto no se puede hacer
nombre = nombre.replace('C','K')
print(nombre)

#Los nombres se pueden multiplicar
print(nombre*10)


#saltos de línea con comillas triples
poema = '''Mil pequeños peces blancos
como si hirviera
el color del agua '''
print(poema)

print('agua' in poema)
print('sol' in poema)
print('agua' not in poema)
print('sol' not in poema)


#Cantidad de caracteres (incluye espacios, signos de admiración, preguta, etc...)
print(len(poema))