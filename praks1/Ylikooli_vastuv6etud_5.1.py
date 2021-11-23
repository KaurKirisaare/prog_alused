fail = open("rebased.txt", encoding="UTF-8")

b = 2011

vastuvoetud = []

a = int(input("Palun sisestage, millise aasta andmeid vajate: "))

if a <= 2010 or a >= 2020:
    print(a, " aasta kohta ei ole kahjuks andmeid.")

for rida in fail:
    if a == b:
        print(b, " aastal oli vastuvõetuid ", rida)
        break
    b += 1


fail.close