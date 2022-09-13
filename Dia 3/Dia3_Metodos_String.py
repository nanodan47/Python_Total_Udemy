"""
FUNCIONES:

*upper():   Pasa todo a mayúsculas                      --> texto.upper()
*lower():   Pasa todo a minúsculas                      --> texto.lower()
*split():   Separa en partes (listas)                   --> texto.split('separador del texto')
*join():    Unir items usando sparador                  --> 'separador'.join(lista o textos)
*find():    Encontrar un substring                      --> text.find('los que busca')
*replace(): Permite reemplazar una palabra por otra     --> texto.replace('buscado','reemplazo')

"""

texto='Este es el texto de Federico'
resultado=texto.upper()
print(resultado)


texto='Este es el texto de Federico'
resultado=texto.lower()
print(resultado)

texto='Este es el texto de Federico'
resultado=texto.split(' ')
print(resultado)

a='Aprender'
b='Python'
c='es'
d='genial'
resultado='-'.join([a,b,c,d])
print(resultado)

#Cuando find no encuentra lo que busca devuelve un -1
texto='Este es el texto de Federico'
resultado=texto.find('s')
print(resultado)


texto='Este es el texto de Federico'
resultado=texto.replace('Federico','Todos').replace('texto','almuerzo')
print(resultado)



texto = 'IX'
print(texto.split())