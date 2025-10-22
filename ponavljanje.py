"""
broj = 10 # int (integer)
ime = "Marko"#string
znak  = 'a'#char(character)
cijena = 10.5#float (decimalni broj)
istina = False #bool (boolean)

if broj > 5:
    print ("Broj je veći od 5.")
elif broj == 5:
    print("Broj je jednak 5.")
else:
    print("Broj nije veći od 5.")

if istina:
    print("True")
else:
    print("False")

"""

# Zadatak 2
""""
print("Unesi temperaturu:")
temperatura = input()
temperatura = int(temperatura)


temperatura = int(input("Unesi temperaturu: "))
if temperatura < 0:
    print("Ledenica")
elif temperatura >=0 and temperatura <=15:
    print("Hladno")
else:
    print("vruće")
"""

#petlje
for i in range(10):
    print(i)

for slovo in "bok":
    print(slovo)