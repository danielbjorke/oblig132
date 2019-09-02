#Oppgave 1

#Henter inn matte modulen for å få tilgang til ferdiglagte funksjoner
import math
import random

#Ber bruker om radius
tall = float(input("Hva er radiusen til sirkelen?\n"))
#Gjør om input fra bruker til areal med hjelp av math.pi funksjonen
areal = (math.pi * tall * tall)
#Print ut arealet av sirkelen til brukeren
print("Arealet til en sirkelen med radius " + str(tall) + " er " + str(round(areal, 3)))

#Oppgave 2

#Henter inn setning fra bruker
setning = input("Skriv inn et setning:\n")
#Gjør om setning til en talllengde
fasit = len(setning)
#Lar bruker gjette et antall tall, og bestem booleansk verdi
forsøk = int(input("Hvor mange bokstaver tror du det var i den setningen?\n")) == fasit
#Skriver ut tilbakemelding om forsøket var riktig eller galt
print("Det er " + str(forsøk))

#Oppgave 3

#Henter inn tall fra bruker
tall_1 = int(input("Gi meg et tall:\n"))
#Lager tilfeldig tall
tilfeldig_tall = (str(random.randint(0,9)))
#Setter sammen tallene
sammensatt_tall = int((str(tall_1) + str(tilfeldig_tall)))
#Deler det sammensatte tallet med det tilfeldig lagte tallet
sum = (int(sammensatt_tall)//int(tilfeldig_tall))
#Printer ut regnestykket og fasit
print(str(sammensatt_tall) + "/" + str(tilfeldig_tall) + " = " + str(sum))