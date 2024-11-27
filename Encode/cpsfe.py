tekst = input("Tekst: ")
glebia = int(input("Glebia: "))

przedzialy = [[48,57,10],[65,90,26],[97,122,26]]

tekst2 = ""
for i in tekst:
    litera_ascii = ord(i)
    for x in przedzialy:
        if litera_ascii >= x[0] and litera_ascii <= x[1]:
            litera_ascii += glebia%x[2]
            if litera_ascii > x[1]:
                litera_ascii = x[0] + (litera_ascii%x[1]-1)%x[2]
    tekst2 += chr(litera_ascii)
print(tekst2)
input()
