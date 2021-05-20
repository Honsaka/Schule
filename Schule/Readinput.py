e = []
def read_string():
    Eingabe = input("Hi:")
    a = str(Eingabe)
    return a
def read_int():
    while True:
        b = input("Zahl:")
        if b.isdigit():
            b = int(b)
            return b
def read_bool():
    while True:
        c = input("Wahreihtswert:")
        if c.lower() == "ja" or c.lower() == "j" or c == "1" or c.lower() == "true" or c.lower() == "t":
            return True
        elif c.lower() == "nein" or c.lower() == "n" or c == "0" or c.lower() == "false" or c.lower() == "f":
            return False
def read_list():
    while True:
        d = input("Irgendwas:")
        e.append(d)
        if d == "":
            return e
def read_float():
    while True:
        punkte = 0
        kommas = 0
        zahlen = 0
        f = input("Irgendwas:")
        for x in range (0,len(f)):
            if f[x].isdigit():
                zahlen += 1
            elif f[x] == ".":
                punkte += 1
            elif f[x] == ",":
                kommas += 1
        if len(f) == zahlen + 1:
            if punkte + kommas <= 1:
                f = f.replace(",", ".")
                f = float(f)
            return f
print(read_string())
print(read_int())
print(read_bool())
print(read_float())
print(read_list())