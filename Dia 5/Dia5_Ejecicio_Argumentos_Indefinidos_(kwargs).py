"""
Crea una función llamada cantidad_atributos que cuente la cantidad de 
parémetros que se entregan, y devuelva esa cantidad como resultado.
"""

def cantidad_atributos(**kwargs):
    cuetna = 0
    for arg in kwargs:
        cuetna += 1
    return cuetna

dic = {'a':1,'b':2}
print(cantidad_atributos(**dic))



"""
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de 
los atributos entregados en forma de palabras clave (keywords). 
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
"""

def lista_atributos(**kwargs):
    lista=[]
    for key,value in kwargs.items():
        lista.append(value)
    return lista

dic = {'a':1,'b':2}
print(lista_atributos(**dic))


"""
Crea una función llamada describir_persona, que tome como parámetros su nombre y 
luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
"""
def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}:')
    for key,val in kwargs.items():
        print(f'{key}: {val}')
        
describir_persona('tomás',color_ojos='azules',color_pelo='rubio')
