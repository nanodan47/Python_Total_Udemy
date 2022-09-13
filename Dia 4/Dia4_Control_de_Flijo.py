if 10>112:
    print('10 es mayor a 9')
else:
    print('10 no es tan grande')


mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
else:
    print('No tienes un gato, pero no sé que animal tienes')


mascota2='perro'
if mascota2=='gato':
    print('Tienes un gato')
elif mascota2=='perro':
    print('tienes un perro')
else:
    print('no sé que mascota tienes')


edad = 16
calificacion = 9
if edad < 18:
    print('eres menor de edad')
    if calificacion >= 7:
        print('Aprobaste la asignatura')
    else:
        print('No aprobaste la asignatura')
else:
    print('eres mayor de edad')
