def mahlapakkide_arv(b):
    mahlapakkide_arv = b * 0.4 / 3
    return round(mahlapakkide_arv)

b = float(input("Mitu kilogrammi õunu on? "))

print(mahlapakkide_arv(b))