from tkinter import *

pealkiri = Tk()
pealkiri.title("malelaud")
laud = Canvas(width = 600, height = 600)

# 1 rida
laud.create_rectangle(0,0,75 ,75 , fill = "black")
laud.create_rectangle(150,0,225 ,75 , fill = "black")
laud.create_rectangle(300,0,375 ,75 , fill = "black")
laud.create_rectangle(450,0,525 ,75 , fill = "black")

# 2 rida
laud.create_rectangle(75,75,150 ,150 , fill = "black")
laud.create_rectangle(225,75,300 ,150 , fill = "black")
laud.create_rectangle(375,75,450 ,150 , fill = "black")
laud.create_rectangle(525,75,600 ,150 , fill = "black")

# 3 rida
laud.create_rectangle(0,150,75 ,225 , fill = "black")
laud.create_rectangle(150,150,225 ,225 , fill = "black")
laud.create_rectangle(300,150,375 ,225 , fill = "black")
laud.create_rectangle(450,150,525 ,225 , fill = "black")

# 4 rida
laud.create_rectangle(75,225,150 ,300 , fill = "black")
laud.create_rectangle(225,225,300 ,300 , fill = "black")
laud.create_rectangle(375,225,450 ,300 , fill = "black")
laud.create_rectangle(525,225,600 ,300 , fill = "black")

# 5 rida
laud.create_rectangle(0,300,75 ,375 , fill = "black")
laud.create_rectangle(150,300,225 ,375 , fill = "black")
laud.create_rectangle(300,300,375 ,375 , fill = "black")
laud.create_rectangle(450,300,525 ,375 , fill = "black")

# 6 rida
laud.create_rectangle(75,375,150 ,450 , fill = "black")
laud.create_rectangle(225,375,300 ,450 , fill = "black")
laud.create_rectangle(375,375,450 ,450 , fill = "black")
laud.create_rectangle(525,375,600 ,450 , fill = "black")

# 7 rida
laud.create_rectangle(0,450,75 ,525 , fill = "black")
laud.create_rectangle(150,450,225 ,525 , fill = "black")
laud.create_rectangle(300,450,375 ,525 , fill = "black")
laud.create_rectangle(450,450,525 ,525 , fill = "black")

# 8 rida
laud.create_rectangle(75,525,150 ,600 , fill = "black")
laud.create_rectangle(225,525,300 ,600 , fill = "black")
laud.create_rectangle(375,525,450 ,600 , fill = "black")
laud.create_rectangle(525,525,600 ,600 , fill = "black")

laud.pack()
pealkiri.mainloop()