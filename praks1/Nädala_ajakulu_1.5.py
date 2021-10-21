print("Sisestage ainepunktide arv: ")
a = int(input())

print("Sisestage nädalate arv: ")
b = int(input())

c = a*26 / b

vastus = "Ühe nädala eeldatava ajakulu : " + str(round(c))

print(vastus)