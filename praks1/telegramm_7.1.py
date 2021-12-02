fail = open(input("Sisestage failinimi: "), encoding = "UTF-8")
sonum = fail.read().upper().replace("Ä", "AE").replace("Õ", "OE").replace("Ü", "UE")

print(sonum)
fail.close