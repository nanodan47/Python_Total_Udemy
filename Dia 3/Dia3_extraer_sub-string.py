"""
mi_texto = esta palabra
Nuevamente la función no es inclusiva al terminar el intervalo
entonces [a,b) incluye a, pero no b.
Un tercer parámetro es cada cuanto quiero tomar un caracter
entonces: 
mi_texto[1:6] --> sta p  incluye el 1, pero no el 6
mi_texto[1:6:2] --> sap  salta de 2 en dos, además eliminó el epsacio

"""
from cgitb import text


mi_texto = 'esta palabra'
print(mi_texto[1:6:2] )

texto = 'ABCDEFGHIJKLM'
fragmento=texto[2:5]
print(fragmento)

fragmento=texto[2:]
print(fragmento)

fragmento=texto[:5]
print(fragmento)

fragmento=texto[2:10:2]
print(fragmento)

fragmento=texto[::2]#= texto[0:max(texto):2]
print(fragmento)


fragmento=texto[::-1]#= Todas las letras en orden inverso con saltos de 1
print(fragmento)

fragmento=texto[::-2]#= Todas las letras en orden inverso con saltos de 2
print(fragmento)


print(max(texto))