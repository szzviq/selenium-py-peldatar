#Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így, ahogy beolvastad, soronként egy szóval egy másik fájlba!
with open('adat.txt', 'r') as mese:
        # res.append(line.split(None,1)[0])
        mese_list = mese.readlines()

with open ('adat3.txt','w') as res:
    res.writelines(mese_list)
    # (" ".join(mese_list))