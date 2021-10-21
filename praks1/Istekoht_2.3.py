from random import randint

a = input("Kas soovite istekohta ise valida (ise) või loosida (loos)? : ")

if a == "ise":
    b = input("Kas soovite istuda akna ääres (aken) või mitte (muu)? : ")
    if b == "aken":
        print("Valisite ise. Aknakoht")
    elif b == "muu":
        print("Valisite ise. Vahekäigukoht")
if a == "loos":
    b = randint(1, 3)
    if b == 1:
        print("Istekoht loositi. Aknakoht")
    elif b >= 2:
        print("Istekoht loositi. Vahekäigukoht")