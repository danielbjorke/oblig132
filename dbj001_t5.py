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
    forening = list(velforening.split())
    alleverv = []

    for plassering, word in enumerate(forening):
        if word == navn.capitalize():
            alleverv.append(forening[plassering - 1].replace(":", "").capitalize())

    return(alleverv)


print(verv("kari"))
