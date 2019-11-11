import random
ubruktekort = ["\u2660A", "\u2660K", "\u2660Q", "\u2660J", "\u266010", "\u26609", "\u26608", "\u26607",
               "\u2666A", "\u2666K", "\u2666Q", "\u2666J", "\u266610","\u26669", "\u26668", "\u26667",
               "\u2663A", "\u2663K", "\u2663Q", "\u2663J", "\u266310", "\u26639", "\u26638", "\u26637",
               "\u2665A", "\u2665K", "\u2665Q", "\u2665J", "\u266510", "\u26659", "\u26658", "\u26657"]
kortibruk = []
bunken = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4, "G": 4, "H": 4}

#Lager bordet med kort
def spill():

    def visbrett():
        if sum(list(bunken.values())) == 0:
            print("Gratulerer du har vunnet spillet.")
        else:
            navn = ("      ".join(list(bunken.keys())))
            print("\t", navn)
            print("   ", "     ".join(kortibruk))
            antall = list(map(str, list(bunken.values())))
            print("\t", "      ".join(antall))

    #Gyldigtrekk, 2 forskjellige bunker som ikke er tomme, og kort med samme verdi
    def gyldigvalg(liste):
        kortposisjon = []
        if len(liste) == 2 and liste[0].upper() != liste[1].upper() and liste[0].upper() in list(bunken.keys())and liste[1].upper() in list(bunken.keys()):
            kortposisjon.append()
            for bokstav in liste:
                if bunken[bokstav.upper()] > 0:
                    return True
                else:
                    print("Bunken du har valgt er allerede tom.")
                    return False
        else:
            return False

    # endre en posisjon
    def endrekort():
        valgt = input("Velg bunker: ")
        if gyldigvalg(valgt):
            for bokstav in valgt.upper():
                if bokstav.upper() in list(bunken.keys()):
                    index = list(bunken.keys()).index(bokstav)
                    if bunken[bokstav.upper()] - 1 > 0:
                        bunken[bokstav.upper()] -= 1
                        kortibruk[index] = ubruktekort.pop(random.randint(0, len(ubruktekort) - 1))
                    else:
                        bunken[bokstav.upper()] = 0
                        kortibruk[index] = "  "
        else:
            print("Ikke gyldig input.")
        visbrett()


    print("Trekk to kort - X for å avbryte")
    while len(kortibruk) < 8:
        kort = ubruktekort.pop(random.randint(0,len(ubruktekort) - 1))
        kortibruk.append(kort)

    visbrett()
    while True:
        endrekort()

spill()





def start():
    while True:
        hjelp = ("""1 - start nytt spill
    2 - lagre spillet
    3 - hent lagret spill
    4 - avslutt""")
        print(hjelp)
        valg = int(input("Velg handling (0 for meny)\n"))
        if valg == 1: lagbord()
        elif valg == 2:pass
        elif valg == 3:pass
        elif valg == 4: break
        elif valg == 0: print(hjelp)
