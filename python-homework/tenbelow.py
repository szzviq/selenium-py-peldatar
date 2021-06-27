# Python while ciklus gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
# Írja ki ezek után a beolvasott számok összegét!
x = 0
flag = True
while flag:
    user_int = int(input("Írj be egy számot!"))
    if user_int < 10:
        x += user_int
    else:
        flag = False

print(x)