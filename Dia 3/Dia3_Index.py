"""
Las cadenas o strings tiene posiciones ordenadas, en python inicina desde cero.
"HOLA"  "HOLA MUNDO"  
 0123    01235678910
 También existe el indice reverso, en este caso la primera posición sigue siendo 0,
 pero las demás si cambian.
 Un ejemplo sería así. se van a separar las letroas porque se necesita espacio
 ya que son números negativos
 "H  O  L  A     M  U  N  D  O"  
  0 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""

print('>>> index() <<<\n1. Sirve para conocer el índice de un carater\n2. Conocer qué caracter hay en un índice\n')

mi_texto = 'Esta es una prueba'
resultado=mi_texto[0]
print(f'El caracter en la posición 0 es: {resultado}')
resultado=mi_texto[9]
print(f'El caracter en la posición 9 es: {resultado}')

##Ahora con los valores negativos
resultado=mi_texto[-4]
print(f'El caracter en la posición -4 es: {resultado}')

resultado=mi_texto.index('n')
print(f'la letra n está en la posición: {resultado}')

resultado=mi_texto.index('prueba')
print(f'la palabra prueba inicia en la posición: {resultado}')

##Index siempre va a devolver la priemra coincidencia, 
##podemos decirle que inicie después de cierta ubicación
##para que no coja la primera ocurrencia sino la primera
##después de esa posición
resultado=mi_texto.index('a',4)
print(resultado)

##También le puedo decir que busque desde una posición
##hasta otra, hay que recordar que: [4,11) entonces cogerá de nuevo 
##la posición 10

resultado=mi_texto.index('a',4,11)
print(resultado)


##Para hacer la búsqueda al revés existe la función
##rindex, hace lo mismo pero de derecha a izquierda


