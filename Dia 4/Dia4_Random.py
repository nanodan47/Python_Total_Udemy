from calendar import leapdays
from random import randint as r #numero aleatorio entero
from random import uniform #numero aleatorio float uniform(desde,hasta)
from random import random #numero aleatorio entre 1 y 0
from random import choice
from random import shuffle

aleatorio = r(1,50)
print(aleatorio)

aleatorio = round(uniform(0,1),2) 
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul','rojo','verde','amarillo']
r_color = choice(colores)
print(r_color)

numeros = list(range(5,51,5))
print(numeros)
shuffle(numeros)
print(numeros)