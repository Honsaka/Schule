picture = [["-", "o", "o", "o", "o", "-", "-", "-"],
           ["-", "o", "-", "-", "-", "o", "-", "-"],
           ["-", "o", "-", "-", "-", "o", "-", "-"],
           ["-", "o", "o", "o", "o", "-", "-", "-"],
           ["-", "o", "o", "-", "-", "-", "-", "-"],
           ["-", "o", "-", "o", "-", "-", "-", "-"],
           ["-", "o", "-", "-", "o", "-", "-", "-"],
           ["-", "o", "-", "-", "-", "o", "-", "-"]]

def normal():
    print()
    print("normal")
    print()
    for reihe in picture:
        for zeichen in reihe:
            print(zeichen, end="")
        print()

platz = normal()

def horizontal():
    print()
    print("horizontal")
    print()
    for reihe in picture[::-1]:
        for zeichen in reihe:
            print(zeichen, end="")
        print()

platz = horizontal()

def vertikal():
    print()
    print("vertikal")
    print()
    for reihe in picture:
        for zeichen in reihe[::-1]:
            print(zeichen, end="")
        print()

platz = vertikal()

def neunzig():
    print()
    print("90°")
    print()
    for i in range(len(picture[0])):
        for j in range(len(picture)):
            print(picture[-1-j][i], end="")
        print()

platz = neunzig()

def hundertachzig():
    print()
    print("180°")
    print()
    for reihe in picture[::-1]:
        for zeichen in reihe[::-1]:
            print(zeichen, end="")
        print()
platz = hundertachzig()

def zweihundertsiebzig():
    print()
    print("270°")
    print()
    for i in range(len(picture[0])):
        for j in range(len(picture)):
            print(picture[j][-1-i], end="")
        print()
platz = zweihundertsiebzig()