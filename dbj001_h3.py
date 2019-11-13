import random

info = ("""1 - start nytt spill
2 - lagre spillet
3 - hent lagret spill
4 - avslutt""")

allekort = ["\u2660A", "\u2660K", "\u2660Q", "\u2660J", "\u266010", "\u26609", "\u26608", "\u26607",
            "\u2666A", "\u2666K", "\u2666Q", "\u2666J", "\u266610","\u26669", "\u26668", "\u26667",
            "\u2663A", "\u2663K", "\u2663Q", "\u2663J", "\u266310", "\u26639", "\u26638", "\u26637",
            "\u2665A", "\u2665K", "\u2665Q", "\u2665J", "\u266510", "\u26659", "\u26658", "\u26657"]

allebunker = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4, "G": 4, "H": 4}

bunken = {}
kortibruk = []
ubruktekort = []

def lagre():
    if len(kortibruk) == 0 and len(ubruktekort) == 0 and len(list(bunken.keys())) == 0:
        print("Det er ingenting å lagre. Start et spill for å generere data.")
    else:
        with open("bunken.txt", "w", encoding="utf-8") as innhold:
            for nøkkel, verdi in bunken.items():
                innhold.write(nøkkel + " " + str(verdi) + "\n")
        with open("kortibruk.txt", "w", encoding="utf-8") as innhold:
            for kort in kortibruk:
                innhold.write(kort + "\n")
        with open("ubruktekort.txt", "w", encoding="utf-8") as innhold:
            for kort in ubruktekort:
                innhold.write(kort + "\n")
        print("Spillet er lagret.")

def nybunke():
    global allekort, allebunker, bunken, kortibruk, ubruktekort

    bunken = {}
    kortibruk = []
    ubruktekort = []

    for kort in allekort:
        ubruktekort.append(kort)
    for nøkkel, verdi in allebunker.items():
        bunken[nøkkel] = verdi

    while len(kortibruk) < 8:
        kort = ubruktekort.pop(random.randint(0, len(ubruktekort) - 1))
        kortibruk.append(kort)

def hentbunke():
    global bunken, kortibruk, ubruktekort

    bunken = {}
    kortibruk = []
    ubruktekort = []


    with open("bunken.txt", encoding="utf-8") as dokument:
        for linje in dokument:
            nøkkel, verdi = linje.split()
            bunken[nøkkel] = int(verdi)

    with open("kortibruk.txt", encoding="utf-8") as dokument:
        for linje in dokument:
            kortibruk.append(linje.strip("\n"))

    with open("ubruktekort.txt", encoding="utf") as dokument:
        for linje in dokument:
            ubruktekort.append(linje.strip("\n"))




def spill(loading):
    global bunke, kortibruk, ubruktekort
    loading()
    print("Trekk to kort - X for å avbryte")

    # Gyldigtrekk, 2 forskjellige bunker som ikke er tomme, og kort med samme verdi
    def gyldigvalg(liste):
        if len(liste) == 2 and liste[0].upper() != liste[1].upper() and liste[0].upper() in list(bunken.keys()) and \
                liste[1].upper() in list(bunken.keys()):
            if kortibruk[list(bunken.keys()).index(liste[0].upper())][-1] == \
                    kortibruk[list(bunken.keys()).index(liste[1].upper())][-1]:
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

    def status():
        kort = set()

        for objekt in kortibruk:
            kort.add(objekt[-1])

        if sum(list(bunken.values())) == 0:
            print("Gratulerer du har vunnet spillet.")
            return False

        elif len(kort) == len(set(kortibruk)):
            navn = ("      ".join(list(bunken.keys())))
            print("\t", navn)
            print("   ", "     ".join(kortibruk))
            antall = list(map(str, list(bunken.values())))
            print("\t", "      ".join(antall))
            print("Ingen mulige trekk.")
            return False


        else:
            return True

    while status():
        navn = ("      ".join(list(bunken.keys())))
        print("\t", navn)
        print("   ", "     ".join(kortibruk))
        antall = list(map(str, list(bunken.values())))
        print("\t", "      ".join(antall))

        valg = input("Velg bunker:")

        if valg.upper() == "X":
            print("Spillet avbrutt. Tast 2 for å lagre, 0 for meny: ")
            break

        elif gyldigvalg(valg):
            for bokstav in valg.upper():
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





def valg():
    print(info)

    while True:
        try:
            valg = int(input("Velg handling (0 for meny)\n"))
            if valg == 1: spill(nybunke)
            elif valg == 2:
                lagre()
            elif valg == 3:spill(hentbunke)
            elif valg == 4:
                print("Takk for nå.")
                break
            elif valg == 0: print(info)
            else:
                print("Input skal være tall mellom 0-4")
        except:
            print("Input skal være tall mellom 0-4")

valg()
