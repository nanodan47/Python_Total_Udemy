"""
Funciona muy parecido a **args, pero se debe pasar un diccionario, o en algunas
ocasiones, una lista de pares puede funcionar, por ejemplo x=3,y=5,z=6 y el lo convertirá en diccionario
"""

def suma(**kwargs):
    print(type(kwargs))
    print((kwargs))
suma (x=3,y=5,z=6) 


def recorrer(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}') 
        total += valor
    return total

print(recorrer(x=3,y=5,z=6))



def prueba (num1,num2,*args,**kwargs):
    print(f'el primer valor es {num1}')
    print(f'el primer valor es {num2}')
    for argumentos in args:
        print(f'args = {argumentos}')
    for key, value in kwargs.items():
        print(f'{key} = {value}')


prueba(12,50,100,200,300,400,x='uno',y='dos',z='tres')

#se pueden desempaquetar listas y demás
args = [100,200,300,400]
kwargs={'x':'uno','y':'dos','z':'tres'}

prueba(12,50,*args,**kwargs)
    