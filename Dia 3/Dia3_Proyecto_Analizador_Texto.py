"""
1. Pedir un texto largo al usuario
2. Pedir 3 letras separadas por coma
@@Return:
    1. Cuantas veces aparece cada letra
    2. Cuantas palabras hay en total (se puede usar split)
    3. Primera y última letra del texto
    4. Palabras en orden inverso
    5. ¿Está la palabra python en el texto?
"""
#palabra = input('Ingrese un texto: ').lower()
#letras = input('Ingrese 3 letras separadas por coma, sin espacios: ').lower()
#letras = []
#letras.append(input('Ingrese la primera letra: ')).lower()
#letras.append(input('Ingrese la segunda letra: ')).lower()
#letras.append(input('Ingrese la tercera letra: ')).lower()
from pydoc import plain


palabra = ('El dia de hoy estamos revisando el proyecto 3 del curso python').lower()
letras = ('a,b,c').lower()
dic_respuestas = {}


lista_letrasa=letras.split(',')

#1. Cuantas veces aparece cada letra
dic_respuestas[f'Letra {lista_letrasa[0]}'] = palabra.count(lista_letrasa[0])
dic_respuestas[f'Letra {lista_letrasa[1]}'] = palabra.count(lista_letrasa[1])
dic_respuestas[f'Letra {lista_letrasa[2]}'] = palabra.count(lista_letrasa[2])

#2. Cuantas palabras hay en total
lista_palabras = palabra.split(' ')
dic_respuestas['Cantidad palabras'] = len(lista_palabras)

#3. Primera y última letra del texto
dic_respuestas['Primera letra'] = palabra[0]
dic_respuestas['Ultima letra'] = palabra[-1]

#4. Palabras en orden inverso
lista_palabras_inversa = lista_palabras[::-1]
palabras_inversa = ' '.join(lista_palabras_inversa)
dic_respuestas['Palabras orden inverso'] = palabras_inversa
#Otra forma
lista_palabras.reverse()
palabras_inversa = ' '.join(lista_palabras)



#5. ¿Está la palabra python en el texto?
my_bool = 'python' in lista_palabras
dic_bool = {True:'Sí',False:'No'}

dic_respuestas['Esta python'] = dic_bool[my_bool]

print(dic_respuestas)
