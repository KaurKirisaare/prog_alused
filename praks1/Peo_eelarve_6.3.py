def eelarve(külaliste_arv):
    kokku = (külaliste_arv * 10) + 55
    return kokku

kutsutud = int(input("Mitu inimest on kutsutud? "))
tulevad = int(input("Mitu inimest tuleb? "))

max_eelarve = eelarve(kutsutud)
min_eelarve = eelarve(tulevad)

print("Maksimaalne eelarve: " + str(max_eelarve))
print("Minimaalne eelarve: " + str(min_eelarve))