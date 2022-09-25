def saludar():
    """
    Función que imprime la palabra ¡Hola mundo!
    cada vez que es llamada
    :return:
    """
    print('¡Hola mundo!')


def bienvenida(nombre_persona):
    """
    Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, 
    y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
    Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
    Solo debes definir la función y crear la variable, no debes invocar la función luego.
    """
    print(f'¡Bienvenido {nombre_persona}!')
nombre_persona = 'Daniel'




def cuadrado(un_numero):
    """
    Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, 
    imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
    El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.
    Solo debes definir la función y crear la variable, no debes invocar la función luego.
    """
    print(un_numero**2)
un_numero = 10