# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik.
# Kétféle italt ismerünk: sör és kóla. Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki. Ha a felhasználó 60 feletti,
# és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását. Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")

ital = input("Mit szeretne inni, sört vagy kólát? ")
if ital == "sört":
    kor = int(input("Hány éves?"))
    if kor < 18:
        print("csak nagykorúakat szolgálhatunk ki alkohollal")
    else:
        print("Parancsoljon, a söre")
elif ital == "kólát":
    kor = int(input("Hány éves?"))
    if kor > 60:
        print("a koffein megemelheti a vérnyomását")
    else:
        print("Parancsoljon, a kólája")
else:
    print("csak sör van és kóla")