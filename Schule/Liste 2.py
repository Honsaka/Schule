a = []
antwort = "1"
while antwort != "":
    antwort = input("Schreibe etwas: ")
    a.append(antwort)
print(a)
for i in reversed(a):
    print(i)
