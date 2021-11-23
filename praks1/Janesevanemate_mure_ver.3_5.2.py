ringi_a = int(input("Sisestage ringide arv: "))

ringi_a += 1
porg_a = 0

for a in range(2, ringi_a, 2):
    porg_a += a

print(porg_a)