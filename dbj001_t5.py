#Oppgave1
def antallVokaler(tekst):
    vokaler = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"]
    antall = 0
    for bokstav in tekst.lower():
        if bokstav in vokaler:
            antall += 1
    return antall

#Oppgave2
velforening = """Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
"""

def verv(navn):

    vervliste = []
    antall = 0
    neste_start = 0

    while antall < tv.count(navn.capitalize()):
        stopp = tv.find(navn.capitalize(),neste_start) - 2
        lengdeverv = tv[stopp::-1].find("\n")
        start = stopp - lengdeverv + 1
        vervliste.append(tv[start:stopp].capitalize())
        antall += 1
        neste_start = stopp + len(navn)

    return(vervliste)


print(verv("kari"))
