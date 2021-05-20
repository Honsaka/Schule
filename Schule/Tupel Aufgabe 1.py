herzkarten = [("Herz","7"),("Herz","8"),("Herz","9"),("Herz","10"),("Herz","Bube"),("Herz","Dame"),("Herz","König"),("Herz","Ass")]
pikkarten = [("Pik","7"),("Pik","8"),("Pik","9"),("Pik","10"),("Pik","Bube"),("Pik","Dame"),("Pik","König"),("Pik","Ass")]
karokarten = [("Karo","7"),("Karo","8"),("Karo","9"),("Karo","10"),("Karo","Bube"),("Karo","Dame"),("Karo","König"),("Karo","Ass")]
kreuzkarten = [("Kreuz","7"),("Kreuz","8"),("Kreuz","9"),("Kreuz","10"),("Kreuz","Bube"),("Kreuz","Dame"),("Kreuz","König"),("Kreuz","Ass")]
karten = [kreuzkarten,karokarten,pikkarten,herzkarten]
print(kreuzkarten[0])
print(herzkarten[-1])
for alles in [kreuzkarten,karokarten,pikkarten,herzkarten]:
    print(alles)