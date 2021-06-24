# feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
#irj programot, ami kiírja a kisbetűket, és melléjük az karakter kódjukat! A kiírás több oszlopos legyen, és legfeljebb 10 soros. Minta:


for number in range(ord("a"),ord("a")+10):
    if number+20 <= ord("z"):
        print("{} {} {} {} {} {}".format(chr(number), number, chr(number+10), number+10, chr(number+20), number+20))
    else:
        print("{} {} {} {} ".format(chr(number), number, chr(number + 10), number + 10))