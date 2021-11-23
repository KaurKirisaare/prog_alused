fail = open("sisseranne.txt", encoding="UTF-8")
sisse_r = []
for ränne in fail:
    sisse_r.append(ränne)
fail.close

fail = open("valjaranne.txt", encoding="UTF-8")
valja_r = []
for ränne in fail:
    valja_r.append(ränne)
fail.close

randesaldoloend = []
i = 0
while i < 10:
    randesaldoloend.append(int(sisse_r[i]) - int(valja_r[i]))
    i += 1
print(randesaldoloend)
if max(randesaldoloend) > 0:
    print("Suurim positiivne rändesaldo oli " + str(i) +". aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")