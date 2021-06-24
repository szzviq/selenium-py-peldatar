# Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik, nem szökőév minden századik, mégis az minden 400-adik. (2000-ben ezért volt szökőév.) A függvény visszatérési értéke legyen logikai típusú! Tipp( % maradekos osztas operátor)
# Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e! Használd az előbb megírt függvényt! Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.

year = int(input("milyen évet írunk? "))
def leapyear(this_year):
    result = False
    if (this_year % 400 == 0):
        result = True
    elif (this_year % 4 == 0) and not (this_year % 100 == 0):
        result = True

    return result

if leapyear(year):
    print("ez szökőév")
else:
    print("nem szökőév")