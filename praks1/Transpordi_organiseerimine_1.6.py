ini_a= int(input("inimeste arv : "))
koht_a=int(input("kohtade arv : "))

if koht_a>ini_a:
    print ("Busse oli 1 ja maha jäi " + str(ini_m) + " inimest.")
    
else:
    üle = ini_a % koht_a
    if üle>0:
        busse = (ini_a//koht_a)
        print ("Busse oli "+str(busse) + " ja maha jäi " + str(üle) + " inimest.")
    elif üle==0:
        busse = (ini_a//koht_a)
        print ("Busse oli "+str(busse) + " ja maha jäi " + str(koht_a) + " inimest.")
    else:
        busse = (ini_a//koht_a)
        print ("Busse oli "+str(busse) + " ja maha jäi " + str(ini_m) + " inimest.")