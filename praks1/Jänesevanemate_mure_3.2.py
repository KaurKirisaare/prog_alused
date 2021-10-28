a = int(input("Sisestage ringide arv: "))
b = 0
c = 0
d = 0

while  b < a - 1:
    c = c + 2 + d
    d = d + 2
    b = b + 2

print("Porgandite koguarv on " + str(c))