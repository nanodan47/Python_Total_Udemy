from random import choice

def es_letra(letra: str)->bool:
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if letra in abecedario:
        return True
    else:
        return False


def esta_en_palabra(letra: str, palabra:str)->bool:
    if letra in palabra:
        return True
    else:
        return False
    
def escoger_palabra(palabras:dict):
    palabra,longitud = choice(list(palabras.items()))
    return palabra,longitud


palabras_juego =    {
                        'almuerzo':'--------',
                        'arbol':'-----',
                        'carro':'-----',
                        'computador':'----------'
                    }

palabra,longitud = escoger_palabra(palabras_juego)
#palabra = 'carro'
#longitud = '-----'
print('\n--------------------- Inicio Juego ----------------------')
print('Bienvenido a ahorcado, intenta adivinar la palabra, tienes 6 vidas para lograrlo')
print(f'La palabra tiene {len(longitud)} letras')

adivino = False
restantes = 6
dichas = []
malas = []

while not adivino and restantes > 0:
    if len(dichas) == 0:
        validacion = False
        while not validacion:
            letra = input('Ingresa una letra: ').lower()
            print('********************************')
            print('\n')
            validacion = es_letra(letra)
            if not validacion:
                print(f'\nNo ingresaste una letra válida o ingresaste más de una, vuelve a intentarlo')
            else:
                dichas.append(letra)
    else:
        dichas.sort()
        print(f'\nYa has dicho estas letras{dichas}')
        print(f'Las malas son {malas}')
        validacion = False
        while not validacion:
            letra = input('Ingresa una letra: ').lower()
            print('********************************')
            print('\n')
            validacion = es_letra(letra)
            if not validacion:
                print(f'\nNo ingresaste una letra válida, vuelve a intentarlo')
            elif letra in dichas:
                print(f'Ya has dicho la letra {letra}, vuelve a intentarlo')
                validacion = False
            else:
                dichas.append(letra)
    ##Valido si la letra existe
    existe = esta_en_palabra(letra,palabra)
    ##Caso en que la letra exista en la palabra
    if existe:
        print('La letra se encuentra en la palabra')
        cantidad_ocurrencias = palabra.count(letra)
        if cantidad_ocurrencias > 1:
            pos = 0
            for l in palabra:
                if l == letra:
                    longitud = longitud[:pos]+l+longitud[pos+1:]
                    pos+=1
                else:
                    pos+=1 
        else:
            idx = palabra.index(letra)
            longitud = longitud[:idx] +letra+ longitud[idx+1:]
        print(f'Adivinado:    {longitud}')
        print(f'Te faltan {longitud.count("-")} letras')
        adivino = not esta_en_palabra('-',longitud)
        if adivino:
            print(adivino)
            print(f'*************** HAS ADIVINADO ***************\n\n           la palabra era {palabra.upper()}')
            print(f'\n\n*************** FIN DEL JUEGO ***************')
    else:
        malas.append(letra)
        malas.sort()
        restantes -=1
        if restantes == 0:
            print(f'\n\nSe han acabado las vidas, la palabra era {palabra.upper()}')
            print(f'*************** FIN DEL JUEGO ***************')
        else:
            print(f'La letra no está dentro de la palabra. Te quedan {restantes} vidas')
            print(f'Adivinado:    {longitud}')


