num1 = 20
num2 = 30.5

print(type(num1))
print(type(num2))

num3 = num1+num2
print(type(num3))

## Conversión de datos
num4=int(num3) #int para convertir a número enter
print(str(num3)+' ---> '+str(num4)) #str para converti a string
print(type(num4))


edad=input('Introduce tu edad: ')
print(type(edad))
edad=int(edad)
print(type(edad))
print('tu nueva edad va a ser: '+str(edad+10))

prueba = 10
prueba = float(prueba)
print(type(prueba))