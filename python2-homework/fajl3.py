#Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!
with open('adat.txt', 'r') as mese:
    lines = mese.readlines()
    my_list = [s[:-1] for s in lines]

with open ('adat2.txt','w') as res:
    res.write(" ".join(my_list))