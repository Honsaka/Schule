def decimal_to_binary(IPadresse):
    if IPadresse >= 128:
        IPadresse -= 128
        a = "1"
    else:
        a = "0"
    if IPadresse >= 64:
        IPadresse -= 128
        b = "1"
    else:
        b = "0"
    if IPadresse >= 32:
        IPadresse -= 32
        c = "1"
    else:
        c = "0"
    if IPadresse >= 16:
        IPadresse -= 16
        d = "1"
    else:
        d = "0"
    if IPadresse >= 8:
        IPadresse -= 8
        e = "1"
    else:
        e = "0"
    if IPadresse >= 4:
        IPadresse -= 4
        f = "1"
    else:
        f = "0"
    if IPadresse >= 2:
        IPadresse -= 2
        g = "1"
    else:
        g = "0"
    if IPadresse >= 1:
        IPadresse -= 1
        h = "1"
    else:
        h = "0"
    binaer = a+b+c+d+e+f+g+h
    return binaer

def  binary_to_decimal (binaer):
    if binaer = 10000000
    binaer ==

#IPadresse = int(input("IP adresse in Dezimal"))
#11111111 = 255
