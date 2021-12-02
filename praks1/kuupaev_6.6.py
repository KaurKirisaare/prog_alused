def kuu_nimi(mitmes):
    kuu = ["jaanuar", "veebruar", "märts", "april", "mai", "juuni", "juuli", "august", "septemper", "oktoober", "november", "detsember"]
    return kuu[int(mitmes) - 1]

def kuupaev_sonena(kuupaev):
    kuupaevad = kuupaev.split(".")
    kuupaev = kuupaevad[0] + ". " + kuu_nimi(kuupaevad[1]) + " " + kuupaevad[2] + ". a"
    return kuupaev

kuupaev = input("Siseta kuupäev kujul DD.MM.YYYY ")
print(str(kuupaev_sonena(kuupaev)))