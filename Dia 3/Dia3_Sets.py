"""
No admite repetidos
"""

mi_set = set([1,2,3,4,5])
print(mi_set)

otro_set = {1,2,3,4}
print(otro_set)

#tamaño
print(len(mi_set))
print(2 in mi_set)


s1={1,2,3}
s2={3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)


s1.remove(2) #se puede usar discart que funciona igual, pero no arroja error cuando no existe el 2
print(s1)

s1.pop() #pop elimina de forma aleoatoria
print(s1) 

s1.clear() #deja limpio el set
print(s1)