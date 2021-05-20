def summe(zahl1 , zahl2):
    summe = zahl2
    for i in range (zahl1, zahl2):
        summe += 1
    return summe



eins =  int(input("Nennen Sie den Summenanfang: "))
zwei = int(input("Nennen Sie das Summenende: "))
ergebniss = summe(eins,zwei)
print("Die Summe der Zahlen von",eins ,"bis",zwei,"lautet:",ergebniss)