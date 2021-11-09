a = int(input("Sisestage täisarv: "))

b = 1
c = 0

if a == 0:
    print("Nisuteri 0. ruudu eest: 0")
elif a > 64 or a < 0:
    print("Malelaual on 64 ruutu, arv on liiga suur või negatiivne!")

else:
    c = 1
    while b < a:
        b += 1
        c *= 2
    print("Nisuteri " + str(a) + ". ruudu eest: " + str(c))