from tkinter import *

a = Tk()
a.title("Liiklusmärk : Parkimiskeeld paaritul kuupäeval")
b = Canvas(a, width = 300, height = 300)

b.create_oval(10,10,290,290, fill = "red", outline = "red")
b.create_oval(30,30,270,270, fill = "blue", outline = "blue")
b.create_rectangle(140, 50, 160, 250, fill = "white", outline = "white")
b.create_polygon(80, 50, 220, 250, fill = "red", width = 15, outline = "red")

b.pack()
a.mainloop()