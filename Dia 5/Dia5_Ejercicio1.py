"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""

def devolver_distintos(num1: int, num2: int, num3: int) -> int:
    numbers = [num1,num2,num3]
    suma = sum(numbers)
    maximo = max(numbers)
    minimo = min(numbers)

    if suma > 15:
        return maximo
    elif suma <10:
        return minimo
    else:
        for num in numbers:
            if num != maximo and num != minimo:
                return num
            else:
                pass

print(devolver_distintos(1,2,10))

"""
SOLUCIÓN DEL PROFESOR
"""

def devolver_distintos(num1: int, num2: int, num3: int) -> int:
    numbers = [num1,num2,num3]
    suma = sum(numbers)
    if suma > 15:
        return max(numbers)
    elif suma <10:
        return min(numbers)
    else:
        numbers.sort()
        return numbers[1]

print(devolver_distintos(1,2,10))