karakterer = {"INFO100": "B", "INFO104": "A", "INFO110": "B", "INFO125": "C", "INFO280": "A", "ECON100": "A", "DIKULT105": "A"}

emner = ["INFO100", "INFO104", "INFO110", "INFO125", "INFO280", "ECON100", "ECON200", "DIKULT105", "DIKULT106", "EXP100", "EXP200"]

fagområde = {"Informasjonsvitenskap": "INF", "Økonomi": "ECON", "Filosofi": "EXP"}


def emneliste():
    global emner, karakterer, fagområde
    print("Velg fag og/eller emnenivå (<enter> for alle)")

    område = input(" - Fag: ")
    nivå = input(" - Nivå (1-3): ")

    # kun et fagområde
    def velgområde(område):
        for emne in emner:
            if fagområde[område] in emne.upper():
                print(emne, karakterer.get(emne, ""))

    # kun et niva
    def emnenivå(tall):
        for emne in emner:
            if int(emne[-3]) == int(tall):
                print(emne, karakterer.get(emne, ""))

    # begge deler
    def beggedeler(område, tall):
        for emne in emner:
            if int(emne[-3]) == int(tall) and fagområde[str(område)] in emne.upper():
                print(emne, karakterer.get(emne, ""))


    #Ingen kritierer
    def ingen():
        for emne in emner:
            print(emne, karakterer.get(emne, ""))

    if område == "" and nivå == "":
        ingen()

    elif område.capitalize() in fagområde and nivå == "":
        velgområde(område.capitalize())

    elif område == "" and (int(nivå) < 4 and int(nivå) > 0):
        emnenivå(nivå)

    else:
        try: beggedeler(område.capitalize(), int(nivå))
        except: print("Fant ingen fag.")


def lovligemnekode(kode):
    hjelp = """Ikke gyldig emnekode.
 - Koden skal starte med tre eller fire bokstaver.
 - Koden skal avsluttes med tre siffer, hvor det første skal være mellom 1 og 3 etter nivå.
    """
    try:
        if (0 < int(kode[-3]) < 4) and (5 < len(kode) < 8) and (kode[:3].isalpha() and (int(kode[-3:].isalnum()))):
            return True
        else:
            print(hjelp)
            return False
    except:
        print(hjelp)


def leggtil():
    global emner
    nyttemne = str(input("Nytt emne:\n"))
    if lovligemnekode(nyttemne):
        emner.append(nyttemne)
        print(nyttemne, "lagt til.")


def endrekarakter():
    global emner, karakterer
    emne = input("Emne:\n")
    if emne.upper() in emner:
        nykarakter = input("Karakter A-F (<enter> for å slette):\n")
        if (0 < len(nykarakter) < 2) and (nykarakter.upper() in "ABCDEF"):
            karakterer[emne] = nykarakter.upper()
        else:
            print("Ikke gyldig karakter. A-F(<enter> for å slette)")
    else:
        print("Fant ikke emne. Om du ønsker legge til emne <tast 2>")


def snittkalkulator(fagområde, nivå):
    global karakterer, emner
    total = {"A": 6, "B": 5, "C": 4, "D": 3, "E": 2, "F": 1}
    poeng = []
    for emne in liste:
        if ((karakterer.get(emne, "Ingen"))) != "Ingen":
            tall = ((karakterer.get(emne, "Ingen")))
            poeng.append(total[tall])

    avg = (sum(poeng)) / len(poeng)
    for key, value in total.items():
        if value == round(avg):
            return (key)


def snitt():




def valg():
    info = ("""--------------------
1 Emneliste
2 Legg til emne
3 Sett karakter
4 Karaktersnitt
5 Avslutt
--------------------""")
    print(info)
    while True:
        try:
            handling = int(input("Velg handling (0 for meny):\n"))
            if handling == 1: emneliste()
            elif handling == 2: leggtil()
            elif handling == 3: endrekarakter()
            elif handling == 4:
                pass
            elif handling == 5:
                print("Avsluttet.")
                break
            elif handling == 0: print(info)
            else: print("Kun tall mellom 1-5 gyldig.")
        except: print("Kun tall mellom 1-5 gyldig.")

