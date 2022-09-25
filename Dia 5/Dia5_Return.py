def multiplicar(numero1, numero2):
    return numero1 * numero2

mi_mult = multiplicar(5,10)
print(mi_mult)



#Invertir Strings

def invertir_palabra(palabra):
    word = palabra.upper()
    word = word[::-1]
    print(word)

invertir_palabra('python')



def invertir_cadena(cadena):
    return cadena[::-1]


def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida


print(invertir_cadena("Hola"))
print(invertir_cadena_manual("Hola"))
print(invertir_cadena("parzibyte.me"))
print(invertir_cadena_manual("parzibyte.me"))
print(invertir_cadena("All the young dudes"))
print(invertir_cadena_manual("All the young dudes"))