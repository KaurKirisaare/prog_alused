from datetime import *

fail = open(input("Sisestage faili nimi: "), encoding="UTF-8")
nimed = []
for nimi in fail:
    nimed.append(nimi)

print("Vastama tuleb: " + str(nimed[int(datetime.now().day) - 1]))
fail.close