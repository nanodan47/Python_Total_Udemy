precios_cafe = [('capuchino',1.5),('Expresso',2.2),('Moka',1.9)]

for elemento in precios_cafe:
    print(elemento)

for cafe,precio in precios_cafe:
    print(cafe)
    print(precio)



##Definición de cafe 
def cafe_mas_caro(lista_precios):
    mayor=0
    coffee = ''

    for cafe,precio in lista_precios:
        if precio > mayor:
            mayor = precio
            coffee = cafe
        else:
            pass
    return (coffee,mayor)

print(cafe_mas_caro(precios_cafe))

cafe,precio = cafe_mas_caro(precios_cafe)

print(f'El cafe más caro es {cafe}, su precio es {precio}')