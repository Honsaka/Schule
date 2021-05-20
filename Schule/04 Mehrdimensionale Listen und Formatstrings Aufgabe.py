invoice = [
    # Tupel: Anzahl, Artikelnummer, Beschreibung, Einzelpreis
    (2, "57620676", "Tastatur", 24.95),
    (3, "29878362", "Kabelbinder 6mm, 50 St.", 3.43),
    (1, "47923243", "WLAN Access Point", 123.21)
]
print("Pos.  Anzahl  Art.-Nr.  Beschreibung                     Einzelpreis  Gesamtpreis")
pos = 0
for Anzahl ,ArtikelNr,Beschreibung ,Preis in invoice:
    pos += 1
    print(f"{pos:>02}   {Anzahl:6}   {ArtikelNr:>11}  {Beschreibung:<25}  {Preis:12.2f}   {Preis * Anzahl:12.2f}")w