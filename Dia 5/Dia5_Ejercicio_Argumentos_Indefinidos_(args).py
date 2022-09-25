def suma_cuadrados(*args):
    """
    Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos 
    numéricos, y que retorne la suma de sus valores al cuadrado.
    Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
    """
    total_cuadrado = 0
    for num in args:
        total_cuadrado += num**2
    return total_cuadrado

print(suma_cuadrados(1,2,3))


def suma_absolutos(*args):
    """
    Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier 
    extensión, y retorne la suma de sus valores absolutos 
    (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere 
    a todos -negativos y positivos- como positivos).
    """    
    print([abs(num) for num in args])
    return sum([abs(num) for num in args])

print(suma_absolutos(-1,2,3))



def numeros_persona(nombre,*args):
    """
    Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
    La función debe devolver el siguiente mensaje:
    "{nombre}, la suma de tus números es {suma_numeros}"
    """
    return f'{nombre}, la suma de tus números es {sum(args)}'

print(numeros_persona('Daniel',1,2,3,4,5,6))