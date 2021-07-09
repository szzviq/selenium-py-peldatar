with open('adat.txt', 'r') as mese:
    lines = mese.readlines()
    my_list = [s[:-1] for s in lines]
    print(" ".join(my_list))


