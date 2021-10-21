print("Sisestage oma nimi: ")
nimi = input()

print("Sisestage lubatgud kiirus: ")
lub_kiirus = int(input())

print("Sisestage tegelik kiirus: ")
teg_kiirus = int(input())

if teg_kiirus > lub_kiirus:
    c = teg_kiirus - lub_kiirus
    d = c * 3
else:
    trahv = 0
    
if d > 190:
    d = 190
    
print(nimi + ". kiiruse ületamise eest on teie trahv " + str(d) + " eurot.")