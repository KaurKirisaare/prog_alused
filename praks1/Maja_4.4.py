from tkinter import *

a = Tk()
a.title("Maja")
b = Canvas(a, width = 300, height = 300)

b.create_rectangle(50,100, 250, 300, fill = "yellow")
b.create_rectangle(170,210, 225, 300, fill = "brown")
b.create_oval(80,120,140,200, fill = "lightblue")
b.create_rectangle(40,100, 260, 90, fill = "gray")
b.create_oval(180,255,185,260, fill = "black")

b.pack()
a.mainloop()