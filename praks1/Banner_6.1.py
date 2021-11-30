def banner(b):
    return b.upper()
    
a = int(input("Mitu korda soovite reklaamlauset kuvada? "))
b = input("Sisestage reklaamlause: ")

for i in range(0, a):
    print(banner(b))