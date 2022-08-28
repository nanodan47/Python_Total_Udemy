"""
Los problemas al imprimir variables a veces es cansón, así que se creo el format
supongamos dos variables:

color = 'gris'
modelo = 2016

print('Mi auto es color {} y modelo {}'.format(color,modelo))

Esto no es tán fácil de leer para el ojo, entonces en python 3 se inventó lo siguiente, se antepone una f

print(f'Mi auto es {color} y modelo {modelo}')
"""

print('********* Método 1 *********')
x = 10
y = 5
print('Las coordenadas en mi plano cartecianos son x: {} y y: {}'.format(x,y))

print('\n********* Método 2 *********')

print(f'Las coordenadas en mi plano cartecianos son x: {x} y y: {y}')




print('\n********* Método 1 *********')

print('Las suma entre x: {} y y: {} es: {}'.format(x,y,x+y))

print('\n********* Método 2 *********')

print(f'Las suma entre x: {x} y y: {y} es: {x+y}')

