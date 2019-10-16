karakterer = {"INFO100": "A", "INFO104": "D", "INFO110": "B", "INFO125": "C", "INFO280": "B", "ECON100": "B", "DIKULT105": "B"}

emner = ["INFO100", "INFO1004", "INFO110", "INFO125", "INFO280", "ECON100", "ECON200", "DIKULT105", "DIKULT106", "EXP100", "EXP200"]

fagområde = {"Informasjonsvitenskap": "INF", "Økonomi": "ECON", "Filosofi": "EXP"}







def emneliste():
    global emner, karakterer, fagområde
    print("Velg fag og/eller emnenivå (<enter> for alle)")

    område = input(" - Fag: ")
    nivå = input(" - Nivå: ")

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
            if int(emne[-3]) == tall and fagområde[område] in emne.upper():
                print(emne, karakterer.get(emne, ""))

    #Ingen kritierer
    def ingen():
        for emne in emner:
            print(emne, karakterer.get(emne, ""))

    if område == "" and nivå == "":
        ingen()

    elif område in fagområde and nivå == "":
        velgområde(område)

    elif område == "" and (int(nivå) < 4 and int(nivå) > 0):
        emnenivå(nivå)

    else:
        beggedeler(område, int(nivå))


emneliste()


def leggtil():
    global fag
    print(emner[1]["Informajonsvitenskap"])


def settkarakter():
    pass


def snitt():
    pass


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
        handling = int(input("Velg handling (0 for meny):\n"))
        if handling == 1: emneliste()
        elif handling == 2: leggtil()
        elif handling == 3:
            pass
        elif handling == 4:
            pass
        elif handling == 5:
            print("Avsluttet.")
            break
        elif handling == 0: print(info)

