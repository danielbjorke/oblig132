#OPPGAVE 1
print("Daniel", "Martin", "Bjørke", sep="\n")
print("Daniel", "\nMartin", "\nBjørke")

#OPPGAVE 2
print("*          ***         ** *     *    *     * * *     *       ")
print("* *       *   *        *   *    *    *     *         *       ")
print("*  *     *     *       *    *   *    *     *         *       ")
print("*   *   ******* *      *     *  *    *     * * *     *       ")
print("*  *    *       *      *      * *    *     *         *       ")
print("* *     *       *      *       **    *     *         *       ")
print("*       *       *      *       **    *     * * *     * * **  ")


#OPPGAVE 3

#Hente inn sum i kroner
nok = float(input("hvor mange norske kroner vil du gjøre om til Euro og dollar? "))

#Gjøre om sum i variabler
euro = ("%.2f" % (nok / 10.1))
dollar = ("%.2f" % (nok / 8.96))

#Skrive ut omggjort sum
print(str(nok) + " Kroner tilsvarer " + str(euro) + " Euro og " + str(dollar) + " Dollar")

#Skirve ut omgjort sum med valuta symboler
print("Nok " + str(nok)+ " tilsvarer " + (str(dollar)) + (u"\N{dollar sign}" ) + " og " + str(euro) + (u"\N{euro sign}"))




