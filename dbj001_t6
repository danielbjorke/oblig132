nummer = open("nummer.txt", "r+")
backup = open("backup.txt", "w")

def leggtil(fil):
    antall = int(input("Hvor mange navn og nummer skal du legge til?\n"))
    print("Legg til navn og nummer, avlsutt med <enter>")

    while antall > 0:
        navnnummer = str(input("Navn og nummer:\n"))
        fil.write("\n" + navnnummer)
        antall -= 1


def endreNummer():
    navn = str(input("Navn:\n"))
    tlf = input("Nummer:\n")

    for linje in nummer:
        if navn and tlf in linje:
            print("Ja")


endreNummer()

nummer.close()
backup.close()
