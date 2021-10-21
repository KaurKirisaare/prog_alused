a = int(input("Sisestage enda vanus : "))
b = input("Sisestage enda sugu (m/n) : ")
print("Treeningutüüpid : 1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening")
c = int(input("Sisestage treeningutüüp : "))

if b == "n" or b == "N":
    if c == 1:
        d = 206 - (a/100*88)
        n1 = round(d/100*50)
        n2 = round(d/100*70)
    elif c == 2:
        d = 206 - (a/100*88)
        n1 = round(d/100*70)
        n2 = round(d/100*80)
    elif c == 3:
        d = 206 - (a/100*88)
        n1 = round(d/100*80)
        n2 = round(d/100*87)
if b == "m" or b == "M":
    if c == 1:
        d = 220 - a
        n1 = round(d/100*50)
        n2 = round(d/100*70)
    elif c == 2:
        d = 220 - a
        n1 = round(d/100*70)
        n2 = round(d/100*80)       
    elif c == 3:
        d = 220 - a
        n1 = round(d/100*80)
        n2 = round(d/100*87)

print("Pulsisagedus peaks olema vahemikus " + str(n1) + " kuni " + str(n2))