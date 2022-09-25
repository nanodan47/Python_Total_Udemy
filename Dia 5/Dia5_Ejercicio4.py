"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla cuántos números
primos hay en el rango que va desde cero hasta ese número
incluido, y va a devolverla cantidad de números primos que
encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
"""
def contar_primos(max_num: int) ->int:
    conteo = 0
    primos = []
    for num in range(2,max_num+1):
        primo = True
        for n in range(2,num):
            if num%n == 0:
                primo = False
                break
            else:
                pass
        if primo:
            conteo += 1
            primos.append(num)
    print(primos)
    return conteo

print(f'la cantidad de números primos hasta el número ingresado es: {contar_primos(2)}')
print(f'la cantidad de números primos hasta el número ingresado es: {contar_primos(13)}')
print(f'la cantidad de números primos hasta el número ingresado es: {contar_primos(16)}')
print(f'la cantidad de números primos hasta el número ingresado es: {contar_primos(17)}')
print(f'la cantidad de números primos hasta el número ingresado es: {contar_primos(97)}')
print(f'la cantidad de números primos hasta el número ingresado es: {contar_primos(100)}')

