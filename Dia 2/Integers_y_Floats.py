mi_numero=1+3
print(mi_numero)
print('el tipo de dato de "mi_numero" es: '+ str(type(mi_numero)))

mi_decima = 5.8
print(mi_decima)
print('\nel tipo de dato de "mi_numero" es: '+ str(type(mi_decima)))

mi_numero2=mi_numero+mi_numero
print(mi_numero2)

#Lo importante para esta prueba es ver qué tipo termina siendo,
#Será del tipo del resultado, en este caso float
prueba = 5+5.8
print(prueba)
print('\nel tipo de dato de "mi_numero" es: '+ str(type(prueba)))

#Usando input, recordar que todo lo que entra es texto, así que los
#números toca convertirlos
edad = input('Introduce tu edad: ')
edad = int(edad)
print('tu edad en 10 años será: '+str(edad+10)+' años')

