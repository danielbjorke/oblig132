#oppgave1
def leggtil(): #Kunne hatt argumenter som antall å legge til for eksempel.

    antall = int(input("Hvor mange navn og nummer skal du legge til?\n"))
    print("Legg til navn og nummer, avlsutt med <enter>")

    while antall > 0:
        navnnummer = str(input("Navn og nummer:\n"))
        with open("telefon.txt", "a", encoding="utf-8") as nummer:
            nummer.write("\n" + navnnummer)
        antall -= 1
    print("Navn og nummer lagt til.  ")

#oppgave2
def endreTlf(): #Kunne hatt navn som argument feks, men holder den tom for oppgavens del.
    with open("telefon.txt", encoding="utf-8") as telefon:
        innhold = telefon.read()

    navn = input("Navn:\n")

    for plassering, ord in enumerate(innhold.split()):
        if ord == navn.capitalize():
            gammeltnummer = (innhold.split()[plassering+1])
            print("Gammelt telefonnummer:", gammeltnummer)
            nyttnummer = input("Nytt telefonnummer:\n")
            innhold = innhold.replace(gammeltnummer, nyttnummer)

            with open("telefon.txt", "w", encoding="utf-8") as telefon:
                telefon.write(innhold)

#oppgave3
def fjernVokaler(fil):
    try:
        vokaler = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"]

        with open(fil, encoding="utf-8") as tresmå:
            innhold = tresmå.read()

        for bokstav in vokaler:
            innhold = innhold.replace(bokstav, "")

        with open("NYtreSmåKinesere.txt", "w", encoding="utf-8") as tresmå:
            tresmå.write(innhold)
    except:
        print("Fant ingen fil.")


