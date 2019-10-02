#Oppgave 1
import math
def pi(d = 2):
    if d > 15:
        print("For mange desimaler.")
        return math.pi
    else:
        return(round(math.pi, d))

#Oppgave 2
def temperaturKonvertering(temp, skala="C"):
    if skala.lower() == "c":
        return(temp * 1.8 + 32)
    elif skala.lower() == "f":
        return((temp - 32) / 1.8)
    else:
        print("Temperaturen skal være oppgitt i (C)elcius eller (F)ahrenheit")

#Oppgave 3
saldo = 500
rentesats = 0.01
endringer = []

def innskudd(sum):
    global saldo,endringer, rentesats

    saldo += sum
    endringer.append("+ " + str(sum))

    if rentesats == 0.01 and saldo > 1000000:
        rentesats = 0.02
        print("Gratulerer, du får bonusrente.")

    return saldo


def uttak(sum):
    global saldo, endringer, rentesats

    if (saldo - sum) < 0:
        print("Overtrekk ikke mulig")
        return saldo
    else:
        saldo -= sum
        endringer.append("- " + str(sum))
        if rentesats == 0.02 and (saldo <= 1000000):
            rentesats = 0.01
            print("Du har nå ordinær rente.")
        return saldo

def beregnRente():
    global saldo, rentesats
    return(saldo * rentesats)

def renteoppgjør():
    global saldo, rentesats
    saldo += beregnRente()
    endringer.append("+ " + str(round(beregnRente(), 1)))
    return saldo

def velg():
    global saldo
    global rentesats
    global endringer
    print("""- - - - - - - - -
1 - vis saldo
2 - innskudd
3 - uttak
4 - renteoppgjør
5 - siste endringer 
6 - avslutt
- - - - - - - - -""")
    while True:
        try:
            inntast = int(input("velg handling: "))
            if inntast == 1:
                print(saldo)
            elif inntast == 2:
                beløp = int(input("Beløp: "))
                innskudd(beløp)
            elif inntast == 3:
                beløp = int(input("Beløp: "))
                uttak(beløp)
            elif inntast == 4:
                print(renteoppgjør())
            elif inntast == 5:
                for i,b in enumerate(endringer[::-1]):
                    if i <= 2:
                        print(b)
            elif inntast == 6:
                print("Avsluttet.")
                break
            else:
                print("Velg mellom alternativene.")
        except:
            print("Kun tall.")

velg()

#Oppgave 4
import random
def tilfeldig3():
    tall1 = (random.randint(1,9))
    tall2 = (random.randint(1,9))
    tall3 = (random.randint(1,9))
    liste = [str(tall1), str(tall2), str(tall3)]
    return int(("".join(sorted((liste)))))
