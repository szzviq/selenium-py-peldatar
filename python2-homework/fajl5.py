#Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz
with open('adat.txt', 'r') as mese:
    with open('adat4.txt', 'w') as res:
        for line in mese.readlines():
            res.writelines(line)
