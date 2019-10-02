#Oppgave1

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

    alleverv = []
    antall = 1

    while antall <= velforening.count(navn):

        stopp = (velforening.find(navn) - 2)
        lenVerv = velforening[stopp:0:-1].find("\n")
        start = stopp - lenVerv
        ansvar = (velforening[(start + 1):stopp])
        alleverv.append(ansvar)
        antall += 1

    print(alleverv)

verv("Liv")
