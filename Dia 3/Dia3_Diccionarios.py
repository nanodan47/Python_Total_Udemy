"""
Es como el diccionario de la vida real, tiene una palabra clave y un valor asociado a esa clave.
Las claves son únicas dentro del diccionario
dic={'clave1':'valor1', 'clave2':'valor2'}
No tiene orden ya que se busca es por clave y no por índice.
"""

diccionario = {'c1':'Valor1','c2':'Valor1'}
print(type(diccionario))
print(diccionario)
print(diccionario['c1'])

for value in diccionario:
    print(value)
    print(diccionario[value])

dic_cliente={'nombre':'Juan','apellido':'Fuentes','peso':78,'talla':1.76}
consulta_cliente=dic_cliente['apellido']
print(consulta_cliente)


dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'])
print(dic['c2'][1])


print(dic['c3'])
print(dic['c3']['s2'])

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())


#Agregar al diccionario 
dic = {1:'a',2:'b'}
print(dic)
dic[3] = 'c'
print(dic)

#Sobre escribir en un diccionario
dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())



mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])