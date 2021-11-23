fail = str(input("Palun sisestage failinimi: "))

fail = open(fail, encoding="UTF-8")

b = 1
print("Muusikapalade valik:")
c = []

for rida in fail:
    print(str(b) + ". " + str(rida[:-1]))
    b += 1
    c.append(rida)

laul_v = int(input("Valige laulu järjekorranumber: "))
laul_v -= 1

print("Mängitav muusikapala on " + c[laul_v])

fail.close()