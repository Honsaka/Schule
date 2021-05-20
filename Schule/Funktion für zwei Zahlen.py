def max(x , y):
    if x < y:
        maximum = y
        return (y)
    else:
        maximum = x
        return (x)
def min(x , y):
    if x < y:
        minimum = x
        return (x)
    else:
        minimum = y
        return (y)
def mitte(x ,y):
    mittelwert = (x + y)/2
    return (mittelwert)
def abs (x,y):
    if x < y:
        absoluter = (y-x)
        return (absoluter)
    if y < x:
        absoluter = (x-y)
        return (absoluter)



zahl1 =  int(input("Nennen Sie den Summenanfang: "))
zahl2 = int(input("Nennen Sie das Summenende: "))
maximum = max(zahl1,zahl2)
minimum = min(zahl1,zahl2)
mittelwert = mitte(zahl1,zahl2)
absoluter = abs(zahl1,zahl2)
print("Maximum:",maximum,"Minimum:",minimum,"Mittelwert:",mittelwert,"Absoluter Abstand",absoluter)