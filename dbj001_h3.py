import random
ubruktekort = ["\u2660A", "\u2660K", "\u2660Q", "\u2660J", "\u266010", "\u26609", "\u26608", "\u26607",
               "\u2666A", "\u2666K", "\u2666Q", "\u2666J", "\u266610","\u26669", "\u26668", "\u26667",
               "\u2663A", "\u2663K", "\u2663Q", "\u2663J", "\u266310", "\u26639", "\u26638", "\u26637",
               "\u2665A", "\u2665K", "\u2665Q", "\u2665J", "\u266510", "\u26659", "\u26658", "\u26657"]
kortibruk = []
bunken = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4, "G": 4, "H": 4}

def lagre():
    with open("lagret.txt", "w", encoding="utf-8") as innhold:
        innhold.write("Bunken:\n")
        for nøkkel, verdi in bunken.items():
            innhold.write(nøkkel + " " + str(verdi) + "\n")
        innhold.write("Kortibruk:\n")
        for kort in kortibruk:
            innhold.write(kort + "\n")
        innhold.write("Ubruktekort:\n")
        for kort in ubruktekort:
            innhold.write(kort + "\n")
def hentspill(liste1, liste2, dict):
    bunken = {}
    kortibruk = []
    with open("lagret.txt", encoding="utf-8") as innhold:
        while len(list(bunken)) < 9:
            for linje in innhold:
                (key, value) = linje.split()
                bunken[key] = value



#Lager bordet med kort
def nyttspill():
    print("Trekk to kort - X for å avbryte")

    #Forteller om spillet er vunnet eller tapt. Om ikke viser det bare brettet.
    def visbrett():
        while True:
            kort = set()

            for objekt in kortibruk:
                kort.add(objekt[-1])

            if sum(list(bunken.values())) == 0:
                print("Gratulerer du har vunnet spillet.")
                break

            elif len(kort) == len(set(kortibruk)):
                navn = ("      ".join(list(bunken.keys())))
                print("\t", navn)
                print("   ", "     ".join(kortibruk))
                antall = list(map(str, list(bunken.values())))
                print("\t", "      ".join(antall))
                print("Ingen mulige trekk.")
                break


            else:
                navn = ("      ".join(list(bunken.keys())))
                print("\t", navn)
                print("   ", "     ".join(kortibruk))
                antall = list(map(str, list(bunken.values())))
                print("\t", "      ".join(antall))
                endrekort()


    #Gyldigtrekk, 2 forskjellige bunker som ikke er tomme, og kort med samme verdi
    def gyldigvalg(liste):
        if len(liste) == 2 and liste[0].upper() != liste[1].upper() and liste[0].upper() in list(bunken.keys())and liste[1].upper() in list(bunken.keys()):
            if kortibruk[list(bunken.keys()).index(liste[0].upper())][-1] == kortibruk[list(bunken.keys()).index(liste[1].upper())][-1]:
                for bokstav in liste:
                    if bunken[bokstav.upper()] > 0:
                        return True
                    else:
                        print("Bunken du har valgt er allerede tom.")
                        return False
            else:
                print("Kortene har ikke samme verdi.")
        else:
            return False

    # endre en posisjon
    def endrekort():
        valgt = input("Velg bunker: ")
        if valgt.upper() == "X":
            xvalg = input("Spillet avbrutt. Tast 2 for å lagre, 0 for meny: ")
            if int(xvalg) == 0:
                pass
            elif int(xvalg) == 2:
                lagre()
        elif gyldigvalg(valgt):
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


def start():
    info = ("""1 - start nytt spill
2 - lagre spillet
3 - hent lagret spill
4 - avslutt""")
    print(info)
    while True:
        valg = int(input("Velg handling (0 for meny)\n"))
        if valg == 1:
            while len(kortibruk) < 8:
                kort = ubruktekort.pop(random.randint(0, len(ubruktekort) - 1))
                kortibruk.append(kort)
            nyttspill()
        elif valg == 2:pass
        elif valg == 3:pass
        elif valg == 4: break
        elif valg == 0: print(info)

start()
