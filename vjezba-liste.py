"""

moja_lista = [10,20,30]

prvi_element = moja_lista[0]

print (prvi_element)

moja_lista.append(40)

print (moja_lista)

dio_liste = moja_lista[1:3]

print (dio_liste)

"""
"""
lista_voca = ['jabuka', 'banana', 'kruška']

prvi_element = lista_voca[0]

print(prvi_element)

lista_voca.append('naranča')

print(lista_voca)

"""
"""
ormar=[
    ['majica', 'kapa', 'sal'],
    ['hlace', 'carape', 'remen'],
    ['jakna', 'cipele', 'cizme']
]

print(f"Hlače? {ormar[1][0]}")
"""
"""
print(ormar [1][0])
print(ormar [1][1])
print(ormar [2][1])
"""
"""
for odjeca in ormar:
    print (odjeca[1])

for redak in ormar:
    print (f"sadržaj retka: {redak}")

for element in redak:
    print (f"Element; {element}")
"""
def pronadji_broj (lista, broj):
    print (f"Tražim broj {broj} u listi {lista}")
    prekidac = False
    
    for element in lista:
        if element == trazeni_broj:
            prekidac = True
            break
        else:
            prekidac = False
    if prekidac:
        print (f"Broj {trazeni_broj} je pronađen u listi.")
    else:
        print (f"Broj {trazeni_broj} nije pronađen u listi.")

    
lista=[10,20,30,40,50]
trazeni_broj=30
pronadji_broj (lista, trazeni_broj) 