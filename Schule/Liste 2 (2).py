a = "a"
b = []
while a != "ende":
    print("1) Liste anzeigen")
    print("2) Listenelemente hinten anfügen")
    print("3) Listenelement an einer bestimmten Stelle einfügen")
    print("4) Listenelement löschen")
    print("5) Suchen (Vorhandensein bestätigen und Index eines Elementes ausgeben)")
    a = str(input("Was möchten sie tun(ende für das Ende)? "))
    if a == "1":
        print(b)
    elif a == "2":
        c = (input("Und was ? "))
        b.append(c)
    elif a == "3":
        d = (input("Und was ? "))
        e = int(input("An welcher Stelle ? "))
        e -= 1
        b.insert(e,d)
    elif a == "4":
        f = (input("Und was ? "))
        b.remove(f)
    elif a == "5":
        h = ""
        g = (input("Welches Wort ? "))
        h = b.index(g)
        if h != "":
            h += 1
            print("Ja an der ",h,"Stelle")
        else:
            print("Die Zahl exestiert nicht")
    elif a != "ende":
        print("KEINE GÜLTIGE EINGABE!!!")
print("Ende!!!")