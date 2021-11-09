a = int(input("Sisestage ringide arv: "))

b = 1
c = 0
d = 0

while b <= a:
    d += b
    b += 1
    c = d + c
    
print("Porgandite koguarv on " + str(c))