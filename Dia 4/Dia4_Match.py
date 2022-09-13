"""
Es como hacer un if donde la condición es que sea igual a algo, después igual a otra cosa, etc
"""

serie = 'N-02'
match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-01':
        print('Motorola')
    case _:
        print('Sin coincidencia')


cliente = {'nombre':'Federico',
            'edad':45,
            'ocupacion':'instructor'}
pelicula =  {
                'titulo':'matrix',
                'ficha_tecnica':{   
                                    'protagonista':'Keanu reeves',
                                    'drector':'Lana y Lilly Wachowski'
                                }
            }

elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'ocupacion':ocupacion 
             }:
             print('Es un clinete')
             print(nombre,edad,ocupacion)
        case {'titulo':titulo,
              'ficha_tecnica':{   
                                    'protagonista':protagonista,
                                    'drector':director
                              }
             }:
             print('es una película')
             print(titulo,protagonista,director)
        case _:
            print('No sé que es esto')