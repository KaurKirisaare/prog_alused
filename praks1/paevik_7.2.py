from datetime import datetime
paev_kell = datetime.today()

fail = open("paevik.txt", "a", encoding = "UTF-8")

kiri = input("Sisestage sissekande tekst: ")
fail.write(str(paev_kell) + "\n")
fail.write(kiri + "\n")

fail.close