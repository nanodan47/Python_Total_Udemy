name=input('Introduce tu nombre: ')
ventas=input('Introduce el valor de tus ventas: ')
P_comision = 0.13
valor_comision=round(int(ventas)*P_comision,2)

print(f'Hola {name}, tu comisión este mes es: ${valor_comision} cop')