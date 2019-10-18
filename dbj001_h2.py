karakterer = {}
emner = []


fagområde = {"Informasjonsvitenskap": "INFO", "Økonomi": "ECON", "Filosofi": "EXP","Organisasjonsvitenskap": "AORG", "Matematikk": "MAT"}


def emneliste():
    global emner, karakterer, fagområde
    print("Velg fag og/eller emnenivå (<enter> for alle)")

    område = input(" - Fag: ")
    nivå = input(" - Nivå (100, 200, 300): ")

    #Ingen kriterier
    if område == "" and nivå == "":
        for emne in sorted(emner):
            print(emne, karakterer.get(emne, ""))
    #Kun fagområder
    elif område.capitalize() in fagområde and nivå == "":
        for emne in sorted(emner):
            if fagområde[område.capitalize()] in emne.upper():
                print(emne, karakterer.get(emne, ""))
    #Kun nivå
    elif område == "" and (4 > int(nivå[0]) > 0) and len(nivå) == 3:
        for emne in sorted(emner):
            if int(emne[-3]) == int(nivå[0]):
                print(emne, karakterer.get(emne, ""))
    #Nivå og fagområde
    else:
        try:
            for emne in sorted(emner):
                if int(emne[-3]) == int(nivå[0]) and len(nivå) == 3 and fagområde[str(område.capitalize())] in emne.upper():
                    print(emne, karakterer.get(emne, ""))
            if 0 > nivå[0] or nivå[0] > 3:
                print("Ikke gyldige emner.")
        except:
            print("Fant ingen fag.")


def lovligemnekode(kode):
    hjelp = """Ikke gyldig emnekode.
 - Koden skal starte med tre eller fire bokstaver.
 - Koden skal avsluttes med tre siffer, hvor det første skal være mellom 1 og 3 etter nivå.
 - Koden må finnes under et fagfelt.
    """
    lovlig = []
    for bokstav in kode:
        if bokstav.isalpha():
            lovlig.append(bokstav)
    try:
        if ("".join(lovlig) in list(fagområde.values())) and (0 < int(kode[-3]) < 4) and (5 < len(kode) < 8) and (kode[:3].isalpha() and (int(kode[-3:].isalnum()))):
            return True
        else:
            print(hjelp)
            return False
    except:
        print(hjelp)


def leggtil():
    global emner, fagområde
    nyttemne = str(input("Nytt emne:\n"))
    if nyttemne.upper() in emner:
        print("Emne eksisterer allerede")
    elif lovligemnekode(nyttemne.upper()):
        emner.append(nyttemne.upper())
        print(nyttemne.upper(), "lagt til.")


def endrekarakter():
    global emner, karakterer, fagområde
    emne = input("Emne:\n")
    if emne.upper() in emner:
        nykarakter = input("Karakter A-F (<enter> for å slette):\n")
        if (0 < len(nykarakter) < 2) and (nykarakter.upper() in "ABCDEF"):
            karakterer[emne.upper()] = nykarakter.upper()
        else:
            print("Ikke gyldig karakter. A-F(<enter> for å slette)")
    else:
        print("Fant ikke emne. Om du ønsker legge til emne <tast 2>")


def snitt():
    global emner, karakterer, fagområde
    print("Velg fag og/eller emnenivå (<enter> for alle)")

    total = {"A": 6, "B": 5, "C": 4, "D": 3, "E": 2, "F": 1}
    poeng = []

    def snittkalkulator(liste):
        avg = (sum(poeng)) / len(poeng)
        for key, value in total.items():
            if value == round(avg):
                print("Snitt:", key)

    område = input(" - Fag: ")
    nivå = input(" - Nivå (100, 200, 300): ")

    try:
        #Ingen krav
        if område == "" and nivå == "":
            for key, value in karakterer.items():
                poeng.append(total[value])

            snittkalkulator(poeng)
        #Kun nivå
        elif område == "" and (0 < int(nivå[0]) < 4) and len(nivå) == 3:
            for key, value in karakterer.items():
                if (key[-3]) == nivå[0]:
                    poeng.append(total[value])

            snittkalkulator(poeng)
        #Kun fagområde
        elif nivå == "" and område.capitalize() in fagområde:
            for emne in emner:
                if fagområde[område.capitalize()] in emne:
                    for key, value in karakterer.items():
                        if emne == key:
                            poeng.append(total[value])

            snittkalkulator(poeng)

        #Begge deler
        elif (0 < int(nivå[0]) < 4) and len(nivå) == 3 and område.capitalize() in fagområde:
            for emne in emner:
                if fagområde[område.capitalize()] in emne:
                    for key, value in karakterer.items():
                        if (key[-3]) == str(nivå[0]) and key == emne:
                            poeng.append(total[value])
            try:
                snittkalkulator(poeng)
            except:
                print("Ingen karakterer funnet som matchet søk.")
        else:
            print("Ingen karakterer funnet som matchet søk. ")
    except:
        print("Ingen karakter funnet som matchet søk. ")


def valg():
    global emner, karakterer, fagområde

    with open("karakterer.txt", encoding="utf-8") as dokument:
        for line in dokument:
            (key, value) = line.split()
            karakterer[key] = value

    with open("emner.txt", encoding="utf-8") as dokument:
        for line in dokument:
            emner.append(line.strip("\n"))

    info = ("""--------------------
1 Emneliste
2 Legg til emne
3 Sett karakter
4 Karaktersnitt
5 Avslutt
6 Lagre
--------------------""")
    print(info)
    while True:
        try:
            handling = int(input("Velg handling (0 for meny):\n"))
            if handling == 1: emneliste()
            elif handling == 2: leggtil()
            elif handling == 3: endrekarakter()
            elif handling == 4: snitt()
            elif handling == 5:
                print("Takk for nå.")
                break

            elif handling == 6:
                svar = input("Vil du lagre? (Ja/Nei)")
                if svar.capitalize() == "Ja":
                    with open("karakterer.txt", "w") as dokument:
                        for key, value in karakterer.items():
                            dokument.write(key + " " + value + "\n")
                    with open("emner.txt", "w") as dokument:
                        for item in emner:
                            dokument.write(item + "\n")
                    print("Takk for nå.")
                    break

            elif handling == 0: print(info)
            else: print("Kun tall mellom 1-6 gyldig.")
        except: print("Kun tall mellom 1-6 gyldig.")

valg()
