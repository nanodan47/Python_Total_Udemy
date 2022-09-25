"""
Es elemental para trabajar cuando no se conocen las variables totales.
Debe tener un trato especial porque las operaciones serán hechas pensando
en una cantidad de parámetros n y no fijo.
*args: argumentos
**kwargs: key words argumentos

*args es una notación, pero podría ser cualquei palabra que inicia con asterisco. *gato, *perro, *casa
"""

##Función pedagógica

def suma(*args):
    total = 0
    for a in args:
        total += a
    return total

print(suma(1,2,4))


##Función usando sum
def suma(*args):
    return sum(args)

print(suma(1))



##Función usando sum
def suma(*avion):
    return sum(avion)

print(suma(1))