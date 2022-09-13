monedas = 5
while monedas > 0:
    print(f'tengo {monedas} monedas')
    monedas = monedas-1
    monedas -=1
else:
    print('No tengo más dinero')


respuesta = 's'
while respuesta == 's':
    respuesta = input('¿Quieres seguir (s/n)? ')
else:
    print('Has decidido no continuar')

#Con pass el while pasa 
respuesta = 's'
while respuesta == 's':
    respuesta = 'n'
print('hola')

#break
nombre = input('Escribe tu nombre: ')
for letra in nombre:
    if letra == 'a':
        break
    else:
        print(letra)

#continue
nombre = input('Escribe tu nombre: ')
for letra in nombre:
    if letra == 'a':
        continue
    else:
        print(letra)


numero = 50
while numero<= 0:
    if numero%5 == 0:
        print(numero)
        numero-=1
    else:
        numero-=1