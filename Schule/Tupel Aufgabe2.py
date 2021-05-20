karten = [("Herz","7"),("Herz","8"),("Herz","9"),("Herz","10"),("Herz","Bube"),("Herz","Dame"),("Herz","König"),("Herz","Ass"),("Pik","7"),("Pik","8"),("Pik","9"),("Pik","10"),("Pik","Bube"),("Pik","Dame"),("Pik","König"),("Pik","Ass"),("Kreuz","7"),("Kreuz","8"),("Kreuz","9"),("Kreuz","10"),("Kreuz","Bube"),("Kreuz","Dame"),("Kreuz","König"),("Kreuz","Ass"),("Karo","7"),("Karo","8"),("Karo","9"),("Karo","10"),("Karo","Bube"),("Karo","Dame"),("Karo","König"),("Karo","Ass")]
runde = 0
while runde !=10:
    erstekarte = int(input("Die Erstekarte(0-31):"))
    zweitekarte = int(input("Die Zweitekarte(0-31):"))
    karten.insert(erstekarte, karten[zweitekarte])
    karten.insert(zweitekarte, karten[erstekarte])
    karten.pop(erstekarte+1)
    karten.pop(zweitekarte+1)
    runde += 1
print(karten)