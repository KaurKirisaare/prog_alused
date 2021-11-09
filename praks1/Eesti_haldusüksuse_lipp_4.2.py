from tkinter import *

a = Tk()
a.title("Kiviõli lipp")
b = Canvas(a, width = 600, height = 300)

b.create_rectangle(0,0,600,135, fill ="blue", outline = "blue")
b.create_rectangle(0,135,600,165, fill = "white", outline = "white")
b.create_rectangle(0,165,600,300, fill ="brown", outline = "brown")

b.pack()
a.mainloop()