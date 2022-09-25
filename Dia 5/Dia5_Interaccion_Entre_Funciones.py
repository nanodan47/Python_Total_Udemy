#Esoger el palito más corto lava la loza
from random import shuffle
#Primero una lista inicial
palitos=['-','--','---','----']

#Mezclar palitos
def mezclar_lista(lista):
    shuffle(lista)
    return lista


#Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Elige un número del 1 al 4: ')
    return int(intento)

#Comprobar el intento
def chequear_intento(lista,intento):
    if lista[intento-1]=='-':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')
    print(f'Te ha tocado {lista[intento-1]}')


palitos_mezclados = mezclar_lista(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)