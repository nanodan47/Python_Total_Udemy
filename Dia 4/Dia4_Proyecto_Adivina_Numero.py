"""
1. Pedir el nombre del usuario
2. 'He pensado un número entre 1 y 100 y tienes solo 8 intentos para adivinarlo
3. se peude responder:  menor a 1 o mayor a 100 --> elegiste número no permitido
                        menor al número secreto
                        mayor al número secreto
                        acertó el número secreto
"""
from random import randint

nombre = input('Ingresa tu nombre: ')
numero = randint(1,100)

print(f'Hola {nombre}, he pensado un número entre 1 y 100, ¿Puedes adivinarlo en 8 intentos?')
for n in range(0,8):
    num_usuario = int(input(f'\nIngrese un numero (INTENTO {n+1}): '))
    if n == 7:
        print('*****************************')
        print('Se han acabado los 8 intentos')
        print('*****************************')
    elif num_usuario<1 or num_usuario > 100:
        print(f'El número {num_usuario} está fuera del rango')
    elif num_usuario < numero:
        print(f'El número {num_usuario} es menor al esperado')
    elif num_usuario > numero:
        print(f'El número {num_usuario} es mayor al esperado')
    else:
        print('\n¡¡¡FELICITACIONES!!!')
        print(f'Has adivinado en {n+1} intents, el número era: {num_usuario}')
        break
