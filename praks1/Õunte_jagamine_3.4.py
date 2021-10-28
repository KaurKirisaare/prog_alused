from random import randint

a = int(input("Mitu pöialpoissi tahab õunu (0-7)? "))
d = 0
c = 14

while a > d:
    b = randint(1, 2)
    c = c - b
    d = d + 1
    print(b)

print("Lumivalgekesele jäi " + str(c))